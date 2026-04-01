# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .file_param import FileParam
from .message_param import MessageParam
from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
from .chat_completion_content_part_audio_param import ChatCompletionContentPartAudioParam
from .chat_completion_content_part_image_param import ChatCompletionContentPartImageParam
from .chat_completion_content_part_refusal_param import ChatCompletionContentPartRefusalParam
from .chat_completion_message_function_tool_call_param import ChatCompletionMessageFunctionToolCallParam

__all__ = [
    "ChatCreateCompletionParams",
    "Message",
    "MessageChatCompletionDeveloperMessageParam",
    "MessageChatCompletionSystemMessageParam",
    "MessageChatCompletionUserMessageParam",
    "MessageChatCompletionUserMessageParamContentUnionMember1",
    "MessageChatCompletionAssistantMessageParam",
    "MessageChatCompletionAssistantMessageParamAudio",
    "MessageChatCompletionAssistantMessageParamContentUnionMember1",
    "MessageChatCompletionAssistantMessageParamFunctionCall",
    "MessageChatCompletionAssistantMessageParamToolCall",
    "MessageChatCompletionAssistantMessageParamToolCallChatCompletionMessageCustomToolCallParam",
    "MessageChatCompletionAssistantMessageParamToolCallChatCompletionMessageCustomToolCallParamCustom",
    "MessageChatCompletionToolMessageParam",
    "MessageChatCompletionFunctionMessageParam",
    "MessageCustomChatCompletionMessageParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1",
    "MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioParamAudioURL",
    "MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartVideoParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartVideoParamVideoURL",
    "MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleImageParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartImageEmbedsParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioEmbedsParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleAudioParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleVideoParam",
    "MessageCustomChatCompletionMessageParamContentUnionMember1CustomThinkCompletionContentParam",
    "MessageCustomChatCompletionMessageParamTool",
    "MessageCustomChatCompletionMessageParamToolFunction",
    "LogitsProcessor",
    "LogitsProcessorLogitsProcessorConstructor",
    "ResponseFormat",
    "ResponseFormatResponseFormat",
    "ResponseFormatResponseFormatJsonSchema",
    "ResponseFormatStructuralTagResponseFormat",
    "ResponseFormatLegacyStructuralTagResponseFormat",
    "ResponseFormatLegacyStructuralTagResponseFormatStructure",
    "StreamOptions",
    "StructuredOutputs",
    "ToolChoice",
    "ToolChoiceChatCompletionNamedToolChoiceParam",
    "ToolChoiceChatCompletionNamedToolChoiceParamFunction",
    "Tool",
    "ToolFunction",
]


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    add_generation_prompt: bool
    """If true, the generation prompt will be added to the chat template.

    This is a parameter used by chat template in tokenizer config of the model.
    """

    add_special_tokens: bool
    """If true, special tokens (e.g.

    BOS) will be added to the prompt on top of what is added by the chat template.
    For most models, the chat template takes care of adding the special tokens so
    this should be set to false (as is the default).
    """

    allowed_token_ids: Optional[Iterable[int]]

    bad_words: SequenceNotStr[str]

    cache_salt: Optional[str]
    """
    If specified, the prefix cache will be salted with the provided string to
    prevent an attacker to guess prompts in multi-user environments. The salt should
    be random, protected from access by 3rd parties, and long enough to be
    unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).
    """

    chat_template: Optional[str]
    """A Jinja template to use for this conversion.

    As of transformers v4.44, default chat template is no longer allowed, so you
    must provide a chat template if the tokenizer does not define one.
    """

    chat_template_kwargs: Optional[Dict[str, object]]
    """Additional keyword args to pass to the template renderer.

    Will be accessible by the chat template.
    """

    continue_final_message: bool
    """
    If this is set, the chat will be formatted so that the final message in the chat
    is open-ended, without any EOS tokens. The model will continue this message
    rather than starting a new one. This allows you to "prefill" part of the model's
    response for it. Cannot be used at the same time as `add_generation_prompt`.
    """

    documents: Optional[Iterable[Dict[str, str]]]
    """
    A list of dicts representing documents that will be accessible to the model if
    it is performing RAG (retrieval-augmented generation). If the template does not
    support RAG, this argument will have no effect. We recommend that each document
    should be a dict containing "title" and "text" keys.
    """

    echo: bool
    """
    If true, the new message will be prepended with the last message if they belong
    to the same role.
    """

    frequency_penalty: Optional[float]

    ignore_eos: bool

    include_reasoning: bool

    include_stop_str_in_output: bool

    kv_transfer_params: Optional[Dict[str, object]]
    """KVTransfer parameters used for disaggregated serving."""

    length_penalty: float

    logit_bias: Optional[Dict[str, float]]

    logits_processors: Optional[SequenceNotStr[LogitsProcessor]]
    """
    A list of either qualified names of logits processors, or constructor objects,
    to apply when sampling. A constructor is a JSON object with a required
    'qualname' field specifying the qualified name of the processor class/factory,
    and optional 'args' and 'kwargs' fields containing positional and keyword
    arguments. For example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1,
    2], 'kwargs': {'param': 'value'}}.
    """

    logprobs: Optional[bool]

    max_completion_tokens: Optional[int]

    max_tokens: Optional[int]

    min_p: Optional[float]

    min_tokens: int

    mm_processor_kwargs: Optional[Dict[str, object]]
    """Additional kwargs to pass to the HF processor."""

    model: Optional[str]

    n: Optional[int]

    parallel_tool_calls: Optional[bool]

    presence_penalty: Optional[float]

    priority: int
    """The priority of the request (lower means earlier handling; default: 0).

    Any priority other than 0 will raise an error if the served model does not use
    priority scheduling.
    """

    prompt_logprobs: Optional[int]

    reasoning_effort: Optional[Literal["low", "medium", "high"]]

    repetition_penalty: Optional[float]

    request_id: str
    """The request_id related to this request.

    If the caller does not set it, a random_uuid will be generated. This id is used
    through out the inference process and return in response.
    """

    response_format: Optional[ResponseFormat]

    return_token_ids: Optional[bool]
    """If specified, the result will include token IDs alongside the generated text.

    In streaming mode, prompt_token_ids is included only in the first chunk, and
    token_ids contains the delta tokens for each chunk. This is useful for debugging
    or when you need to map generated text back to input tokens.
    """

    return_tokens_as_token_ids: Optional[bool]
    """
    If specified with 'logprobs', tokens are represented as strings of the form
    'token_id:{token_id}' so that tokens that are not JSON-encodable can be
    identified.
    """

    seed: Optional[int]

    skip_special_tokens: bool

    spaces_between_special_tokens: bool

    stop: Union[str, SequenceNotStr[str], None]

    stop_token_ids: Optional[Iterable[int]]

    stream: Optional[bool]

    stream_options: Optional[StreamOptions]

    structured_outputs: Optional[StructuredOutputs]
    """Additional kwargs for structured outputs"""

    temperature: Optional[float]

    tool_choice: Optional[ToolChoice]

    tools: Optional[Iterable[Tool]]

    top_k: Optional[int]

    top_logprobs: Optional[int]

    top_p: Optional[float]

    truncate_prompt_tokens: Optional[int]

    use_beam_search: bool

    user: Optional[str]

    vllm_xargs: Optional[Dict[str, Union[str, float, SequenceNotStr[Union[str, float]]]]]
    """
    Additional request parameters with (list of) string or numeric values, used by
    custom extensions.
    """


class MessageChatCompletionDeveloperMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Developer-provided instructions that the model should follow, regardless of
    messages sent by the user. With o1 models and newer, `developer` messages
    replace the previous `system` messages.
    """

    content: Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]

    role: Required[Literal["developer"]]

    name: str


class MessageChatCompletionSystemMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Developer-provided instructions that the model should follow, regardless of
    messages sent by the user. With o1 models and newer, use `developer` messages
    for this purpose instead.
    """

    content: Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]

    role: Required[Literal["system"]]

    name: str


MessageChatCompletionUserMessageParamContentUnionMember1: TypeAlias = Union[
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartAudioParam,
    FileParam,
]


class MessageChatCompletionUserMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Messages sent by an end user, containing prompts or additional context
    information.
    """

    content: Required[Union[str, Iterable[MessageChatCompletionUserMessageParamContentUnionMember1]]]

    role: Required[Literal["user"]]

    name: str


class MessageChatCompletionAssistantMessageParamAudio(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Data about a previous audio response from the model.
    [Learn more](https://platform.openai.com/docs/guides/audio).
    """

    id: Required[str]


MessageChatCompletionAssistantMessageParamContentUnionMember1: TypeAlias = Union[
    ChatCompletionContentPartTextParam, ChatCompletionContentPartRefusalParam
]


