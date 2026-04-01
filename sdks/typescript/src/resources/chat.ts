// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import * as ChatAPI from './chat';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class Chat extends APIResource {
  /**
   * Create Chat Completion
   */
  createCompletion(body: ChatCreateCompletionParams, options?: RequestOptions): APIPromise<unknown> {
    return this._client.post('/v1/chat/completions', { body, ...options });
  }
}

/**
 * Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).
 */
export interface ChatCompletionContentPartAudio {
  input_audio: ChatCompletionContentPartAudio.InputAudio;

  type: 'input_audio';

  [k: string]: unknown;
}

export namespace ChatCompletionContentPartAudio {
  export interface InputAudio {
    data: string;

    format: 'wav' | 'mp3';

    [k: string]: unknown;
  }
}

/**
 * Learn about [image inputs](https://platform.openai.com/docs/guides/vision).
 */
export interface ChatCompletionContentPartImage {
  image_url: ChatCompletionContentPartImage.ImageURL;

  type: 'image_url';

  [k: string]: unknown;
}

export namespace ChatCompletionContentPartImage {
  export interface ImageURL {
    url: string;

    detail?: 'auto' | 'low' | 'high';

    [k: string]: unknown;
  }
}

export interface ChatCompletionContentPartRefusal {
  refusal: string;

  type: 'refusal';

  [k: string]: unknown;
}

/**
 * Learn about
 * [text inputs](https://platform.openai.com/docs/guides/text-generation).
 */
export interface ChatCompletionContentPartText {
  text: string;

  type: 'text';

  [k: string]: unknown;
}

/**
 * A call to a function tool created by the model.
 */
export interface ChatCompletionMessageFunctionToolCall {
  id: string;

  /**
   * The function that the model called.
   */
  function: ChatCompletionMessageFunctionToolCall.Function;

  type: 'function';

  [k: string]: unknown;
}

export namespace ChatCompletionMessageFunctionToolCall {
  /**
   * The function that the model called.
   */
  export interface Function {
    arguments: string;

    name: string;

    [k: string]: unknown;
  }
}

/**
 * Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text
 * generation.
 */
export interface File {
  file: File.File;

  type: 'file';

  [k: string]: unknown;
}

export namespace File {
  export interface File {
    file_data?: string;

    file_id?: string;

    filename?: string;

    [k: string]: unknown;
  }
}

export interface Message {
  author: Message.Author;

  channel?: string | null;

  content?: Array<unknown>;

  content_type?: string | null;

  recipient?: string | null;
}

export namespace Message {
  export interface Author {
    /**
     * The role of a message author (mirrors `chat::Role`).
     */
    role: 'user' | 'assistant' | 'system' | 'developer' | 'tool';

    name?: string | null;
  }
}

export type ChatCreateCompletionResponse = unknown;

export interface ChatCreateCompletionParams {
  messages: Array<
    | ChatCreateCompletionParams.ChatCompletionDeveloperMessageParam
    | ChatCreateCompletionParams.ChatCompletionSystemMessageParam
    | ChatCreateCompletionParams.ChatCompletionUserMessageParam
    | ChatCreateCompletionParams.ChatCompletionAssistantMessageParam
    | ChatCreateCompletionParams.ChatCompletionToolMessageParam
    | ChatCreateCompletionParams.ChatCompletionFunctionMessageParam
    | ChatCreateCompletionParams.CustomChatCompletionMessageParam
    | Message
  >;

  /**
   * If true, the generation prompt will be added to the chat template. This is a
   * parameter used by chat template in tokenizer config of the model.
   */
  add_generation_prompt?: boolean;

  /**
   * If true, special tokens (e.g. BOS) will be added to the prompt on top of what is
   * added by the chat template. For most models, the chat template takes care of
   * adding the special tokens so this should be set to false (as is the default).
   */
  add_special_tokens?: boolean;

  allowed_token_ids?: Array<number> | null;

  bad_words?: Array<string>;

