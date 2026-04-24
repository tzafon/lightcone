// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import * as ResponsesAPI from './responses';
import * as ChatAPI from './chat';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class Responses extends APIResource {
  /**
   * Create Responses
   */
  create(body: ResponseCreateParams, options?: RequestOptions): APIPromise<ResponseCreateResponse> {
    return this._client.post('/v1/responses', { body, ...options });
  }

  /**
   * Retrieve Responses
   */
  retrieve(responseID: string, query: ResponseRetrieveParams | null | undefined = {}, options?: RequestOptions): APIPromise<unknown> {
    return this._client.get(path`/v1/responses/${responseID}`, { query, ...options });
  }

  /**
   * Cancel Responses
   */
  cancel(responseID: string, options?: RequestOptions): APIPromise<unknown> {
    return this._client.post(path`/v1/responses/${responseID}/cancel`, options);
  }
}

/**
 * A click action.
 */
export interface ActionClick {
  button: 'left' | 'right' | 'wheel' | 'back' | 'forward';

  type: 'click';

  x: number;

  y: number;

[k: string]: unknown
}

/**
 * A double click action.
 */
export interface ActionDoubleClick {
  type: 'double_click';

  x: number;

  y: number;

[k: string]: unknown
}

/**
 * A drag action.
 */
export interface ActionDrag {
  path: Array<ActionDrag.Path>;

  type: 'drag';

[k: string]: unknown
}

export namespace ActionDrag {
  /**
   * An x/y coordinate pair, e.g. `{ x: 100, y: 200 }`.
   */
  export interface Path {
    x: number;

    y: number;

  [k: string]: unknown
  }
}

/**
 * Action type "find": Searches for a pattern within a loaded page.
 */
export interface ActionFind {
  pattern: string;

  type: 'find';

  url: string;

[k: string]: unknown
}

/**
 * A collection of keypresses the model would like to perform.
 */
export interface ActionKeypress {
  keys: Array<string>;

  type: 'keypress';

[k: string]: unknown
}

/**
 * A mouse move action.
 */
export interface ActionMove {
  type: 'move';

  x: number;

  y: number;

[k: string]: unknown
}

/**
 * Action type "open_page" - Opens a specific URL from search results.
 */
export interface ActionOpenPage {
  type: 'open_page';

  url: string;

[k: string]: unknown
}

/**
 * A screenshot action.
 */
export interface ActionScreenshot {
  type: 'screenshot';

[k: string]: unknown
}

/**
 * A scroll action.
 */
export interface ActionScroll {
  scroll_x: number;

  scroll_y: number;

  type: 'scroll';

  x: number;

  y: number;

[k: string]: unknown
}

/**
 * A source used in the search.
 */
export interface ActionSearchSource {
  type: 'url';

  url: string;

[k: string]: unknown
}

/**
 * An action to type in text.
 */
export interface ActionType {
  text: string;

  type: 'type';

[k: string]: unknown
}

/**
 * A wait action.
 */
export interface ActionWait {
  type: 'wait';

[k: string]: unknown
}

/**
 * A citation for a container file used to generate a model response.
 */
export interface AnnotationContainerFileCitation {
  container_id: string;

  end_index: number;

  file_id: string;

  filename: string;

  start_index: number;

  type: 'container_file_citation';

[k: string]: unknown
}

/**
 * A citation to a file.
 */
export interface AnnotationFileCitation {
  file_id: string;

  filename: string;

  index: number;

  type: 'file_citation';

[k: string]: unknown
}

/**
 * A path to a file.
 */
export interface AnnotationFilePath {
  file_id: string;

  index: number;

  type: 'file_path';

[k: string]: unknown
}

/**
 * A citation for a web resource used to generate a model response.
 */
export interface AnnotationURLCitation {
  end_index: number;

  start_index: number;

  title: string;

  type: 'url_citation';

  url: string;

[k: string]: unknown
}

/**
 * The log probability of a token.
 */
export interface Logprob {
  token: string;

  bytes: Array<number>;

  logprob: number;

  top_logprobs: Array<Logprob.TopLogprob>;

[k: string]: unknown
}

export namespace Logprob {
  /**
   * The top log probability of a token.
   */
  export interface TopLogprob {
    token: string;

    bytes: Array<number>;

    logprob: number;

  [k: string]: unknown
  }
}

/**
 * A request for human approval of a tool invocation.
 */
export interface McpApprovalRequest {
  id: string;

  arguments: string;

  name: string;

  server_label: string;

  type: 'mcp_approval_request';

[k: string]: unknown
}

/**
 * The image output from the code interpreter.
 */
export interface OutputImage {
  type: 'image';

  url: string;

[k: string]: unknown
}

/**
 * The logs output from the code interpreter.
 */
export interface OutputLogs {
  logs: string;

  type: 'logs';

[k: string]: unknown
}

/**
 * A file input to the model.
 */
export interface ResponseInputFileParam {
  type: 'input_file';

  file_data?: string;

  file_id?: string | null;

  file_url?: string;

  filename?: string;

[k: string]: unknown
}

/**
 * An image input to the model.
 *
 * Learn about [image inputs](https://platform.openai.com/docs/guides/vision).
 */
export interface ResponseInputImageParam {
  detail: 'low' | 'high' | 'auto';

  type: 'input_image';

  file_id?: string | null;

  image_url?: string | null;

[k: string]: unknown
}

/**
 * A text input to the model.
 */
export interface ResponseInputTextParam {
  text: string;

  type: 'input_text';

[k: string]: unknown
}

/**
 * A summary text from the model.
 */
export interface Summary {
  text: string;

  type: 'summary_text';

[k: string]: unknown
}

/**
 * The response object returned by the Responses API.
 */
export interface ResponseCreateResponse {
  id: string;

  created_at: number;

  model: string;

  object: 'response';

  output: Array<ResponseCreateResponse.ResponseOutputMessage | ResponseCreateResponse.ResponseFunctionToolCall | ResponseCreateResponse.ResponseComputerToolCall | { [key: string]: unknown }>;

  status: 'completed' | 'failed' | 'in_progress' | 'incomplete' | 'cancelled';

  error?: { [key: string]: unknown } | null;

