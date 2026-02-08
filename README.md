<div align="center">

# Northstar CUA Fast

### Fast, Lightweight Computer-Use Intelligence

[API Docs](https://docs.tzafon.ai/api-reference/introduction) | [Discord](https://discord.gg/tzafon) | [X (Twitter)](https://x.com/tzafon_company)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

---

## 1. Model Introduction

Northstar CUA Fast is a 4B-parameter computer-use agent model developed by Tzafon. It is purpose-built for GUI automation — interpreting screenshots, reasoning about UI state, and producing structured actions (clicks, typing, scrolling) to operate a desktop autonomously.

Despite its small size, Northstar CUA Fast is optimised for real-time agentic loops where latency matters: each step requires a full model call, so a faster model directly translates to a faster agent.

### Key Features

- **4B parameters** — small enough to run on a single GPU, fast enough for real-time desktop automation.
- **Structured tool calling** — outputs normalised actions in a 0-999 coordinate grid, scaled to any viewport.
- **Built for agentic loops** — designed for the screenshot-think-act cycle, not just single-turn QA.

## 2. Model Summary

| | |
|---|---|
| **Architecture** | Dense Transformer |
| **Parameters** | 4B |
| **Context Length** | 64K |
| **Input** | Text + Image (screenshot) |
| **Output** | Structured tool calls (JSON) |
| **Coordinate System** | Normalised 0-999 grid |
| **Training Data** | Desktop GUI interaction traces |
| **License** | MIT |

## 3. Evaluation Results

### OSWorld Benchmark

Evaluated on [OSWorld](https://os-world.github.io/) — 369 real-world computer tasks across desktop applications, web browsing, file management, and terminal operations.

#### Per-Domain Breakdown

| Domain | UI-TARS 2 | Qwen3 Flash | Northstar CUA Fast (4B) |
|---|---|---|---|
| **Overall** | **53.1%** | 41.6% | 37.01% |
| Chrome | 62.96% | 56.43% | 55.30% |
| Thunderbird | 73.33% | 66.67% | 62.40% |
| LibreOffice Writer | 60.87% | 56.52% | 56.94% |
| OS | 41.67% | 54.17% | 46.26% |
| VLC | 49.94% | 34.41% | 43.87% |
| VS Code | 73.91% | 69.57% | 43.82% |
| GIMP | 50.00% | 42.31% | 41.58% |
| LibreOffice Impress | 56.38% | 50.98% | 37.50% |
| LibreOffice Calc | 65.96% | 23.04% | 30.64% |
| Multi-Apps | 34.13% | 22.01% | 15.55% |

## 4. Quickstart

### API Access

Northstar CUA Fast is available via the [Tzafon API](https://docs.tzafon.ai/api-reference/introduction), which is OpenAI-compatible:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.tzafon.ai/v1",
)

response = client.chat.completions.create(
    model="tzafon.northstar-cua-fast",
    messages=[
        {"role": "system", "content": "You are a desktop automation agent."},
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}},
            {"type": "text", "text": "Click on the Firefox icon."},
        ]},
    ],
    temperature=0.3,
    max_tokens=512,
)
print(response.choices[0].message.content)
```

## 5. Agent Harness

This repository includes **Lightcone**, an agent harness that wraps Northstar CUA Fast into a full desktop automation loop: screenshot, think, act, repeat.

### Install

```bash
# Requires Python 3.12+ and a Rust toolchain
git clone https://github.com/tzafon/lightcone.git
cd lightcone
uv venv && uv sync --extra dev
uv run maturin develop -m native/Cargo.toml
```

### Run a Task

```bash
export LIGHTCONE_API_KEY="your-api-key"

# CLI
lightcone run --task "Open Firefox and search for 'hello world'"

# Python
from lightcone.agent import CUAAgent

agent = CUAAgent(prompt_profile="browser")
status, result = agent.run(task="Navigate to https://example.com")
```

### Start the Server

```bash
lightcone serve --port 8000

# SSE streaming
curl -N -X POST http://localhost:8000/tasks/stream \
  -H "Authorization: Bearer $LIGHTCONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"instruction": "Open Firefox"}'
```

### Architecture

```
screenshot → Northstar CUA Fast → parse action → execute on computer → repeat
```

- **Pure-async FastAPI** server with SSE streaming.
- **Sliding-window context management** — automatically shrinks history on context-length errors.
- **Rust-accelerated image processing** — screenshot decode, resize, and encode in a single GIL-free call.
- **Auto-discovering tool registry** — add new tools by dropping a file.

## 6. Configuration

All settings are loaded from environment variables (prefixed `LIGHTCONE_`):

| Variable | Default | Description |
|---|---|---|
| `LIGHTCONE_API_KEY` | — | API key (required) |
| `LIGHTCONE_LLM_MODEL` | `auto` | Model name or alias |
| `LIGHTCONE_LLM_BASE_URL` | `https://api.tzafon.ai/v1` | LLM endpoint |
| `LIGHTCONE_MAX_STEPS` | `150` | Max agent steps per task |
| `LIGHTCONE_MAX_HISTORY_TURNS` | `4` | Sliding window size |
| `LIGHTCONE_PROMPT_PROFILE` | `default` | Prompt profile (`default`, `browser`, `terminal`, `desktop`) |

## 7. License

The code in this repository is released under the [MIT License](LICENSE).

Model weights are available exclusively via the [Tzafon API](https://docs.tzafon.ai/api-reference/introduction).

## 8. Citation

```bibtex
@misc{tzafon2026northstarcuafast,
    title={Northstar CUA Fast: Lightweight Computer-Use Agent Model},
    author={Tzafon Team},
    year={2026},
    url={https://github.com/tzafon/lightcone},
}
```

## 9. Contact

Questions or feedback? Reach out at **support@tzafon.ai** or open an issue.