  /**
   * If specified, the prefix cache will be salted with the provided string to
   * prevent an attacker to guess prompts in multi-user environments. The salt should
   * be random, protected from access by 3rd parties, and long enough to be
   * unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).
   */
  cache_salt?: string | null;

  /**
   * A Jinja template to use for this conversion. As of transformers v4.44, default
   * chat template is no longer allowed, so you must provide a chat template if the
   * tokenizer does not define one.
   */
  chat_template?: string | null;

  /**
   * Additional keyword args to pass to the template renderer. Will be accessible by
   * the chat template.
   */
  chat_template_kwargs?: { [key: string]: unknown } | null;

  /**
   * If this is set, the chat will be formatted so that the final message in the chat
   * is open-ended, without any EOS tokens. The model will continue this message
   * rather than starting a new one. This allows you to "prefill" part of the model's
   * response for it. Cannot be used at the same time as `add_generation_prompt`.
   */
  continue_final_message?: boolean;

  /**
   * A list of dicts representing documents that will be accessible to the model if
   * it is performing RAG (retrieval-augmented generation). If the template does not
   * support RAG, this argument will have no effect. We recommend that each document
   * should be a dict containing "title" and "text" keys.
   */
  documents?: Array<{ [key: string]: string }> | null;

  /**
   * If true, the new message will be prepended with the last message if they belong
   * to the same role.
   */
  echo?: boolean;

  frequency_penalty?: number | null;

  ignore_eos?: boolean;

  include_reasoning?: boolean;

  include_stop_str_in_output?: boolean;

  /**
   * KVTransfer parameters used for disaggregated serving.
   */
  kv_transfer_params?: { [key: string]: unknown } | null;

  length_penalty?: number;

  logit_bias?: { [key: string]: number } | null;

  /**
   * A list of either qualified names of logits processors, or constructor objects,
   * to apply when sampling. A constructor is a JSON object with a required
   * 'qualname' field specifying the qualified name of the processor class/factory,
   * and optional 'args' and 'kwargs' fields containing positional and keyword
   * arguments. For example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1,
   * 2], 'kwargs': {'param': 'value'}}.
   */
  logits_processors?: Array<string | ChatCreateCompletionParams.LogitsProcessorConstructor> | null;

  logprobs?: boolean | null;

  max_completion_tokens?: number | null;

  /**
   * @deprecated
   */
  max_tokens?: number | null;

  min_p?: number | null;

  min_tokens?: number;

  /**
   * Additional kwargs to pass to the HF processor.
   */
  mm_processor_kwargs?: { [key: string]: unknown } | null;

  model?: string | null;

  n?: number | null;

  parallel_tool_calls?: boolean | null;

  presence_penalty?: number | null;

  /**
   * The priority of the request (lower means earlier handling; default: 0). Any
   * priority other than 0 will raise an error if the served model does not use
   * priority scheduling.
   */
  priority?: number;

  prompt_logprobs?: number | null;

  reasoning_effort?: 'low' | 'medium' | 'high' | null;

  repetition_penalty?: number | null;

  /**
   * The request_id related to this request. If the caller does not set it, a
   * random_uuid will be generated. This id is used through out the inference process
   * and return in response.
   */
  request_id?: string;

  response_format?:
    | ChatCreateCompletionParams.ResponseFormat
    | ChatCreateCompletionParams.StructuralTagResponseFormat
    | ChatCreateCompletionParams.LegacyStructuralTagResponseFormat
    | null;

  /**
   * If specified, the result will include token IDs alongside the generated text. In
   * streaming mode, prompt_token_ids is included only in the first chunk, and
   * token_ids contains the delta tokens for each chunk. This is useful for debugging
   * or when you need to map generated text back to input tokens.
   */
  return_token_ids?: boolean | null;

  /**
   * If specified with 'logprobs', tokens are represented as strings of the form
   * 'token_id:{token_id}' so that tokens that are not JSON-encodable can be
   * identified.
   */
  return_tokens_as_token_ids?: boolean | null;

  seed?: number | null;

  skip_special_tokens?: boolean;

  spaces_between_special_tokens?: boolean;

  stop?: string | Array<string> | null;

  stop_token_ids?: Array<number> | null;

