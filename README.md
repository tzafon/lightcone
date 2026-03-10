<div align="center">

# Lightcone

### SDKs and examples for Tzafon's computer-use agents

<img src="northstar.svg" alt="Northstar" width="160">

Featuring **Northstar CUA Fast** — a 4B model trained with reinforcement learning

[API Docs](https://docs.tzafon.ai/api-reference/introduction) | [Pricing](https://docs.tzafon.ai/pricing) | [X (Twitter)](https://x.com/tzafon_company)

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![PyPI - tzafon](https://img.shields.io/pypi/v/tzafon?label=tzafon&color=blue)](https://pypi.org/project/tzafon/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)

</div>

---

Northstar CUA Fast recovers from mistakes, generalizes across environments, and outperforms open-source models at twice its size. Built for agentic loops where every step is a model call.

| | |
|---|---|
| **Parameters** | 4B |
| **Context** | 64K |
| **Training** | GUI reinforcement learning |
| **Input** | Text + screenshot |
| **Output** | GUI actions — `click`, `type`, `scroll`, `key`, `drag`, ... |
| **Coordinates** | 0–999 normalized (model) · pixel-scaled (Responses API) |
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

---

## CUA Loop

The Responses API handles context, parsing, and coordinate scaling — your agent loop is just screenshot, think, act, repeat:

```python
import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {"type": "computer_use", "display_width": 1280, "display_height": 720, "environment": "browser"}
TASK = "Go to wikipedia.org and search for 'Alan Turing'"

with client.computer.create(kind="browser") as computer:
    screenshot_url = computer.get_screenshot_url(computer.screenshot())

    response = client.responses.create(
        model="tzafon.northstar-cua-fast",
        tools=[TOOL],
        input=[{"role": "user", "content": [
            {"type": "input_text", "text": TASK},
            {"type": "input_image", "image_url": screenshot_url},
        ]}],
    )

    while True:
        computer_call = next(
            (o for o in (response.output or []) if o.type == "computer_call"), None
        )
        if not computer_call:
            break

        action = computer_call.action
        if action.type == "click":
            computer.click(action.x, action.y)
        elif action.type == "type":
            computer.type(action.text)
        elif action.type in ("key", "keypress"):
            computer.hotkey(action.keys)
        elif action.type == "scroll":
            computer.scroll(dx=action.scroll_x or 0, dy=action.scroll_y or 0)
        elif action.type == "navigate":
            computer.navigate(action.url)
        elif action.type in ("terminate", "done", "answer"):
            break
        # ... see examples/ for full action handling

        computer.wait(1)
        screenshot_url = computer.get_screenshot_url(computer.screenshot())
        response = client.responses.create(
            model="tzafon.northstar-cua-fast",
            previous_response_id=response.id,
            tools=[TOOL],
            input=[{
                "type": "computer_call_output",
                "call_id": computer_call.call_id,
                "output": {"type": "input_image", "image_url": screenshot_url},
            }],
        )
```

---

## Examples

| Example | Description |
|---|---|
| [`simple.py`](examples/simple.py) | Basic CUA loop — the minimal agent |
| [`persistent_session.py`](examples/persistent_session.py) | Persistent browser sessions for authenticated workflows |
| [`streaming.py`](examples/streaming.py) | FastAPI SSE endpoint wrapping the CUA loop |
| [`interactive.py`](examples/interactive.py) | Human-in-the-loop — pauses for CAPTCHAs, 2FA, ambiguity |
| [`shell.py`](examples/shell.py) | Desktop session mixing browser + shell commands |
| [`multi_tab.py`](examples/multi_tab.py) | Multi-tab comparison across sites |
| [`monitor.py`](examples/monitor.py) | Screenshot-only observer for dashboard monitoring |

```bash
# Run the simple example
export TZAFON_API_KEY="your-api-key"
python examples/simple.py

# Run the streaming server
pip install 'lightcone[streaming]'
uvicorn examples.streaming:app
curl -N -X POST http://localhost:8000/tasks/stream \
  -H "Content-Type: application/json" \
  -d '{"instruction": "Go to wikipedia.org and search for Alan Turing"}'
```

---

## Supported Actions

`click` · `double_click` · `triple_click` · `right_click` · `drag` · `type` · `key` · `scroll` · `hscroll` · `navigate` (browser only) · `wait` · `terminate`

Via the **Responses API** (`/v1/responses`), coordinates are scaled to viewport pixels and responses are structured — no parsing required. Multi-turn conversations are managed server-side via `previous_response_id`.

---

## SDKs

| SDK | Install | Source |
|---|---|---|
| Python | `pip install tzafon` | [`sdks/python`](sdks/python) |
| TypeScript | `npm install @tzafon/lightcone` | [`sdks/typescript`](sdks/typescript) |

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

> At 4B parameters, Northstar CUA Fast is competitive with open-source models at twice its size on single-app tasks. See our [research blog](https://www.tzafon.ai/blog/training-vlm-for-cua) for training details.

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