  tools?: Array<{ [key: string]: unknown }>;

  usage?: ResponseCreateResponse.Usage | null;

[k: string]: unknown
}

export namespace ResponseCreateResponse {
  /**
   * An output message from the model.
   */
  export interface ResponseOutputMessage {
    id: string;

    content: Array<ResponseOutputMessage.ResponseOutputText | ResponseOutputMessage.ResponseOutputRefusal>;

    role: 'assistant';

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'message';

  [k: string]: unknown
  }

  export namespace ResponseOutputMessage {
    /**
     * A text output from the model.
     */
    export interface ResponseOutputText {
      annotations: Array<ResponsesAPI.AnnotationFileCitation | ResponsesAPI.AnnotationURLCitation | ResponsesAPI.AnnotationContainerFileCitation | ResponsesAPI.AnnotationFilePath>;

      text: string;

      type: 'output_text';

      logprobs?: Array<ResponsesAPI.Logprob> | null;

    [k: string]: unknown
    }

    /**
     * A refusal from the model.
     */
    export interface ResponseOutputRefusal {
      refusal: string;

      type: 'refusal';

    [k: string]: unknown
    }
  }

  /**
   * A tool call to run a function.
   *
   * See the
   * [function calling guide](https://platform.openai.com/docs/guides/function-calling)
   * for more information.
   */
  export interface ResponseFunctionToolCall {
    arguments: string;

    call_id: string;

    name: string;

    type: 'function_call';

    id?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  /**
   * A tool call to a computer use tool.
   *
   * See the
   * [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use)
   * for more information.
   */
  export interface ResponseComputerToolCall {
    id: string;

    /**
     * A click action.
     */
    action: ResponsesAPI.ActionClick | ResponsesAPI.ActionDoubleClick | ResponsesAPI.ActionDrag | ResponsesAPI.ActionKeypress | ResponsesAPI.ActionMove | ResponsesAPI.ActionScreenshot | ResponsesAPI.ActionScroll | ResponsesAPI.ActionType | ResponsesAPI.ActionWait | ResponseComputerToolCall.ActionPointAndType | ResponseComputerToolCall.ActionMouseDown | ResponseComputerToolCall.ActionMouseUp | ResponseComputerToolCall.ActionKeyDown | ResponseComputerToolCall.ActionKeyUp;

    call_id: string;

    pending_safety_checks: Array<ResponseComputerToolCall.PendingSafetyCheck>;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'computer_call';

  [k: string]: unknown
  }

  export namespace ResponseComputerToolCall {
    /**
     * Click at a position then type text.
     */
    export interface ActionPointAndType {
      text: string;

      type: 'point_and_type';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Press and hold the left mouse button at a position.
     */
    export interface ActionMouseDown {
      type: 'mouse_down';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Release the left mouse button at a position.
     */
    export interface ActionMouseUp {
      type: 'mouse_up';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Press and hold a key.
     */
    export interface ActionKeyDown {
      keys: Array<string>;

      type: 'key_down';

    [k: string]: unknown
    }

    /**
     * Release a held key.
     */
    export interface ActionKeyUp {
      keys: Array<string>;

      type: 'key_up';

    [k: string]: unknown
    }

    /**
     * A pending safety check for the computer call.
     */
    export interface PendingSafetyCheck {
      id: string;

      code?: string | null;

      message?: string | null;

    [k: string]: unknown
    }
  }

  export interface Usage {
    input_tokens?: number;

    output_tokens?: number;

    total_tokens?: number;

  [k: string]: unknown
  }
}

export type ResponseRetrieveResponse = unknown

export type ResponseCancelResponse = unknown

export interface ResponseCreateParams {
  input: string | Array<ResponseCreateParams.EasyInputMessageParam | ResponseCreateParams.Message | ResponseCreateParams.ResponseOutputMessageParam | ResponseCreateParams.ResponseFileSearchToolCallParam | ResponseCreateParams.ResponseComputerToolCallParam | ResponseCreateParams.ComputerCallOutput | ResponseCreateParams.ResponseFunctionWebSearchParam | ResponseCreateParams.ResponseFunctionToolCallParam | ResponseCreateParams.FunctionCallOutput | ResponseCreateParams.ResponseReasoningItemParam | ResponseCreateParams.ResponseCompactionItemParamParam | ResponseCreateParams.ImageGenerationCall | ResponseCreateParams.ResponseCodeInterpreterToolCallParam | ResponseCreateParams.LocalShellCall | ResponseCreateParams.LocalShellCallOutput | ResponseCreateParams.ShellCall | ResponseCreateParams.ShellCallOutput | ResponseCreateParams.ApplyPatchCall | ResponseCreateParams.ApplyPatchCallOutput | ResponseCreateParams.McpListTools | McpApprovalRequest | ResponseCreateParams.McpApprovalResponse | ResponseCreateParams.McpCall | ResponseCreateParams.ResponseCustomToolCallOutputParam | ResponseCreateParams.ResponseCustomToolCallParam | ResponseCreateParams.ItemReference | ResponseCreateParams.ResponseOutputMessage | ResponseCreateParams.ResponseFileSearchToolCall | ResponseCreateParams.ResponseFunctionToolCall | ResponseCreateParams.ResponseFunctionWebSearch | ResponseCreateParams.ResponseComputerToolCall | ResponseCreateParams.ResponseReasoningItem | ResponseCreateParams.ResponseCompactionItem | ResponseCreateParams.ImageGenerationCall | ResponseCreateParams.ResponseCodeInterpreterToolCall | ResponseCreateParams.LocalShellCall | ResponseCreateParams.ResponseFunctionShellToolCall | ResponseCreateParams.ResponseFunctionShellToolCallOutput | ResponseCreateParams.ResponseApplyPatchToolCall | ResponseCreateParams.ResponseApplyPatchToolCallOutput | ResponseCreateParams.McpCall | ResponseCreateParams.McpListTools | McpApprovalRequest | ResponseCreateParams.ResponseCustomToolCall>;

  background?: boolean | null;

