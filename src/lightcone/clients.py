"""Factory functions for LLM and Computer clients."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from openai import OpenAI
from tzafon import Computer

from lightcone.config import Settings, get_settings


@dataclass(frozen=True)
class AgentClients:
    llm: OpenAI
    computer: Computer


def resolve_api_key(api_key: Optional[str] = None, settings: Optional[Settings] = None) -> str:
    resolved_settings = settings or get_settings()
    resolved = api_key or resolved_settings.api_key or os.environ.get("TZAFON_API_KEY")
    if not resolved:
        raise RuntimeError("TZAFON_API_KEY is not set")
    return resolved


def build_llm_client(api_key: str, settings: Optional[Settings] = None) -> OpenAI:
    resolved_settings = settings or get_settings()
    return OpenAI(
        api_key=api_key,
        base_url=resolved_settings.llm_base_url,
        timeout=resolved_settings.llm_timeout_s,
    )


def build_computer_client(api_key: str, settings: Optional[Settings] = None) -> Computer:
    resolved_settings = settings or get_settings()
    return Computer(api_key=api_key, base_url=resolved_settings.computer_base_url)


def build_clients(api_key: Optional[str] = None, settings: Optional[Settings] = None) -> AgentClients:
    resolved_settings = settings or get_settings()
    resolved_api_key = resolve_api_key(api_key, resolved_settings)
    return AgentClients(
        llm=build_llm_client(resolved_api_key, resolved_settings),
        computer=build_computer_client(resolved_api_key, resolved_settings),
    )