  stream?: boolean | null;

  stream_options?: ChatCreateCompletionParams.StreamOptions | null;

  /**
   * Additional kwargs for structured outputs
   */
  structured_outputs?: ChatCreateCompletionParams.StructuredOutputs | null;

  temperature?: number | null;

  tool_choice?:
    | 'none'
    | 'auto'
    | 'required'
    | ChatCreateCompletionParams.ChatCompletionNamedToolChoiceParam
    | null;

  tools?: Array<ChatCreateCompletionParams.Tool> | null;

  top_k?: number | null;

  top_logprobs?: number | null;

  top_p?: number | null;

  truncate_prompt_tokens?: number | null;

  use_beam_search?: boolean;

  user?: string | null;

  /**
   * Additional request parameters with (list of) string or numeric values, used by
   * custom extensions.
   */
  vllm_xargs?: { [key: string]: string | number | Array<string | number> } | null;

  [k: string]: unknown;
}

export namespace ChatCreateCompletionParams {
  /**
   * Developer-provided instructions that the model should follow, regardless of
   * messages sent by the user. With o1 models and newer, `developer` messages
   * replace the previous `system` messages.
   */
  export interface ChatCompletionDeveloperMessageParam {
    content: string | Array<ChatAPI.ChatCompletionContentPartText>;

    role: 'developer';

    name?: string;

    [k: string]: unknown;
  }

  /**
   * Developer-provided instructions that the model should follow, regardless of
   * messages sent by the user. With o1 models and newer, use `developer` messages
   * for this purpose instead.
   */
  export interface ChatCompletionSystemMessageParam {
    content: string | Array<ChatAPI.ChatCompletionContentPartText>;

    role: 'system';

    name?: string;

    [k: string]: unknown;
  }

  /**
   * Messages sent by an end user, containing prompts or additional context
   * information.
   */
  export interface ChatCompletionUserMessageParam {
    content:
      | string
      | Array<
          | ChatAPI.ChatCompletionContentPartText
          | ChatAPI.ChatCompletionContentPartImage
          | ChatAPI.ChatCompletionContentPartAudio
          | ChatAPI.File
        >;

    role: 'user';

    name?: string;

    [k: string]: unknown;
  }

  /**
   * Messages sent by the model in response to user messages.
   */
  export interface ChatCompletionAssistantMessageParam {
    role: 'assistant';

    /**
     * Data about a previous audio response from the model.
     * [Learn more](https://platform.openai.com/docs/guides/audio).
     */
    audio?: ChatCompletionAssistantMessageParam.Audio | null;

    content?:
      | string
      | Array<ChatAPI.ChatCompletionContentPartText | ChatAPI.ChatCompletionContentPartRefusal>
      | null;

    /**
     * Deprecated and replaced by `tool_calls`.
     *
     * The name and arguments of a function that should be called, as generated by the
     * model.
     */
    function_call?: ChatCompletionAssistantMessageParam.FunctionCall | null;

    name?: string;

    refusal?: string | null;

    tool_calls?: Array<
      | ChatAPI.ChatCompletionMessageFunctionToolCall
      | ChatCompletionAssistantMessageParam.ChatCompletionMessageCustomToolCallParam
    >;

    [k: string]: unknown;
  }

  export namespace ChatCompletionAssistantMessageParam {
    /**
     * Data about a previous audio response from the model.
     * [Learn more](https://platform.openai.com/docs/guides/audio).
     */
    export interface Audio {
      id: string;

      [k: string]: unknown;
    }

    /**
     * Deprecated and replaced by `tool_calls`.
     *
     * The name and arguments of a function that should be called, as generated by the
     * model.
     */
    export interface FunctionCall {
      arguments: string;

      name: string;

      [k: string]: unknown;
    }

    /**
     * A call to a custom tool created by the model.
     */
    export interface ChatCompletionMessageCustomToolCallParam {
      id: string;

      /**
       * The custom tool that the model called.
       */
      custom: ChatCompletionMessageCustomToolCallParam.Custom;

      type: 'custom';

