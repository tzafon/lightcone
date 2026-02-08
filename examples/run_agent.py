"""Minimal programmatic usage example."""

from lightcone.agent import CUAAgent


def main() -> None:
    agent = CUAAgent()
    status, result = agent.run(task="Open Firefox and navigate to https://example.com")
    print(f"Status: {status}")
    if result:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
