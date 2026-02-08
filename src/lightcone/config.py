"""Configuration via environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Callable, TypeVar

from dotenv import find_dotenv, load_dotenv

T = TypeVar("T")

_DOTENV_PATH = find_dotenv(usecwd=True)
if _DOTENV_PATH:
    load_dotenv(_DOTENV_PATH)


def _get_env(name: str, default: T, cast: Callable[[str], T] | None = None) -> T:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    if cast is None:
        return value  # type: ignore[return-value]
    try:
        return cast(value)
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    api_key: str | None
    llm_base_url: str
    computer_base_url: str
    llm_model: str
    llm_max_tokens: int
    llm_timeout_s: float
    llm_max_retries: int
    llm_retry_delay_s: float
    llm_temperature: float
    llm_top_p: float
    max_steps: int
    max_history_turns: int
    prompt_profile: str


@lru_cache
def get_settings() -> Settings:
    raw_model = os.getenv("LIGHTCONE_LLM_MODEL") or os.getenv("LIGHTCONE_MODEL") or ""
    return Settings(
        api_key=os.getenv("LIGHTCONE_API_KEY"),
        llm_base_url=_get_env("LIGHTCONE_LLM_BASE_URL", "https://api.tzafon.ai/v1"),
        computer_base_url=_get_env("LIGHTCONE_COMPUTER_BASE_URL", "https://api.tzafon.ai"),
        llm_model=raw_model or "auto",
        llm_max_tokens=_get_env("LIGHTCONE_LLM_MAX_TOKENS", 512, int),
        llm_timeout_s=_get_env("LIGHTCONE_LLM_TIMEOUT_S", 60.0, float),
        llm_max_retries=_get_env("LIGHTCONE_LLM_MAX_RETRIES", 3, int),
        llm_retry_delay_s=_get_env("LIGHTCONE_LLM_RETRY_DELAY_S", 2.0, float),
        llm_temperature=_get_env("LIGHTCONE_LLM_TEMPERATURE", 0.3, float),
        llm_top_p=_get_env("LIGHTCONE_LLM_TOP_P", 0.95, float),
        max_steps=_get_env("LIGHTCONE_MAX_STEPS", 150, int),
        max_history_turns=_get_env("LIGHTCONE_MAX_HISTORY_TURNS", 4, int),
        prompt_profile=_get_env("LIGHTCONE_PROMPT_PROFILE", "default"),
    )
