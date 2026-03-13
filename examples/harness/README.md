# Harness Examples

Packages tepeated CUA loop from examples into a small reusable runner.

Files:

- `runner.py`: `CuaRunner`, config/result types, action hooks, and JSONL traces
- `simple.py`: minimal browser-task example using the harness
- `interactive.py`: human-in-the-loop example using `before_action`

Run from the repo root:

```bash
export TZAFON_API_KEY=your-api-key
python -m examples.harness.simple
python -m examples.harness.interactive
```

Each run writes a trace under `runs/` with one JSON object per event. The trace
is intended for replay, debugging, or basic eval tooling later.
