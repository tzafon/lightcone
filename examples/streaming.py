"""CUA loop as a streaming SSE endpoint.

Start:  uvicorn examples.streaming:app
Call:   curl -N -X POST http://localhost:8000/tasks/stream \
          -H "Content-Type: application/json" \
          -d '{"instruction": "Go to wikipedia.org and search for Alan Turing"}'
"""

import asyncio
import json
import os
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from tzafon import Lightcone

app = FastAPI()
client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "browser",
}


class TaskRequest(BaseModel):
    instruction: str
    start_url: str | None = None
    max_steps: int = 50


def _px(coord, dim):
    """Convert a 0–1000 model coordinate to a pixel coordinate."""
    return int(coord / 1000 * dim)


def execute_action(computer, action):
    """Execute a model action on the computer session."""
    w, h = TOOL["display_width"], TOOL["display_height"]
    t = action.type
    if t == "click":
        computer.click(_px(action.x, w), _px(action.y, h))
    elif t == "double_click":
        computer.double_click(_px(action.x, w), _px(action.y, h))
    elif t == "triple_click":
        computer.click(_px(action.x, w), _px(action.y, h))
        computer.click(_px(action.x, w), _px(action.y, h))
        computer.click(_px(action.x, w), _px(action.y, h))
    elif t == "right_click":
        computer.right_click(_px(action.x, w), _px(action.y, h))
    elif t == "type":
        computer.type(action.text)
    elif t in ("key", "keypress"):
        computer.hotkey(action.keys)
    elif t == "key_down":
        computer.key_down(action.keys[0])
    elif t == "key_up":
        computer.key_up(action.keys[0])
    elif t == "scroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=action.scroll_y or 0,
            x=_px(action.x or 0, w),
            y=_px(action.y or 0, h),
        )
    elif t == "hscroll":
        computer.scroll(
            dx=action.scroll_x or 0,
            dy=0,
            x=_px(action.x or 0, w),
            y=_px(action.y or 0, h),
        )
    elif t == "navigate":
        computer.navigate(action.url)
    elif t == "drag":
        computer.drag(
            _px(action.x, w), _px(action.y, h), _px(action.end_x, w), _px(action.end_y, h)
        )
    elif t == "wait":
        computer.wait(2)


def sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


async def run_loop(req: TaskRequest) -> AsyncIterator[str]:
    with client.computer.create(kind="browser") as computer:
        if req.start_url:
            computer.navigate(req.start_url)
            computer.wait(2)

        yield sse("started", {"computer_id": computer.id})

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            tools=[TOOL],
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": req.instruction},
                        {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                    ],
                }
            ],
        )

        step = 0
        for step in range(req.max_steps):
            computer_call = next(
                (o for o in (response.output or []) if o.type == "computer_call"),
                None,
            )
            if not computer_call:
                break

            action = computer_call.action
            yield sse("action", {"step": step, "type": action.type})

            if action.type in ("terminate", "done", "answer"):
                yield sse(
                    "completed",
                    {
                        "step": step,
                        "result": action.result or action.text or action.status,
                    },
                )
                return

            execute_action(computer, action)
            computer.wait(1)

            screenshot_url = computer.get_screenshot_url(computer.screenshot())
            yield sse("screenshot", {"step": step, "url": screenshot_url})

            response = client.responses.create(
                model="tzafon.northstar-cua-fast",
                previous_response_id=response.id,
                tools=[TOOL],
                input=[
                    {
                        "type": "computer_call_output",
                        "call_id": computer_call.call_id,
                        "output": {
                            "type": "input_image",
                            "image_url": screenshot_url,
                            "detail": "auto",
                        },
                    }
                ],
            )

        yield sse("completed", {"step": step + 1})


async def run_smoke_test() -> None:
    req = TaskRequest(
        instruction=os.getenv("LIGHTCONE_TASK", "Go to wikipedia.org and search for Alan Turing"),
        start_url=os.getenv("LIGHTCONE_START_URL") or None,
        max_steps=int(os.getenv("LIGHTCONE_MAX_STEPS", "6")),
    )
    max_events = int(os.getenv("LIGHTCONE_MAX_EVENTS", "8"))
    count = 0
    async for event in run_loop(req):
        print(event.strip())
        count += 1
        if count >= max_events:
            break


@app.post("/tasks/stream")
async def stream_task(req: TaskRequest):
    return StreamingResponse(run_loop(req), media_type="text/event-stream")


if __name__ == "__main__" and os.getenv("LIGHTCONE_STREAMING_SMOKE", "").lower() in {
    "1",
    "true",
    "yes",
    "on",
}:
    asyncio.run(run_smoke_test())