class MessageChatCompletionAssistantMessageParamFunctionCall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the model.
    """

    arguments: Required[str]

    name: Required[str]


class MessageChatCompletionAssistantMessageParamToolCallChatCompletionMessageCustomToolCallParamCustom(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """The custom tool that the model called."""

    input: Required[str]

    name: Required[str]


class MessageChatCompletionAssistantMessageParamToolCallChatCompletionMessageCustomToolCallParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A call to a custom tool created by the model."""

    id: Required[str]

    custom: Required[MessageChatCompletionAssistantMessageParamToolCallChatCompletionMessageCustomToolCallParamCustom]
    """The custom tool that the model called."""

    type: Required[Literal["custom"]]


MessageChatCompletionAssistantMessageParamToolCall: TypeAlias = Union[
    ChatCompletionMessageFunctionToolCallParam,
    MessageChatCompletionAssistantMessageParamToolCallChatCompletionMessageCustomToolCallParam,
]


class MessageChatCompletionAssistantMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Messages sent by the model in response to user messages."""

    role: Required[Literal["assistant"]]

    audio: Optional[MessageChatCompletionAssistantMessageParamAudio]
    """
    Data about a previous audio response from the model.
    [Learn more](https://platform.openai.com/docs/guides/audio).
    """

    content: Union[str, Iterable[MessageChatCompletionAssistantMessageParamContentUnionMember1], None]

    function_call: Optional[MessageChatCompletionAssistantMessageParamFunctionCall]
    """Deprecated and replaced by `tool_calls`.

    The name and arguments of a function that should be called, as generated by the
    model.
    """

    name: str

    refusal: Optional[str]

    tool_calls: Iterable[MessageChatCompletionAssistantMessageParamToolCall]


class MessageChatCompletionToolMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    content: Required[Union[str, Iterable[ChatCompletionContentPartTextParam]]]

    role: Required[Literal["tool"]]

    tool_call_id: Required[str]


class MessageChatCompletionFunctionMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    content: Required[Optional[str]]

    name: Required[str]

    role: Required[Literal["function"]]


class MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioParamAudioURL(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    url: Required[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    audio_url: Required[
        MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioParamAudioURL
    ]

    type: Required[Literal["audio_url"]]


class MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartVideoParamVideoURL(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    url: Required[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartVideoParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    type: Required[Literal["video_url"]]

    video_url: Required[
        MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartVideoParamVideoURL
    ]


class MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleImageParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """
    A simpler version of the param that only accepts a plain image_url.
    This is supported by OpenAI API, although it is not documented.

    Example:
    {
        "image_url": "https://example.com/image.jpg"
    }
    """

    image_url: Optional[str]

    uuid: Optional[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartImageEmbedsParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    type: Required[Literal["image_embeds"]]

    image_embeds: Union[str, Dict[str, str], None]

    uuid: Optional[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioEmbedsParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    type: Required[Literal["audio_embeds"]]

    audio_embeds: Union[str, Dict[str, str], None]

    uuid: Optional[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleAudioParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A simpler version of the param that only accepts a plain audio_url.

    Example:
    {
        "audio_url": "https://example.com/audio.mp3"
    }
    """

    audio_url: Optional[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleVideoParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A simpler version of the param that only accepts a plain audio_url.

    Example:
    {
        "video_url": "https://example.com/video.mp4"
    }
    """

    uuid: Optional[str]

    video_url: Optional[str]


class MessageCustomChatCompletionMessageParamContentUnionMember1CustomThinkCompletionContentParam(  # type: ignore[call-arg]
    TypedDict, total=False, extra_items=object
):
    """A Think Completion Content Param that accepts a plain text and a boolean.

    Example:
    {
        "thinking": "I am thinking about the answer",
        "closed": True,
        "type": "thinking"
    }
    """

    thinking: Required[str]

    type: Required[Literal["thinking"]]

    closed: bool


MessageCustomChatCompletionMessageParamContentUnionMember1: TypeAlias = Union[
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartAudioParam,
    FileParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartVideoParam,
    ChatCompletionContentPartRefusalParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleImageParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartImageEmbedsParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1ChatCompletionContentPartAudioEmbedsParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleAudioParam,
    MessageCustomChatCompletionMessageParamContentUnionMember1CustomChatCompletionContentSimpleVideoParam,
    str,
    MessageCustomChatCompletionMessageParamContentUnionMember1CustomThinkCompletionContentParam,
]


class MessageCustomChatCompletionMessageParamToolFunction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    name: Required[str]

    description: str

    parameters: Dict[str, object]

    strict: Optional[bool]


class MessageCustomChatCompletionMessageParamTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """A function tool that can be used to generate a response."""

    function: Required[MessageCustomChatCompletionMessageParamToolFunction]

    type: Required[Literal["function"]]


class MessageCustomChatCompletionMessageParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Enables custom roles in the Chat Completion API."""

    role: Required[str]

    content: Union[str, SequenceNotStr[MessageCustomChatCompletionMessageParamContentUnionMember1]]

    name: str

    reasoning: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[ChatCompletionMessageFunctionToolCallParam]]

    tools: Optional[Iterable[MessageCustomChatCompletionMessageParamTool]]


Message: TypeAlias = Union[
    MessageChatCompletionDeveloperMessageParam,
    MessageChatCompletionSystemMessageParam,
    MessageChatCompletionUserMessageParam,
    MessageChatCompletionAssistantMessageParam,
    MessageChatCompletionToolMessageParam,
    MessageChatCompletionFunctionMessageParam,
    MessageCustomChatCompletionMessageParam,
    MessageParam,
]


class LogitsProcessorLogitsProcessorConstructor(TypedDict, total=False):
    qualname: Required[str]

    args: Optional[Iterable[object]]

    kwargs: Optional[Dict[str, object]]


LogitsProcessor: TypeAlias = Union[str, LogitsProcessorLogitsProcessorConstructor]


class ResponseFormatResponseFormatJsonSchema(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    name: Required[str]

    description: Optional[str]

    schema: Optional[Dict[str, object]]

    strict: Optional[bool]


class ResponseFormatResponseFormat(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    type: Required[Literal["text", "json_object", "json_schema"]]

    json_schema: Optional[ResponseFormatResponseFormatJsonSchema]


class ResponseFormatStructuralTagResponseFormat(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    format: Required[object]

    type: Required[Literal["structural_tag"]]


class ResponseFormatLegacyStructuralTagResponseFormatStructure(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    begin: Required[str]

    end: Required[str]

    schema: Optional[Dict[str, object]]


class ResponseFormatLegacyStructuralTagResponseFormat(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    structures: Required[Iterable[ResponseFormatLegacyStructuralTagResponseFormatStructure]]

    triggers: Required[SequenceNotStr[str]]

    type: Required[Literal["structural_tag"]]


ResponseFormat: TypeAlias = Union[
    ResponseFormatResponseFormat,
    ResponseFormatStructuralTagResponseFormat,
    ResponseFormatLegacyStructuralTagResponseFormat,
]


class StreamOptions(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    continuous_usage_stats: Optional[bool]

    include_usage: Optional[bool]


class StructuredOutputs(TypedDict, total=False):
    """Additional kwargs for structured outputs"""

    _backend: Optional[str]

    _backend_was_auto: bool

    choice: Optional[SequenceNotStr[str]]

    disable_additional_properties: bool

    disable_any_whitespace: bool

    disable_fallback: bool

    grammar: Optional[str]

    json: Union[str, Dict[str, object], None]

    json_object: Optional[bool]

    regex: Optional[str]

    structural_tag: Optional[str]

    whitespace_pattern: Optional[str]


class ToolChoiceChatCompletionNamedToolChoiceParamFunction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    name: Required[str]


class ToolChoiceChatCompletionNamedToolChoiceParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    function: Required[ToolChoiceChatCompletionNamedToolChoiceParamFunction]

    type: Literal["function"]


ToolChoice: TypeAlias = Union[Literal["none", "auto", "required"], ToolChoiceChatCompletionNamedToolChoiceParam]


class ToolFunction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    name: Required[str]

    description: Optional[str]

    parameters: Optional[Dict[str, object]]


class Tool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    function: Required[ToolFunction]

    type: Literal["function"]