      [k: string]: unknown;
    }

    export namespace ChatCompletionMessageCustomToolCallParam {
      /**
       * The custom tool that the model called.
       */
      export interface Custom {
        input: string;

        name: string;

        [k: string]: unknown;
      }
    }
  }

  export interface ChatCompletionToolMessageParam {
    content: string | Array<ChatAPI.ChatCompletionContentPartText>;

    role: 'tool';

    tool_call_id: string;

    [k: string]: unknown;
  }

  export interface ChatCompletionFunctionMessageParam {
    content: string | null;

    name: string;

    role: 'function';

    [k: string]: unknown;
  }

  /**
   * Enables custom roles in the Chat Completion API.
   */
  export interface CustomChatCompletionMessageParam {
    role: string;

    content?:
      | string
      | Array<
          | ChatAPI.ChatCompletionContentPartText
          | ChatAPI.ChatCompletionContentPartImage
          | ChatAPI.ChatCompletionContentPartAudio
          | ChatAPI.File
          | CustomChatCompletionMessageParam.ChatCompletionContentPartAudioParam
          | CustomChatCompletionMessageParam.ChatCompletionContentPartVideoParam
          | ChatAPI.ChatCompletionContentPartRefusal
          | CustomChatCompletionMessageParam.CustomChatCompletionContentSimpleImageParam
          | CustomChatCompletionMessageParam.ChatCompletionContentPartImageEmbedsParam
          | CustomChatCompletionMessageParam.ChatCompletionContentPartAudioEmbedsParam
          | CustomChatCompletionMessageParam.CustomChatCompletionContentSimpleAudioParam
          | CustomChatCompletionMessageParam.CustomChatCompletionContentSimpleVideoParam
          | string
          | CustomChatCompletionMessageParam.CustomThinkCompletionContentParam
        >;

    name?: string;

    reasoning?: string | null;

    tool_call_id?: string | null;

    tool_calls?: Array<ChatAPI.ChatCompletionMessageFunctionToolCall> | null;

    tools?: Array<CustomChatCompletionMessageParam.Tool> | null;

    [k: string]: unknown;
  }

  export namespace CustomChatCompletionMessageParam {
    export interface ChatCompletionContentPartAudioParam {
      audio_url: ChatCompletionContentPartAudioParam.AudioURL;

      type: 'audio_url';

      [k: string]: unknown;
    }

    export namespace ChatCompletionContentPartAudioParam {
      export interface AudioURL {
        url: string;

        [k: string]: unknown;
      }
    }

    export interface ChatCompletionContentPartVideoParam {
      type: 'video_url';

      video_url: ChatCompletionContentPartVideoParam.VideoURL;

      [k: string]: unknown;
    }

    export namespace ChatCompletionContentPartVideoParam {
      export interface VideoURL {
        url: string;

        [k: string]: unknown;
      }
    }

    /**
     * A simpler version of the param that only accepts a plain image_url. This is
     * supported by OpenAI API, although it is not documented.
     *
     * Example: { "image_url": "https://example.com/image.jpg" }
     */
    export interface CustomChatCompletionContentSimpleImageParam {
      image_url?: string | null;

      uuid?: string | null;

      [k: string]: unknown;
    }

    export interface ChatCompletionContentPartImageEmbedsParam {
      type: 'image_embeds';

      image_embeds?: string | { [key: string]: string } | null;

      uuid?: string | null;

      [k: string]: unknown;
    }

    export interface ChatCompletionContentPartAudioEmbedsParam {
      type: 'audio_embeds';

      audio_embeds?: string | { [key: string]: string } | null;

      uuid?: string | null;

      [k: string]: unknown;
    }

    /**
     * A simpler version of the param that only accepts a plain audio_url.
     *
     * Example: { "audio_url": "https://example.com/audio.mp3" }
     */
    export interface CustomChatCompletionContentSimpleAudioParam {
      audio_url?: string | null;

      [k: string]: unknown;
    }

    /**
     * A simpler version of the param that only accepts a plain audio_url.
     *
     * Example: { "video_url": "https://example.com/video.mp4" }
     */
    export interface CustomChatCompletionContentSimpleVideoParam {
      uuid?: string | null;

