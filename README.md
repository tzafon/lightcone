<div align="center">

# Northstar CUA Fast

### 4B computer-use model trained with reinforcement learning

[API Docs](https://docs.tzafon.ai/api-reference/introduction) | [Pricing](https://docs.tzafon.ai/pricing) | [Discord](https://discord.gg/tzafon) | [X (Twitter)](https://x.com/tzafon_company)

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![PyPI - tzafon](https://img.shields.io/pypi/v/tzafon?label=tzafon&color=blue)](https://pypi.org/project/tzafon/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)

</div>

---

<!-- TODO: Add demo GIF here -->
<!-- ![Demo](assets/demo.gif) -->

## Why Northstar CUA Fast

A 4B computer-use model trained with GUI reinforcement learning. Recovers from mistakes, generalizes across environments, and outperforms open-source models at twice its size. Built for agentic loops where every step is a model call. < $1/M tokens.

| | |
|---|---|
| **Parameters** | 4B |
| **Context** | 64K |
| **Training** | GUI reinforcement learning |
| **Input** | Text + screenshot |
| **Output** | GUI actions — `click`, `type`, `scroll`, `key`, `drag`, ... |
| **Coordinates** | Normalized 0–999 grid, scaled to viewport pixels |
| **Pricing** | < $1/M tokens ([details](https://docs.tzafon.ai/pricing)) |

---

## Quickstart

### Install

```bash
pip install tzafon
```

### Make your first call

```python
import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

response = client.responses.create(
    model="tzafon.northstar-cua-fast",
    instructions="Click on the Firefox icon.",
    tools=[{
        "type": "computer_use",
        "display_width": 1024,
        "display_height": 768,
        "environment": "browser",
    }],
)
print(response.output)
```

Response:

```json
{
  "id": "resp_abc123",
  "status": "completed",
  "output": [
    {
      "type": "computer_call",
      "call_id": "call_xyz",
      "action": {
        "type": "click",
        "x": 512,
        "y": 384
      }
    }
  ],
  "usage": {
    "input_tokens": 1024,
    "output_tokens": 48,
    "total_tokens": 1072
  }
}
```

### OpenAI-compatible Chat Completions

For direct model access with any OpenAI SDK:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://api.tzafon.ai/v1",
)

response = client.chat.completions.create(
    model="tzafon.northstar-cua-fast",
    messages=[
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": "data:image/png;base64,..."}},
            {"type": "text", "text": "Click on the Firefox icon."},
        ]},
    ],
    temperature=0,
    max_tokens=512,
)
print(response.choices[0].message.content)
```

### cURL

```bash
curl -X POST https://api.tzafon.ai/v1/responses \
  -H "Authorization: Bearer $TZAFON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tzafon.northstar-cua-fast",
    "instructions": "Click on the Firefox icon.",
    "tools": [{"type": "computer_use", "display_width": 1024, "display_height": 768}]
  }'
```

> **[Try it in the Playground](https://docs.tzafon.ai/api-reference/introduction)** — no setup required.

---

## Supported Actions

`click` · `double_click` · `triple_click` · `right_click` · `drag` · `type` · `key` · `scroll` · `hscroll` · `navigate` (browser only) · `wait` · `terminate`

All coordinates use a **0–999 normalized grid** and are scaled to viewport pixels by the API (default 1024×768). Multi-turn conversations are supported via `previous_response_id`.

---

## OSWorld Benchmark (pass@1)

Evaluated on [OSWorld](https://os-world.github.io/) — 369 real-world desktop tasks.

| Domain | UI-TARS 2 | Qwen3 Flash | **Northstar CUA Fast (4B)** |
|---|---|---|---|
| Chrome | 62.96% | 56.43% | **55.30%** |
| Thunderbird | 73.33% | 66.67% | **62.40%** |
| LibreOffice Writer | 60.87% | 56.52% | **56.94%** |
| OS | 41.67% | 54.17% | **46.26%** |
| VLC | 49.94% | 34.41% | **43.87%** |
| **Overall** | **53.1%** | 41.6% | 37.01% |

> Northstar CUA Fast closes the gap on single-app tasks (Chrome, Thunderbird, Writer, VLC) at **~$0.002/step** — roughly 10x cheaper than frontier computer-use models.

---

## Agent Harness

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
export TZAFON_API_KEY="your-api-key"

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
  -H "Authorization: Bearer $TZAFON_API_KEY" \
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

---

## Configuration

All settings are loaded from environment variables:

| Variable | Default | Description |
|---|---|---|
| `TZAFON_API_KEY` | — | API key (required) |
| `LIGHTCONE_LLM_MODEL` | `auto` | Model name or alias |
| `LIGHTCONE_LLM_BASE_URL` | `https://api.tzafon.ai/v1` | LLM endpoint |
| `LIGHTCONE_MAX_STEPS` | `150` | Max agent steps per task |
| `LIGHTCONE_MAX_HISTORY_TURNS` | `4` | Sliding window size |
| `LIGHTCONE_PROMPT_PROFILE` | `default` | Prompt profile (`default`, `browser`, `terminal`, `desktop`) |

---

## What's Open Source vs Hosted

| Component | License | Status |
|---|---|---|
| Lightcone agent harness | Apache 2.0 | This repo |
| Python SDK (`tzafon`) | MIT | [PyPI](https://pypi.org/project/tzafon/) |
| Model weights | — | [Tzafon API](https://docs.tzafon.ai/api-reference/introduction) |

---

## License

The code in this repository is released under the [Apache License 2.0](LICENSE).

## Citation

```bibtex
@misc{tzafon2026northstarcuafast,
    title={Northstar CUA Fast: Lightweight Computer-Use Agent Model},
    author={Tzafon Team},
    year={2026},
    url={https://github.com/tzafon/lightcone},
}
```

## Contact

Questions or feedback? Reach out at **support@tzafon.ai** or open an issue.
