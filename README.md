<div align="center">

# Lightcone

### The API for Northstar, a vision-language model by Tzafon

<img src="northstar.svg" alt="Northstar" width="160">

**Northstar CUA Fast** — 4B parameters, trained with GUI reinforcement learning

[Docs](https://docs.lightcone.ai) | [API Reference](https://docs.lightcone.ai/api) | [Pricing](https://docs.tzafon.ai/pricing) | [X (Twitter)](https://x.com/tzafon_company)

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![PyPI - tzafon](https://img.shields.io/pypi/v/tzafon?label=tzafon&color=blue)](https://pypi.org/project/tzafon/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)

</div>

---

Northstar sees screens and acts on them. Give it a screenshot, it decides where to click, what to type, when to scroll. Give it a task in plain language, it operates a computer from start to finish — opening apps, navigating between pages, filling forms, reading results.

It recovers from mistakes, generalizes across desktop environments, and outperforms open-source models at twice its size. Built for computer-use loops where every step is a model call.

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

### Give Northstar a task

```python
import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

for event in client.agent.tasks.start_stream(
    instruction="Go to wikipedia.org, search for 'Alan Turing', and tell me the first sentence",
    kind="desktop",
):
    print(event)
```

Northstar spins up a computer, opens a browser, searches Wikipedia, reads the article, and reports back. You just described what you wanted.

---

## CUA Loop

For full control, build the loop yourself. Northstar looks at a screenshot, decides the next action, you execute it, feed back the result:

```python
import os
from tzafon import Lightcone

client = Lightcone(api_key=os.environ["TZAFON_API_KEY"])

TOOL = {"type": "computer_use", "display_width": 1280, "display_height": 720, "environment": "desktop"}
TASK = "Open the terminal, run 'uname -a', then run 'df -h' and report the results"

with client.computer.create(kind="desktop") as computer:
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

## Try it

Run Northstar against a live enterprise app (OrangeHRM) and see every step:

```bash
export TZAFON_API_KEY="your-api-key"
uv run python -m examples.harness.evaluate
```

With annotated screenshots saved to a directory:

```bash
uv run --with Pillow --with httpx python -m examples.harness.evaluate --screenshots steps/
```

Reliability check (3 runs):

```bash
uv run python -m examples.harness.evaluate --runs 3
```

Custom target:

```bash
uv run python -m examples.harness.evaluate \
  --url "https://any-web-app.com/login" \
  --instruction "Log in with user/pass, then do something"
```

---

## Examples

| Example | Description |
|---|---|
| [`desktop.py`](examples/desktop.py) | Northstar operates a desktop — opens terminal, runs commands, reads output |
| [`simple.py`](examples/simple.py) | Minimal browser CUA loop |
| [`shell.py`](examples/shell.py) | Mixes Northstar with direct shell commands |
| [`competitor_research.py`](examples/competitor_research.py) | Two-phase: Northstar explores, then extracts structured data |
| [`persistent_session.py`](examples/persistent_session.py) | Persistent state for authenticated workflows |
| [`streaming.py`](examples/streaming.py) | FastAPI SSE endpoint wrapping the CUA loop |
| [`interactive.py`](examples/interactive.py) | Human-in-the-loop — pauses for CAPTCHAs, 2FA, ambiguity |
| [`multi_tab.py`](examples/multi_tab.py) | Multi-tab comparison across sites |
| [`visualize.py`](examples/visualize.py) | Save annotated screenshots showing every decision Northstar makes |
| [`monitor.py`](examples/monitor.py) | Screenshot-only observer for monitoring |

```bash
export TZAFON_API_KEY="your-api-key"
python examples/desktop.py
```

---

## Supported Actions

`click` · `double_click` · `triple_click` · `right_click` · `drag` · `type` · `key` · `scroll` · `hscroll` · `navigate` (browser mode) · `wait` · `terminate`

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