      video_url?: string | null;

      [k: string]: unknown;
    }

    /**
     * A Think Completion Content Param that accepts a plain text and a boolean.
     *
     * Example: { "thinking": "I am thinking about the answer", "closed": True, "type":
     * "thinking" }
     */
    export interface CustomThinkCompletionContentParam {
      thinking: string;

      type: 'thinking';

      closed?: boolean;

      [k: string]: unknown;
    }

    /**
     * A function tool that can be used to generate a response.
     */
    export interface Tool {
      function: Tool.Function;

      type: 'function';

      [k: string]: unknown;
    }

    export namespace Tool {
      export interface Function {
        name: string;

        description?: string;

        parameters?: { [key: string]: unknown };

        strict?: boolean | null;

        [k: string]: unknown;
      }
    }
  }

  export interface LogitsProcessorConstructor {
    qualname: string;

    args?: Array<unknown> | null;

    kwargs?: { [key: string]: unknown } | null;
  }

  export interface ResponseFormat {
    type: 'text' | 'json_object' | 'json_schema';

    json_schema?: ResponseFormat.JsonSchema | null;

    [k: string]: unknown;
  }

  export namespace ResponseFormat {
    export interface JsonSchema {
      name: string;

      description?: string | null;

      schema?: { [key: string]: unknown } | null;

      strict?: boolean | null;

      [k: string]: unknown;
    }
  }

  export interface StructuralTagResponseFormat {
    format: unknown;

    type: 'structural_tag';

    [k: string]: unknown;
  }

  export interface LegacyStructuralTagResponseFormat {
    structures: Array<LegacyStructuralTagResponseFormat.Structure>;

    triggers: Array<string>;

    type: 'structural_tag';

    [k: string]: unknown;
  }

  export namespace LegacyStructuralTagResponseFormat {
    export interface Structure {
      begin: string;

      end: string;

      schema?: { [key: string]: unknown } | null;

      [k: string]: unknown;
    }
  }

  export interface StreamOptions {
    continuous_usage_stats?: boolean | null;

    include_usage?: boolean | null;

    [k: string]: unknown;
  }

  /**
   * Additional kwargs for structured outputs
   */
  export interface StructuredOutputs {
    _backend?: string | null;

    _backend_was_auto?: boolean;

    choice?: Array<string> | null;

    disable_additional_properties?: boolean;

    disable_any_whitespace?: boolean;

    disable_fallback?: boolean;

    grammar?: string | null;

    json?: string | { [key: string]: unknown } | null;

    json_object?: boolean | null;

    regex?: string | null;

    structural_tag?: string | null;

    whitespace_pattern?: string | null;
  }

  export interface ChatCompletionNamedToolChoiceParam {
    function: ChatCompletionNamedToolChoiceParam.Function;

    type?: 'function';

    [k: string]: unknown;
  }

  export namespace ChatCompletionNamedToolChoiceParam {
    export interface Function {
      name: string;

      [k: string]: unknown;
    }
  }

  export interface Tool {
    function: Tool.Function;

    type?: 'function';

    [k: string]: unknown;
  }

  export namespace Tool {
    export interface Function {
      name: string;

      description?: string | null;

      parameters?: { [key: string]: unknown } | null;

      [k: string]: unknown;
    }
  }
}

export declare namespace Chat {
  export {
    type ChatCompletionContentPartAudio as ChatCompletionContentPartAudio,
    type ChatCompletionContentPartImage as ChatCompletionContentPartImage,
    type ChatCompletionContentPartRefusal as ChatCompletionContentPartRefusal,
    type ChatCompletionContentPartText as ChatCompletionContentPartText,
    type ChatCompletionMessageFunctionToolCall as ChatCompletionMessageFunctionToolCall,
    type File as File,
    type Message as Message,
    type ChatCreateCompletionResponse as ChatCreateCompletionResponse,
    type ChatCreateCompletionParams as ChatCreateCompletionParams,
  };
}