  /**
   * If specified, the prefix cache will be salted with the provided string to
   * prevent an attacker to guess prompts in multi-user environments. The salt should
   * be random, protected from access by 3rd parties, and long enough to be
   * unpredictable (e.g., 43 characters base64-encoded, corresponding to 256 bit).
   */
  cache_salt?: string | null;

  /**
   * Dictates whether or not to return messages as part of the response object.
   * Currently only supported fornon-background and gpt-oss only.
   */
  enable_response_messages?: boolean;

  include?: Array<'code_interpreter_call.outputs' | 'computer_call_output.output.image_url' | 'file_search_call.results' | 'message.input_image.image_url' | 'message.output_text.logprobs' | 'reasoning.encrypted_content'> | null;

  include_stop_str_in_output?: boolean;

  instructions?: string | null;

  logit_bias?: { [key: string]: number } | null;

  max_output_tokens?: number | null;

  max_tool_calls?: number | null;

  metadata?: { [key: string]: string } | null;

  /**
   * Additional kwargs to pass to the HF processor.
   */
  mm_processor_kwargs?: { [key: string]: unknown } | null;

  model?: string | null;

  parallel_tool_calls?: boolean | null;

  previous_input_messages?: Array<ChatAPI.Message | { [key: string]: unknown }> | null;

  previous_response_id?: string | null;

  /**
   * The priority of the request (lower means earlier handling; default: 0). Any
   * priority other than 0 will raise an error if the served model does not use
   * priority scheduling.
   */
  priority?: number;

  /**
   * Reference to a prompt template and its variables.
   * [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).
   */
  prompt?: ResponseCreateParams.Prompt | null;

  /**
   * A key that was used to read from or write to the prompt cache.Note: This field
   * has not been implemented yet and vLLM will ignore it.
   */
  prompt_cache_key?: string | null;

  /**
   * **gpt-5 and o-series models only**
   *
   * Configuration options for
   * [reasoning models](https://platform.openai.com/docs/guides/reasoning).
   */
  reasoning?: ResponseCreateParams.Reasoning | null;

  /**
   * The request_id related to this request. If the caller does not set it, a
   * random_uuid will be generated. This id is used through out the inference process
   * and return in response.
   */
  request_id?: string;

  service_tier?: 'auto' | 'default' | 'flex' | 'scale' | 'priority';

  skip_special_tokens?: boolean;

  store?: boolean | null;

  stream?: boolean | null;

  temperature?: number | null;

  /**
   * Configuration options for a text response from the model.
   *
   * Can be plain text or structured JSON data. Learn more:
   *
   * - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
   * - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
   */
  text?: ResponseCreateParams.Text | null;

  /**
   * Constrains the tools available to the model to a pre-defined set.
   */
  tool_choice?: 'none' | 'auto' | 'required' | ResponseCreateParams.ToolChoiceAllowed | ResponseCreateParams.ToolChoiceTypes | ResponseCreateParams.ToolChoiceFunction | ResponseCreateParams.ToolChoiceCustom;

  tools?: Array<ResponseCreateParams.FunctionTool | ResponseCreateParams.CustomTool | ResponseCreateParams.ComputerTool>;

  top_k?: number | null;

  top_logprobs?: number | null;

  top_p?: number | null;

  truncation?: 'auto' | 'disabled' | null;

  user?: string | null;

[k: string]: unknown
}

export namespace ResponseCreateParams {
  /**
   * A message input to the model with a role indicating instruction following
   * hierarchy. Instructions given with the `developer` or `system` role take
   * precedence over instructions given with the `user` role. Messages with the
   * `assistant` role are presumed to have been generated by the model in previous
   * interactions.
   */
  export interface EasyInputMessageParam {
    content: string | Array<ResponsesAPI.ResponseInputTextParam | ResponsesAPI.ResponseInputImageParam | ResponsesAPI.ResponseInputFileParam>;

    role: 'user' | 'assistant' | 'system' | 'developer';

    type?: 'message';

  [k: string]: unknown
  }

  /**
   * A message input to the model with a role indicating instruction following
   * hierarchy. Instructions given with the `developer` or `system` role take
   * precedence over instructions given with the `user` role.
   */
  export interface Message {
    content: Array<ResponsesAPI.ResponseInputTextParam | ResponsesAPI.ResponseInputImageParam | ResponsesAPI.ResponseInputFileParam>;

    role: 'user' | 'system' | 'developer';

    status?: 'in_progress' | 'completed' | 'incomplete';

    type?: 'message';

  [k: string]: unknown
  }

  /**
   * An output message from the model.
   */
  export interface ResponseOutputMessageParam {
    id: string;

    content: Array<ResponseOutputMessageParam.ResponseOutputTextParam | ResponseOutputMessageParam.ResponseOutputRefusalParam>;

    role: 'assistant';

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'message';

  [k: string]: unknown
  }

  export namespace ResponseOutputMessageParam {
    /**
     * A text output from the model.
     */
    export interface ResponseOutputTextParam {
      annotations: Array<ResponsesAPI.AnnotationFileCitation | ResponsesAPI.AnnotationURLCitation | ResponsesAPI.AnnotationContainerFileCitation | ResponsesAPI.AnnotationFilePath>;

      text: string;

      type: 'output_text';

      logprobs?: Array<ResponsesAPI.Logprob>;

    [k: string]: unknown
    }

    /**
     * A refusal from the model.
     */
    export interface ResponseOutputRefusalParam {
      refusal: string;

      type: 'refusal';

    [k: string]: unknown
    }
  }

  /**
   * The results of a file search tool call.
   *
   * See the
   * [file search guide](https://platform.openai.com/docs/guides/tools-file-search)
   * for more information.
   */
  export interface ResponseFileSearchToolCallParam {
    id: string;

    queries: Array<string>;

    status: 'in_progress' | 'searching' | 'completed' | 'incomplete' | 'failed';

    type: 'file_search_call';

    results?: Array<ResponseFileSearchToolCallParam.Result> | null;

  [k: string]: unknown
  }

  export namespace ResponseFileSearchToolCallParam {
    export interface Result {
      attributes?: { [key: string]: string | number | boolean } | null;

      file_id?: string;

      filename?: string;

      score?: number;

      text?: string;

    [k: string]: unknown
    }
  }

