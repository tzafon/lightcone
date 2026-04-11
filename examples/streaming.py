"""CUA loop as a streaming SSE endpoint.

Start:  uvicorn examples.streaming:app
Call:   curl -N -X POST http://localhost:8000/tasks/stream \
          -H "Content-Type: application/json" \
          -d '{"instruction": "Go to wikipedia.org and search for Alan Turing"}'
"""

import asyncio
import json
import os
import time
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from tzafon import Lightcone
from _cua import get_computer_calls, get_messages, format_action, is_terminal_action, DONE_TOOL

app = FastAPI()
client = Lightcone()

TOOL = {
    "type": "computer_use",
    "display_width": 1280,
    "display_height": 720,
    "environment": "desktop",
}


class TaskRequest(BaseModel):
    instruction: str
    start_url: str | None = None
    max_steps: int = 50


def sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


async def run_loop(req: TaskRequest) -> AsyncIterator[str]:
    with client.computer.create(kind="desktop") as computer:
        if req.start_url:
            computer.navigate(req.start_url)
            computer.wait(2)

        yield sse("started", {"computer_id": computer.id})

        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        items = [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": req.instruction},
                    {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                ],
            }
        ]

        for step in range(req.max_steps):
            response = client.responses.create(
                model="tzafon.northstar-cua-fast",
                tools=[TOOL, DONE_TOOL],
                input=items,
            )
            items.extend(response.output or [])

            messages = get_messages(response.output)
            for text in messages:
                yield sse("message", {"step": step, "text": text})

            calls, call_ids = get_computer_calls(response.output, TOOL)
            if not calls:
                break

            for c in calls:
                yield sse("action", {"step": step, "type": c.get("type", "?")})

            if any(is_terminal_action(c) for c in calls):
                yield sse("completed", {"step": step})
                return

            computer.batch(calls)
            time.sleep(1)

            screenshot_url = computer.get_screenshot_url(computer.screenshot())
            yield sse("screenshot", {"step": step, "url": screenshot_url})

            for call_id in call_ids:
                items.append({
                    "type": "computer_call_output",
                    "call_id": call_id,
                    "output": {"type": "input_image", "image_url": screenshot_url, "detail": "auto"},
                })

        yield sse("completed", {"step": step + 1})


async def run_smoke_test() -> None:
    req = TaskRequest(
        instruction="Go to wikipedia.org and search for Alan Turing",
        max_steps=6,
    )
    count = 0
    async for event in run_loop(req):
        print(event.strip())
        count += 1
        if count >= 8:
            break


@app.post("/tasks/stream")
async def stream_task(req: TaskRequest):
    return StreamingResponse(run_loop(req), media_type="text/event-stream")


if __name__ == "__main__" and os.getenv("LIGHTCONE_STREAMING_SMOKE", "").lower() in {
    "1", "true", "yes", "on",
}:
    asyncio.run(run_smoke_test())
