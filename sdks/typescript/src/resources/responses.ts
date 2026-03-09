// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import * as ResponsesAPI from './responses';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';
import { path } from '../internal/utils/path';

export class Responses extends APIResource {
  /**
   * Create a model response. Supports text conversations and computer-use (CUA)
   * workflows. Set stream=true for server-sent events. Include tools with type
   * "computer_use" for CUA mode, which returns structured computer_call actions. Use
   * previous_response_id to chain multi-turn conversations.
   */
  create(body: ResponseCreateParams, options?: RequestOptions): APIPromise<ResponsesResponse> {
    return this._client.post('/v1/responses', { body, ...options });
  }

  /**
   * Retrieve a previously created response by its ID, including all output items.
   */
  retrieve(id: string, options?: RequestOptions): APIPromise<ResponsesResponse> {
    return this._client.get(path`/v1/responses/${id}`, options);
  }

  /**
   * Permanently delete a response and all its output items.
   */
  delete(id: string, options?: RequestOptions): APIPromise<ResponseDeleteResponse> {
    return this._client.delete(path`/v1/responses/${id}`, options);
  }

  /**
   * Cancel an in-progress response. Only responses with status "in_progress" can be
   * cancelled.
   */
  cancel(id: string, options?: RequestOptions): APIPromise<ResponsesResponse> {
    return this._client.post(path`/v1/responses/${id}/cancel`, options);
  }
}

export interface ContentBlock {
  image_url?: string;

  text?: string;

  type?: 'input_text' | 'output_text' | 'summary_text' | 'input_image';
}

export interface ResponsesResponse {
  id?: string;

  computer_id?: string;

  created_at?: string;

  max_output_tokens?: number;

  model?: string;

  object?: string;

  output?: Array<V2GoBackendInternalServiceOutputItem>;

  status?: string;

  temperature?: number;

  top_p?: number;

  usage?: V2GoBackendInternalServiceResponsesUsage;

  viewport?: V2GoBackendInternalServiceViewport;
}

export interface V2GoBackendInternalServiceAction {
  button?: string;

  end_x?: number;

  end_y?: number;

  keys?: Array<string>;

  result?: string;

  scroll_x?: number;

  scroll_y?: number;

  status?: string;

  text?: string;

  type?:
    | 'click'
    | 'double_click'
    | 'triple_click'
    | 'right_click'
    | 'type'
    | 'key'
    | 'keypress'
    | 'key_down'
    | 'key_up'
    | 'scroll'
    | 'hscroll'
    | 'navigate'
    | 'drag'
    | 'wait'
    | 'terminate'
    | 'answer'
    | 'done';

  url?: string;

  x?: number;

  y?: number;
}

export interface V2GoBackendInternalServiceOutputItem {
  id?: string;

  action?: V2GoBackendInternalServiceAction;

  call_id?: string;

  content?: Array<ContentBlock>;

  role?: string;

  status?: string;

  summary?: Array<ContentBlock>;

  type?: 'reasoning' | 'computer_call' | 'computer_call_output' | 'message';
}

export interface V2GoBackendInternalServiceResponsesUsage {
  input_tokens?: number;

  output_tokens?: number;

  total_tokens?: number;
}

export interface V2GoBackendInternalServiceViewport {
  environment?: string;

  height?: number;

  width?: number;
}

export interface ResponseDeleteResponse {
  id?: string;

  deleted?: boolean;

  object?: string;
}

export interface ResponseCreateParams {
  input?: Array<ResponseCreateParams.Input>;

  instructions?: string;

  max_output_tokens?: number;

  model?: string;

  previous_response_id?: string;

  stream?: boolean;

  temperature?: number;

  tools?: Array<ResponseCreateParams.Tool>;

  top_p?: number;
}

export namespace ResponseCreateParams {
  export interface Input {
    call_id?: string;

    content?: Array<ResponsesAPI.ContentBlock>;

    output?: ResponsesAPI.ContentBlock;

    role?: string;

    type?: 'computer_call_output';
  }

  export interface Tool {
    display_height?: number;

    display_width?: number;

    environment?: string;

    type?: 'computer_use';
  }
}

export declare namespace Responses {
  export {
    type ContentBlock as ContentBlock,
    type ResponsesResponse as ResponsesResponse,
    type V2GoBackendInternalServiceAction as V2GoBackendInternalServiceAction,
    type V2GoBackendInternalServiceOutputItem as V2GoBackendInternalServiceOutputItem,
    type V2GoBackendInternalServiceResponsesUsage as V2GoBackendInternalServiceResponsesUsage,
    type V2GoBackendInternalServiceViewport as V2GoBackendInternalServiceViewport,
    type ResponseDeleteResponse as ResponseDeleteResponse,
    type ResponseCreateParams as ResponseCreateParams,
  };
}
