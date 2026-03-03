"""Model alias resolution and provider catalog."""

from __future__ import annotations

import logging
import os
from functools import lru_cache
from typing import Iterable, Optional

import requests

logger = logging.getLogger("lightcone.models")

# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------

DEFAULT_MODEL_ALIAS = "4b"

MODEL_ALIASES: dict[str, str] = {
    "4": "tzafon.northstar-cua-fast",
    "4b": "tzafon.northstar-cua-fast",
    "fast": "tzafon.northstar-cua-fast",
}

OPENAI_COMPATIBLE_BASE_URLS: dict[str, str] = {
    "tzafon": "https://api.tzafon.ai/v1",
    "openai": "https://api.openai.com/v1",
}

# ---------------------------------------------------------------------------
# Resolution helpers
# ---------------------------------------------------------------------------


@lru_cache(maxsize=4)
def _fetch_models(base_url: str, api_key: str) -> list[str]:
    url = base_url.rstrip("/") + "/models"
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=15,
    )
    response.raise_for_status()
    payload = response.json()
    data = payload.get("data", []) if isinstance(payload, dict) else []
    model_ids: list[str] = []
    for entry in data:
        if isinstance(entry, dict):
            model_id = entry.get("id")
            if isinstance(model_id, str) and model_id:
                model_ids.append(model_id)
    return model_ids


def _pick_default(models: Iterable[str]) -> Optional[str]:
    models = list(models)
    if not models:
        return None
    for needle in ("cua", "agent", "vision"):
        for model in models:
            if needle in model.lower():
                return model
    return models[0]


def _resolve_base_url(base_url: str | None) -> str:
    if not base_url:
        return OPENAI_COMPATIBLE_BASE_URLS["tzafon"]
    key = base_url.strip().lower()
    return OPENAI_COMPATIBLE_BASE_URLS.get(key, base_url)


def resolve_model(
    value: str | None,
    *,
    api_key: str | None = None,
    base_url: str | None = None,
) -> str:
    """Resolve a model alias, full ID, or ``'auto'`` to a concrete model ID."""
    raw = (value or "").strip()
    if not raw:
        raw = DEFAULT_MODEL_ALIAS

    if raw.lower() != "auto":
        alias_key = raw.strip().lower()
        return MODEL_ALIASES.get(alias_key, raw)

    api_key = api_key or os.getenv("TZAFON_API_KEY")
    base_url = _resolve_base_url(base_url or os.getenv("LIGHTCONE_LLM_BASE_URL"))
    if not api_key:
        raise RuntimeError("TZAFON_API_KEY is required to auto-select a model")

    try:
        models = _fetch_models(base_url, api_key)
    except Exception as exc:
        raise RuntimeError(
            "Failed to fetch available models from the API. "
            "Set LIGHTCONE_LLM_MODEL explicitly."
        ) from exc

    chosen = _pick_default(models)
    if not chosen:
        raise RuntimeError("No models returned from API. Set LIGHTCONE_LLM_MODEL explicitly.")
    return chosen


def list_models() -> dict[str, str]:
    """Return a copy of the model alias catalog."""
    return dict(MODEL_ALIASES)
