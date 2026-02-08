"""Pure-async FastAPI server with SSE streaming."""

from __future__ import annotations

import asyncio
import json
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from lightcone.agent import CUAAgent
from lightcone.clients import resolve_api_key
from lightcone.config import get_settings

app = FastAPI(title="Lightcone Agent", version="0.1.0")


# ---------------------------------------------------------------------------
# Request / state models
# ---------------------------------------------------------------------------


class TaskRequest(BaseModel):
    instruction: str = Field(..., min_length=1)
    start_url: Optional[str] = None
    max_steps: Optional[int] = Field(default=None, ge=1)
    model: Optional[str] = None
    prompt_profile: Optional[str] = None
    max_history: Optional[int] = Field(default=None, ge=0)
    temperature: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    max_tokens: Optional[int] = Field(default=None, ge=1)
    width: Optional[int] = Field(default=None, ge=1)
    height: Optional[int] = Field(default=None, ge=1)


@dataclass
class TaskState:
    task_id: str
    status: str = "running"
    result: Optional[str] = None
    error: Optional[str] = None
    started_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)


# In-memory task store.  No lock needed — single-threaded async event loop.
_TASKS: dict[str, TaskState] = {}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _extract_api_key(authorization: Optional[str]) -> str:
    if authorization:
        token = authorization.removeprefix("Bearer ").strip()
        if token:
            return token
    try:
        return resolve_api_key(None)
    except RuntimeError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc


def _normalize_status(status: str) -> str:
    return {"success": "completed", "failure": "failed"}.get(status, status)


def _build_agent(request: TaskRequest, api_key: str) -> CUAAgent:
    settings = get_settings()
    return CUAAgent(
        max_steps=request.max_steps,
        max_history_turns=request.max_history,
        temperature=request.temperature,
        max_tokens=request.max_tokens,
        top_p=settings.llm_top_p,
        model=(request.model or settings.llm_model).strip(),
        llm_timeout_s=settings.llm_timeout_s,
        max_retries=settings.llm_max_retries,
        retry_delay=settings.llm_retry_delay_s,
        viewport_width=request.width or 1280,
        viewport_height=request.height or 720,
        api_key=api_key,
        prompt_profile=request.prompt_profile,
    )


async def _run_task_async(
    task_id: str,
    request: TaskRequest,
    api_key: str,
    event_handler: Any = None,
) -> None:
    """Run the agent in a thread-pool executor so the event loop stays free."""
    loop = asyncio.get_running_loop()
    agent = _build_agent(request, api_key)

    def _sync_run() -> tuple[str, Optional[str]]:
        return agent.run(
            task=request.instruction,
            start_url=request.start_url or "",
            task_id=task_id,
            event_handler=event_handler,
        )

    try:
        status, result = await loop.run_in_executor(None, _sync_run)
        state = _TASKS.get(task_id)
        if state:
            state.status = _normalize_status(status)
            state.result = result
            state.updated_at = time.time()
    except Exception as exc:
        state = _TASKS.get(task_id)
        if state:
            state.status = "error"
            state.error = str(exc)
            state.updated_at = time.time()
        if event_handler:
            event_handler({"type": "error", "task_id": task_id, "error": str(exc)})


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@app.post("/tasks/stream")
async def stream_task(
    request: TaskRequest,
    authorization: Optional[str] = Header(default=None),
) -> StreamingResponse:
    api_key = _extract_api_key(authorization)
    task_id = str(uuid.uuid4())
    _TASKS[task_id] = TaskState(task_id=task_id)

    queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
    loop = asyncio.get_running_loop()

    def emit(event: dict[str, Any]) -> None:
        loop.call_soon_threadsafe(queue.put_nowait, event)

    async def _driver() -> None:
        try:
            await _run_task_async(task_id, request, api_key, event_handler=emit)
        finally:
            loop.call_soon_threadsafe(queue.put_nowait, {"type": "_end", "task_id": task_id})

    asyncio.create_task(_driver())

    async def event_stream():  # type: ignore[return]
        while True:
            event = await queue.get()
            if event.get("type") == "_end":
                break
            yield f"data: {json.dumps(event)}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "X-Task-ID": task_id,
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


@app.post("/tasks")
async def start_task(
    request: TaskRequest,
    authorization: Optional[str] = Header(default=None),
) -> dict[str, str]:
    api_key = _extract_api_key(authorization)
    task_id = str(uuid.uuid4())
    _TASKS[task_id] = TaskState(task_id=task_id)
    asyncio.create_task(_run_task_async(task_id, request, api_key))
    return {"task_id": task_id, "status": "started"}


@app.get("/tasks/{task_id}")
async def get_task(task_id: str) -> dict[str, Any]:
    state = _TASKS.get(task_id)
    if not state:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
        "task_id": state.task_id,
        "status": state.status,
        "result": state.result,
        "error": state.error,
        "started_at": state.started_at,
        "updated_at": state.updated_at,
    }


@app.get("/health")
async def health() -> dict[str, Any]:
    active = sum(1 for s in _TASKS.values() if s.status == "running")
    return {"status": "ok", "active_tasks": active}


@app.get("/")
async def root() -> dict[str, Any]:
    return {
        "service": "Lightcone Agent",
        "version": "0.1.0",
        "endpoints": {
            "POST /tasks/stream": "Start task with SSE streaming",
            "POST /tasks": "Start task (fire-and-forget)",
            "GET /tasks/{id}": "Get task status",
            "GET /health": "Health check",
        },
    }
