# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionContentPartAudioParam", "InputAudio"]


class InputAudio(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    data: Required[str]

    format: Required[Literal["wav", "mp3"]]


class ChatCompletionContentPartAudioParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Learn about [audio inputs](https://platform.openai.com/docs/guides/audio)."""

    input_audio: Required[InputAudio]

    type: Required[Literal["input_audio"]]
