"""CLI entry point — ``lightcone run`` and ``lightcone serve``."""

from __future__ import annotations

import argparse
import logging
import os

import uvicorn

from lightcone.agent import CUAAgent
from lightcone.config import get_settings


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lightcone", description="Lightcone Agent CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- run ---
    run_p = subparsers.add_parser("run", help="Run a task locally")
    run_p.add_argument(
        "--task", type=str,
        default=os.getenv("LIGHTCONE_TASK", "").strip(),
        help="Task instruction (default: LIGHTCONE_TASK env var)",
    )
    run_p.add_argument("--api-key", type=str, default="", help="API key (overrides TZAFON_API_KEY)")
    run_p.add_argument("--profile", type=str, default="", help="Prompt profile (browser, terminal, desktop, default)")
    run_p.add_argument("--start-url", type=str, default="", help="URL to open before the agent loop")
    run_p.add_argument("--model", type=str, default="", help="LLM model name or alias (8b, 32b, auto)")
    run_p.add_argument("--max-steps", type=int, default=None, help="Max steps before termination")
    run_p.add_argument("--max-history", type=int, default=None, help="Max history turns in context")
    run_p.add_argument("--temperature", type=float, default=None, help="LLM temperature (0-1)")
    run_p.add_argument("--max-tokens", type=int, default=None, help="LLM max tokens per response")
    run_p.add_argument("--width", type=int, default=1280, help="Viewport width (px)")
    run_p.add_argument("--height", type=int, default=720, help="Viewport height (px)")

    # --- serve ---
    serve_p = subparsers.add_parser("serve", help="Start the API server")
    serve_p.add_argument("--host", type=str, default="0.0.0.0", help="Bind host")
    serve_p.add_argument("--port", type=int, default=8000, help="Bind port")
    serve_p.add_argument("--reload", action="store_true", help="Auto-reload (dev only)")

    return parser


def _run_command(args: argparse.Namespace) -> int:
    settings = get_settings()
    task = (args.task or "").strip()
    if not task:
        raise SystemExit("Task is required (pass --task or set LIGHTCONE_TASK)")

    agent = CUAAgent(
        max_steps=args.max_steps,
        max_history_turns=args.max_history,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=settings.llm_top_p,
        model=(args.model or settings.llm_model).strip(),
        llm_timeout_s=settings.llm_timeout_s,
        max_retries=settings.llm_max_retries,
        retry_delay=settings.llm_retry_delay_s,
        viewport_width=args.width,
        viewport_height=args.height,
        api_key=args.api_key or None,
        prompt_profile=args.profile or None,
    )

    status, result = agent.run(task=task, start_url=(args.start_url or "").strip())
    log = logging.getLogger("lightcone.cli")
    log.info("Final status: %s", status)
    if result:
        log.info("Result: %s", result)
    return 0


def _serve_command(args: argparse.Namespace) -> int:
    uvicorn.run("lightcone.server:app", host=args.host, port=args.port, reload=args.reload)
    return 0


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    parser = _build_parser()
    args = parser.parse_args()
    if args.command == "run":
        return _run_command(args)
    if args.command == "serve":
        return _serve_command(args)
    parser.error(f"Unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