  /**
   * A tool call to a computer use tool.
   *
   * See the
   * [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use)
   * for more information.
   */
  export interface ResponseComputerToolCallParam {
    id: string;

    /**
     * A click action.
     */
    action: ResponsesAPI.ActionClick | ResponsesAPI.ActionDoubleClick | ResponsesAPI.ActionDrag | ResponsesAPI.ActionKeypress | ResponsesAPI.ActionMove | ResponsesAPI.ActionScreenshot | ResponsesAPI.ActionScroll | ResponsesAPI.ActionType | ResponsesAPI.ActionWait | ResponseComputerToolCallParam.ActionPointAndType | ResponseComputerToolCallParam.ActionMouseDown | ResponseComputerToolCallParam.ActionMouseUp | ResponseComputerToolCallParam.ActionKeyDown | ResponseComputerToolCallParam.ActionKeyUp;

    call_id: string;

    pending_safety_checks: Array<ResponseComputerToolCallParam.PendingSafetyCheck>;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'computer_call';

  [k: string]: unknown
  }

  export namespace ResponseComputerToolCallParam {
    /**
     * Click at a position then type text.
     */
    export interface ActionPointAndType {
      text: string;

      type: 'point_and_type';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Press and hold the left mouse button at a position.
     */
    export interface ActionMouseDown {
      type: 'mouse_down';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Release the left mouse button at a position.
     */
    export interface ActionMouseUp {
      type: 'mouse_up';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Press and hold a key.
     */
    export interface ActionKeyDown {
      keys: Array<string>;

      type: 'key_down';

    [k: string]: unknown
    }

    /**
     * Release a held key.
     */
    export interface ActionKeyUp {
      keys: Array<string>;

      type: 'key_up';

    [k: string]: unknown
    }

    /**
     * A pending safety check for the computer call.
     */
    export interface PendingSafetyCheck {
      id: string;

      code?: string | null;

      message?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * The output of a computer tool call.
   */
  export interface ComputerCallOutput {
    call_id: string;

    /**
     * A computer screenshot image used with the computer use tool.
     */
    output: ComputerCallOutput.Output;

    type: 'computer_call_output';

    id?: string | null;

    acknowledged_safety_checks?: Array<ComputerCallOutput.AcknowledgedSafetyCheck> | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  export namespace ComputerCallOutput {
    /**
     * A computer screenshot image used with the computer use tool.
     */
    export interface Output {
      type: 'computer_screenshot';

      file_id?: string;

      image_url?: string;

    [k: string]: unknown
    }

    /**
     * A pending safety check for the computer call.
     */
    export interface AcknowledgedSafetyCheck {
      id: string;

      code?: string | null;

      message?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * The results of a web search tool call.
   *
   * See the
   * [web search guide](https://platform.openai.com/docs/guides/tools-web-search) for
   * more information.
   */
  export interface ResponseFunctionWebSearchParam {
    id: string;

    /**
     * Action type "search" - Performs a web search query.
     */
    action: ResponseFunctionWebSearchParam.ActionSearch | ResponsesAPI.ActionOpenPage | ResponsesAPI.ActionFind;

    status: 'in_progress' | 'searching' | 'completed' | 'failed';

    type: 'web_search_call';

  [k: string]: unknown
  }

  export namespace ResponseFunctionWebSearchParam {
    /**
     * Action type "search" - Performs a web search query.
     */
    export interface ActionSearch {
      query: string;

      type: 'search';

      queries?: Array<string>;

      sources?: Array<ResponsesAPI.ActionSearchSource>;

    [k: string]: unknown
    }
  }

  /**
   * A tool call to run a function.
   *
   * See the
   * [function calling guide](https://platform.openai.com/docs/guides/function-calling)
   * for more information.
   */
  export interface ResponseFunctionToolCallParam {
    arguments: string;

    call_id: string;

    name: string;

    type: 'function_call';

    id?: string;

    status?: 'in_progress' | 'completed' | 'incomplete';

  [k: string]: unknown
  }

  /**
   * The output of a function tool call.
   */
  export interface FunctionCallOutput {
    call_id: string;

    output: string | Array<FunctionCallOutput.ResponseInputTextContentParam | FunctionCallOutput.ResponseInputImageContentParam | FunctionCallOutput.ResponseInputFileContentParam>;

    type: 'function_call_output';

    id?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  export namespace FunctionCallOutput {
    /**
     * A text input to the model.
     */
    export interface ResponseInputTextContentParam {
      text: string;

      type: 'input_text';

    [k: string]: unknown
    }

    /**
     * An image input to the model.
     *
     * Learn about [image inputs](https://platform.openai.com/docs/guides/vision)
     */
    export interface ResponseInputImageContentParam {
      type: 'input_image';

      detail?: 'low' | 'high' | 'auto' | null;

      file_id?: string | null;

      image_url?: string | null;

    [k: string]: unknown
    }

    /**
     * A file input to the model.
     */
    export interface ResponseInputFileContentParam {
      type: 'input_file';

      file_data?: string | null;

      file_id?: string | null;

      file_url?: string | null;

      filename?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * A description of the chain of thought used by a reasoning model while generating
   * a response. Be sure to include these items in your `input` to the Responses API
   * for subsequent turns of a conversation if you are manually
   * [managing context](https://platform.openai.com/docs/guides/conversation-state).
   */
  export interface ResponseReasoningItemParam {
    id: string;

    summary: Array<ResponsesAPI.Summary>;

    type: 'reasoning';

    content?: Array<ResponseReasoningItemParam.Content>;

    encrypted_content?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete';

  [k: string]: unknown
  }

  export namespace ResponseReasoningItemParam {
    /**
     * Reasoning text from the model.
     */
    export interface Content {
      text: string;

      type: 'reasoning_text';

    [k: string]: unknown
    }
  }

  /**
   * A compaction item generated by the
   * [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).
   */
  export interface ResponseCompactionItemParamParam {
    encrypted_content: string;

    type: 'compaction';

    id?: string | null;

  [k: string]: unknown
  }

  /**
   * An image generation request made by the model.
   */
  export interface ImageGenerationCall {
    id: string;

    result: string | null;

    status: 'in_progress' | 'completed' | 'generating' | 'failed';

    type: 'image_generation_call';

  [k: string]: unknown
  }

  /**
   * A tool call to run code.
   */
  export interface ResponseCodeInterpreterToolCallParam {
    id: string;

    code: string | null;

    container_id: string;

    outputs: Array<ResponsesAPI.OutputLogs | ResponsesAPI.OutputImage> | null;

    status: 'in_progress' | 'completed' | 'incomplete' | 'interpreting' | 'failed';

    type: 'code_interpreter_call';

  [k: string]: unknown
  }

  /**
   * A tool call to run a command on the local shell.
   */
  export interface LocalShellCall {
    id: string;

    /**
     * Execute a shell command on the server.
     */
    action: LocalShellCall.Action;

    call_id: string;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'local_shell_call';

  [k: string]: unknown
  }

  export namespace LocalShellCall {
    /**
     * Execute a shell command on the server.
     */
    export interface Action {
      command: Array<string>;

      env: { [key: string]: string };

      type: 'exec';

      timeout_ms?: number | null;

      user?: string | null;

      working_directory?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * The output of a local shell tool call.
   */
  export interface LocalShellCallOutput {
    id: string;

    output: string;

    type: 'local_shell_call_output';

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  /**
   * A tool representing a request to execute one or more shell commands.
   */
  export interface ShellCall {
    /**
     * The shell commands and limits that describe how to run the tool call.
     */
    action: ShellCall.Action;

    call_id: string;

    type: 'shell_call';

    id?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  export namespace ShellCall {
    /**
     * The shell commands and limits that describe how to run the tool call.
     */
    export interface Action {
      commands: Array<string>;

      max_output_length?: number | null;

      timeout_ms?: number | null;

    [k: string]: unknown
    }
  }

  /**
   * The streamed output items emitted by a shell tool call.
   */
  export interface ShellCallOutput {
    call_id: string;

    output: Array<ShellCallOutput.Output>;

    type: 'shell_call_output';

    id?: string | null;

    max_output_length?: number | null;

  [k: string]: unknown
  }

  export namespace ShellCallOutput {
    /**
     * Captured stdout and stderr for a portion of a shell tool call output.
     */
    export interface Output {
      /**
       * Indicates that the shell call exceeded its configured time limit.
       */
      outcome: Output.OutcomeTimeout | Output.OutcomeExit;

      stderr: string;

      stdout: string;

    [k: string]: unknown
    }

    export namespace Output {
      /**
       * Indicates that the shell call exceeded its configured time limit.
       */
      export interface OutcomeTimeout {
        type: 'timeout';

      [k: string]: unknown
      }

      /**
       * Indicates that the shell commands finished and returned an exit code.
       */
      export interface OutcomeExit {
        exit_code: number;

        type: 'exit';

      [k: string]: unknown
      }
    }
  }

  /**
   * A tool call representing a request to create, delete, or update files using diff
   * patches.
   */
  export interface ApplyPatchCall {
    call_id: string;

    /**
     * Instruction for creating a new file via the apply_patch tool.
     */
    operation: ApplyPatchCall.ApplyPatchCallOperationCreateFile | ApplyPatchCall.ApplyPatchCallOperationDeleteFile | ApplyPatchCall.ApplyPatchCallOperationUpdateFile;

    status: 'in_progress' | 'completed';

    type: 'apply_patch_call';

    id?: string | null;

  [k: string]: unknown
  }

  export namespace ApplyPatchCall {
    /**
     * Instruction for creating a new file via the apply_patch tool.
     */
    export interface ApplyPatchCallOperationCreateFile {
      diff: string;

      path: string;

      type: 'create_file';

    [k: string]: unknown
    }

    /**
     * Instruction for deleting an existing file via the apply_patch tool.
     */
    export interface ApplyPatchCallOperationDeleteFile {
      path: string;

      type: 'delete_file';

    [k: string]: unknown
    }

    /**
     * Instruction for updating an existing file via the apply_patch tool.
     */
    export interface ApplyPatchCallOperationUpdateFile {
      diff: string;

      path: string;

      type: 'update_file';

    [k: string]: unknown
    }
  }

  /**
   * The streamed output emitted by an apply patch tool call.
   */
  export interface ApplyPatchCallOutput {
    call_id: string;

    status: 'completed' | 'failed';

    type: 'apply_patch_call_output';

    id?: string | null;

    output?: string | null;

  [k: string]: unknown
  }

  /**
   * A list of tools available on an MCP server.
   */
  export interface McpListTools {
    id: string;

    server_label: string;

    tools: Array<McpListTools.Tool>;

    type: 'mcp_list_tools';

    error?: string | null;

  [k: string]: unknown
  }

  export namespace McpListTools {
    /**
     * A tool available on an MCP server.
     */
    export interface Tool {
      input_schema: unknown;

      name: string;

      annotations?: unknown;

      description?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * A response to an MCP approval request.
   */
  export interface McpApprovalResponse {
    approval_request_id: string;

    approve: boolean;

    type: 'mcp_approval_response';

    id?: string | null;

    reason?: string | null;

  [k: string]: unknown
  }

  /**
   * An invocation of a tool on an MCP server.
   */
  export interface McpCall {
    id: string;

    arguments: string;

    name: string;

    server_label: string;

    type: 'mcp_call';

    approval_request_id?: string | null;

    error?: string | null;

    output?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | 'calling' | 'failed';

  [k: string]: unknown
  }

  /**
   * The output of a custom tool call from your code, being sent back to the model.
   */
  export interface ResponseCustomToolCallOutputParam {
    call_id: string;

    output: string | Array<ResponsesAPI.ResponseInputTextParam | ResponsesAPI.ResponseInputImageParam | ResponsesAPI.ResponseInputFileParam>;

    type: 'custom_tool_call_output';

    id?: string;

  [k: string]: unknown
  }

  /**
   * A call to a custom tool created by the model.
   */
  export interface ResponseCustomToolCallParam {
    call_id: string;

    input: string;

    name: string;

    type: 'custom_tool_call';

    id?: string;

  [k: string]: unknown
  }

  /**
   * An internal identifier for an item to reference.
   */
  export interface ItemReference {
    id: string;

    type?: 'item_reference' | null;

  [k: string]: unknown
  }

  /**
   * An output message from the model.
   */
  export interface ResponseOutputMessage {
    id: string;

    content: Array<ResponseOutputMessage.ResponseOutputText | ResponseOutputMessage.ResponseOutputRefusal>;

    role: 'assistant';

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'message';

  [k: string]: unknown
  }

  export namespace ResponseOutputMessage {
    /**
     * A text output from the model.
     */
    export interface ResponseOutputText {
      annotations: Array<ResponsesAPI.AnnotationFileCitation | ResponsesAPI.AnnotationURLCitation | ResponsesAPI.AnnotationContainerFileCitation | ResponsesAPI.AnnotationFilePath>;

      text: string;

      type: 'output_text';

      logprobs?: Array<ResponsesAPI.Logprob> | null;

    [k: string]: unknown
    }

    /**
     * A refusal from the model.
     */
    export interface ResponseOutputRefusal {
      refusal: string;

      type: 'refusal';

    [k: string]: unknown
    }
  }

  /**
   * The results of a file search tool call.
   *
   * See the
   * [file search guide](https://platform.openai.com/docs/guides/tools-file-search)
   * for more information.
   */
  export interface ResponseFileSearchToolCall {
    id: string;

    queries: Array<string>;

    status: 'in_progress' | 'searching' | 'completed' | 'incomplete' | 'failed';

    type: 'file_search_call';

    results?: Array<ResponseFileSearchToolCall.Result> | null;

  [k: string]: unknown
  }

  export namespace ResponseFileSearchToolCall {
    export interface Result {
      attributes?: { [key: string]: string | number | boolean } | null;

      file_id?: string | null;

      filename?: string | null;

      score?: number | null;

      text?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * A tool call to run a function.
   *
   * See the
   * [function calling guide](https://platform.openai.com/docs/guides/function-calling)
   * for more information.
   */
  export interface ResponseFunctionToolCall {
    arguments: string;

    call_id: string;

    name: string;

    type: 'function_call';

    id?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  /**
   * The results of a web search tool call.
   *
   * See the
   * [web search guide](https://platform.openai.com/docs/guides/tools-web-search) for
   * more information.
   */
  export interface ResponseFunctionWebSearch {
    id: string;

    /**
     * Action type "search" - Performs a web search query.
     */
    action: ResponseFunctionWebSearch.ActionSearch | ResponsesAPI.ActionOpenPage | ResponsesAPI.ActionFind;

    status: 'in_progress' | 'searching' | 'completed' | 'failed';

    type: 'web_search_call';

  [k: string]: unknown
  }

  export namespace ResponseFunctionWebSearch {
    /**
     * Action type "search" - Performs a web search query.
     */
    export interface ActionSearch {
      query: string;

      type: 'search';

      queries?: Array<string> | null;

      sources?: Array<ResponsesAPI.ActionSearchSource> | null;

    [k: string]: unknown
    }
  }

  /**
   * A tool call to a computer use tool.
   *
   * See the
   * [computer use guide](https://platform.openai.com/docs/guides/tools-computer-use)
   * for more information.
   */
  export interface ResponseComputerToolCall {
    id: string;

    /**
     * A click action.
     */
    action: ResponsesAPI.ActionClick | ResponsesAPI.ActionDoubleClick | ResponsesAPI.ActionDrag | ResponsesAPI.ActionKeypress | ResponsesAPI.ActionMove | ResponsesAPI.ActionScreenshot | ResponsesAPI.ActionScroll | ResponsesAPI.ActionType | ResponsesAPI.ActionWait | ResponseComputerToolCall.ActionPointAndType | ResponseComputerToolCall.ActionMouseDown | ResponseComputerToolCall.ActionMouseUp | ResponseComputerToolCall.ActionKeyDown | ResponseComputerToolCall.ActionKeyUp;

    call_id: string;

    pending_safety_checks: Array<ResponseComputerToolCall.PendingSafetyCheck>;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'computer_call';

  [k: string]: unknown
  }

  export namespace ResponseComputerToolCall {
    /**
     * Click at a position then type text.
     */
    export interface ActionPointAndType {
      text: string;

      type: 'point_and_type';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Press and hold the left mouse button at a position.
     */
    export interface ActionMouseDown {
      type: 'mouse_down';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Release the left mouse button at a position.
     */
    export interface ActionMouseUp {
      type: 'mouse_up';

      x: number;

      y: number;

    [k: string]: unknown
    }

    /**
     * Press and hold a key.
     */
    export interface ActionKeyDown {
      keys: Array<string>;

      type: 'key_down';

    [k: string]: unknown
    }

    /**
     * Release a held key.
     */
    export interface ActionKeyUp {
      keys: Array<string>;

      type: 'key_up';

    [k: string]: unknown
    }

    /**
     * A pending safety check for the computer call.
     */
    export interface PendingSafetyCheck {
      id: string;

      code?: string | null;

      message?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * A description of the chain of thought used by a reasoning model while generating
   * a response. Be sure to include these items in your `input` to the Responses API
   * for subsequent turns of a conversation if you are manually
   * [managing context](https://platform.openai.com/docs/guides/conversation-state).
   */
  export interface ResponseReasoningItem {
    id: string;

    summary: Array<ResponsesAPI.Summary>;

    type: 'reasoning';

    content?: Array<ResponseReasoningItem.Content> | null;

    encrypted_content?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | null;

  [k: string]: unknown
  }

  export namespace ResponseReasoningItem {
    /**
     * Reasoning text from the model.
     */
    export interface Content {
      text: string;

      type: 'reasoning_text';

    [k: string]: unknown
    }
  }

  /**
   * A compaction item generated by the
   * [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).
   */
  export interface ResponseCompactionItem {
    id: string;

    encrypted_content: string;

    type: 'compaction';

    created_by?: string | null;

  [k: string]: unknown
  }

  /**
   * An image generation request made by the model.
   */
  export interface ImageGenerationCall {
    id: string;

    status: 'in_progress' | 'completed' | 'generating' | 'failed';

    type: 'image_generation_call';

    result: string | null;
  }

  /**
   * A tool call to run code.
   */
  export interface ResponseCodeInterpreterToolCall {
    id: string;

    container_id: string;

    status: 'in_progress' | 'completed' | 'incomplete' | 'interpreting' | 'failed';

    type: 'code_interpreter_call';

    code?: string | null;

    outputs?: Array<ResponsesAPI.OutputLogs | ResponsesAPI.OutputImage> | null;

  [k: string]: unknown
  }

  /**
   * A tool call to run a command on the local shell.
   */
  export interface LocalShellCall {
    id: string;

    /**
     * Execute a shell command on the server.
     */
    action: LocalShellCall.Action;

    call_id: string;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'local_shell_call';
  }

  export namespace LocalShellCall {
    /**
     * Execute a shell command on the server.
     */
    export interface Action {
      command: Array<string>;

      env: { [key: string]: string };

      type: 'exec';

      timeout_ms?: number | null;

      user?: string | null;

      working_directory?: string | null;
    }
  }

  /**
   * A tool call that executes one or more shell commands in a managed environment.
   */
  export interface ResponseFunctionShellToolCall {
    id: string;

    /**
     * The shell commands and limits that describe how to run the tool call.
     */
    action: ResponseFunctionShellToolCall.Action;

    call_id: string;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'shell_call';

    created_by?: string | null;

  [k: string]: unknown
  }

  export namespace ResponseFunctionShellToolCall {
    /**
     * The shell commands and limits that describe how to run the tool call.
     */
    export interface Action {
      commands: Array<string>;

      max_output_length?: number | null;

      timeout_ms?: number | null;

    [k: string]: unknown
    }
  }

  /**
   * The output of a shell tool call that was emitted.
   */
  export interface ResponseFunctionShellToolCallOutput {
    id: string;

    call_id: string;

    output: Array<ResponseFunctionShellToolCallOutput.Output>;

    status: 'in_progress' | 'completed' | 'incomplete';

    type: 'shell_call_output';

    created_by?: string | null;

    max_output_length?: number | null;

  [k: string]: unknown
  }

  export namespace ResponseFunctionShellToolCallOutput {
    /**
     * The content of a shell tool call output that was emitted.
     */
    export interface Output {
      /**
       * Indicates that the shell call exceeded its configured time limit.
       */
      outcome: Output.OutputOutcomeTimeout | Output.OutputOutcomeExit;

      stderr: string;

      stdout: string;

      created_by?: string | null;

    [k: string]: unknown
    }

    export namespace Output {
      /**
       * Indicates that the shell call exceeded its configured time limit.
       */
      export interface OutputOutcomeTimeout {
        type: 'timeout';

      [k: string]: unknown
      }

      /**
       * Indicates that the shell commands finished and returned an exit code.
       */
      export interface OutputOutcomeExit {
        exit_code: number;

        type: 'exit';

      [k: string]: unknown
      }
    }
  }

  /**
   * A tool call that applies file diffs by creating, deleting, or updating files.
   */
  export interface ResponseApplyPatchToolCall {
    id: string;

    call_id: string;

    /**
     * Instruction describing how to create a file via the apply_patch tool.
     */
    operation: ResponseApplyPatchToolCall.OperationCreateFile | ResponseApplyPatchToolCall.OperationDeleteFile | ResponseApplyPatchToolCall.OperationUpdateFile;

    status: 'in_progress' | 'completed';

    type: 'apply_patch_call';

    created_by?: string | null;

  [k: string]: unknown
  }

  export namespace ResponseApplyPatchToolCall {
    /**
     * Instruction describing how to create a file via the apply_patch tool.
     */
    export interface OperationCreateFile {
      diff: string;

      path: string;

      type: 'create_file';

    [k: string]: unknown
    }

    /**
     * Instruction describing how to delete a file via the apply_patch tool.
     */
    export interface OperationDeleteFile {
      path: string;

      type: 'delete_file';

    [k: string]: unknown
    }

    /**
     * Instruction describing how to update a file via the apply_patch tool.
     */
    export interface OperationUpdateFile {
      diff: string;

      path: string;

      type: 'update_file';

    [k: string]: unknown
    }
  }

  /**
   * The output emitted by an apply patch tool call.
   */
  export interface ResponseApplyPatchToolCallOutput {
    id: string;

    call_id: string;

    status: 'completed' | 'failed';

    type: 'apply_patch_call_output';

    created_by?: string | null;

    output?: string | null;

  [k: string]: unknown
  }

  /**
   * An invocation of a tool on an MCP server.
   */
  export interface McpCall {
    id: string;

    arguments: string;

    name: string;

    server_label: string;

    type: 'mcp_call';

    approval_request_id?: string | null;

    error?: string | null;

    output?: string | null;

    status?: 'in_progress' | 'completed' | 'incomplete' | 'calling' | 'failed';
  }

  /**
   * A list of tools available on an MCP server.
   */
  export interface McpListTools {
    id: string;

    server_label: string;

    tools: Array<McpListTools.Tool>;

    type: 'mcp_list_tools';

    error?: string | null;
  }

  export namespace McpListTools {
    /**
     * A tool available on an MCP server.
     */
    export interface Tool {
      input_schema: unknown;

      name: string;

      annotations?: unknown;

      description?: string | null;
    }
  }

  /**
   * A call to a custom tool created by the model.
   */
  export interface ResponseCustomToolCall {
    call_id: string;

    input: string;

    name: string;

    type: 'custom_tool_call';

    id?: string | null;

  [k: string]: unknown
  }

  /**
   * Reference to a prompt template and its variables.
   * [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).
   */
  export interface Prompt {
    id: string;

    variables?: { [key: string]: string | Prompt.ResponseInputText | Prompt.ResponseInputImage | Prompt.ResponseInputFile } | null;

    version?: string | null;

  [k: string]: unknown
  }

  export namespace Prompt {
    /**
     * A text input to the model.
     */
    export interface ResponseInputText {
      text: string;

      type: 'input_text';

    [k: string]: unknown
    }

    /**
     * An image input to the model.
     *
     * Learn about [image inputs](https://platform.openai.com/docs/guides/vision).
     */
    export interface ResponseInputImage {
      detail: 'low' | 'high' | 'auto';

      type: 'input_image';

      file_id?: string | null;

      image_url?: string | null;

    [k: string]: unknown
    }

    /**
     * A file input to the model.
     */
    export interface ResponseInputFile {
      type: 'input_file';

      file_data?: string | null;

      file_id?: string | null;

      file_url?: string | null;

      filename?: string | null;

    [k: string]: unknown
    }
  }

  /**
   * **gpt-5 and o-series models only**
   *
   * Configuration options for
   * [reasoning models](https://platform.openai.com/docs/guides/reasoning).
   */
  export interface Reasoning {
    effort?: 'none' | 'minimal' | 'low' | 'medium' | 'high' | 'xhigh' | null;

    generate_summary?: 'auto' | 'concise' | 'detailed' | null;

    summary?: 'auto' | 'concise' | 'detailed' | null;

  [k: string]: unknown
  }

  /**
   * Configuration options for a text response from the model.
   *
   * Can be plain text or structured JSON data. Learn more:
   *
   * - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
   * - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
   */
  export interface Text {
    /**
     * Default response format. Used to generate text responses.
     */
    format?: Text.ResponseFormatText | Text.ResponseFormatTextJsonSchemaConfig | Text.ResponseFormatJsonObject | null;

    verbosity?: 'low' | 'medium' | 'high' | null;

  [k: string]: unknown
  }

  export namespace Text {
    /**
     * Default response format. Used to generate text responses.
     */
    export interface ResponseFormatText {
      type: 'text';

    [k: string]: unknown
    }

    /**
     * JSON Schema response format.
     *
     * Used to generate structured JSON responses. Learn more about
     * [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).
     */
    export interface ResponseFormatTextJsonSchemaConfig {
      name: string;

      schema: { [key: string]: unknown };

      type: 'json_schema';

      description?: string | null;

      strict?: boolean | null;

    [k: string]: unknown
    }

    /**
     * JSON object response format.
     *
     * An older method of generating JSON responses. Using `json_schema` is recommended
     * for models that support it. Note that the model will not generate JSON without a
     * system or user message instructing it to do so.
     */
    export interface ResponseFormatJsonObject {
      type: 'json_object';

    [k: string]: unknown
    }
  }

  /**
   * Constrains the tools available to the model to a pre-defined set.
   */
  export interface ToolChoiceAllowed {
    mode: 'auto' | 'required';

    tools: Array<{ [key: string]: unknown }>;

    type: 'allowed_tools';

  [k: string]: unknown
  }

  /**
   * Indicates that the model should use a built-in tool to generate a response.
   * [Learn more about built-in tools](https://platform.openai.com/docs/guides/tools).
   */
  export interface ToolChoiceTypes {
    type: 'computer_use_preview';

  [k: string]: unknown
  }

  /**
   * Use this option to force the model to call a specific function.
   */
  export interface ToolChoiceFunction {
    name: string;

    type: 'function';

  [k: string]: unknown
  }

  /**
   * Use this option to force the model to call a specific custom tool.
   */
  export interface ToolChoiceCustom {
    name: string;

    type: 'custom';

  [k: string]: unknown
  }

  /**
   * Defines a function in your own code the model can choose to call.
   *
   * Learn more about
   * [function calling](https://platform.openai.com/docs/guides/function-calling).
   */
  export interface FunctionTool {
    name: string;

    type: 'function';

    description?: string | null;

    parameters?: { [key: string]: unknown } | null;

    strict?: boolean | null;

  [k: string]: unknown
  }

  /**
   * A custom tool that processes input using a specified format.
   *
   * Learn more about
   * [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)
   */
  export interface CustomTool {
    name: string;

    type: 'custom';

    description?: string | null;

    /**
     * Unconstrained free-form text.
     */
    format?: CustomTool.Text | CustomTool.Grammar | null;

  [k: string]: unknown
  }

  export namespace CustomTool {
    /**
     * Unconstrained free-form text.
     */
    export interface Text {
      type: 'text';

    [k: string]: unknown
    }

    /**
     * A grammar defined by the user.
     */
    export interface Grammar {
      definition: string;

      syntax: 'lark' | 'regex';

      type: 'grammar';

    [k: string]: unknown
    }
  }

  /**
   * A tool that controls a virtual computer.
   *
   * Learn more about the
   * [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).
   */
  export interface ComputerTool {
    display_height: number;

    display_width: number;

    environment: 'windows' | 'mac' | 'linux' | 'ubuntu' | 'browser';

    type: 'computer_use_preview';

  [k: string]: unknown
  }
}

export interface ResponseRetrieveParams {
  starting_after?: number | null;

  stream?: boolean | null;
}

export declare namespace Responses {
  export {
    type ActionClick as ActionClick,
    type ActionDoubleClick as ActionDoubleClick,
    type ActionDrag as ActionDrag,
    type ActionFind as ActionFind,
    type ActionKeypress as ActionKeypress,
    type ActionMove as ActionMove,
    type ActionOpenPage as ActionOpenPage,
    type ActionScreenshot as ActionScreenshot,
    type ActionScroll as ActionScroll,
    type ActionSearchSource as ActionSearchSource,
    type ActionType as ActionType,
    type ActionWait as ActionWait,
    type AnnotationContainerFileCitation as AnnotationContainerFileCitation,
    type AnnotationFileCitation as AnnotationFileCitation,
    type AnnotationFilePath as AnnotationFilePath,
    type AnnotationURLCitation as AnnotationURLCitation,
    type Logprob as Logprob,
    type McpApprovalRequest as McpApprovalRequest,
    type OutputImage as OutputImage,
    type OutputLogs as OutputLogs,
    type ResponseInputFileParam as ResponseInputFileParam,
    type ResponseInputImageParam as ResponseInputImageParam,
    type ResponseInputTextParam as ResponseInputTextParam,
    type Summary as Summary,
    type ResponseCreateResponse as ResponseCreateResponse,
    type ResponseRetrieveResponse as ResponseRetrieveResponse,
    type ResponseCancelResponse as ResponseCancelResponse,
    type ResponseCreateParams as ResponseCreateParams,
    type ResponseRetrieveParams as ResponseRetrieveParams
  };
}
