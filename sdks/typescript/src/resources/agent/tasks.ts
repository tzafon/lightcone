// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { Stream } from '../../core/streaming';
import { buildHeaders } from '../../internal/headers';
import { RequestOptions } from '../../internal/request-options';
import { path } from '../../internal/utils/path';

export class Tasks extends APIResource {
  /**
   * Injects a message into a running agent task.
   */
  injectMessage(id: string, body: TaskInjectMessageParams, options?: RequestOptions): APIPromise<TaskInjectMessageResponse> {
    return this._client.post(path`/agent/tasks/${id}/messages`, { body, ...options });
  }

  /**
   * Pauses a running agent task.
   */
  pause(id: string, options?: RequestOptions): APIPromise<TaskPauseResponse> {
    return this._client.post(path`/agent/tasks/${id}/pause`, options);
  }

  /**
   * Resumes a paused agent task.
   */
  resume(id: string, options?: RequestOptions): APIPromise<TaskResumeResponse> {
    return this._client.post(path`/agent/tasks/${id}/resume`, options);
  }

  /**
   * Returns the current status/result for a task.
   */
  retrieveStatus(id: string, options?: RequestOptions): APIPromise<TaskRetrieveStatusResponse> {
    return this._client.get(path`/agent/tasks/${id}`, options);
  }

  /**
   * Starts an agent task and returns a task_id immediately.
   */
  start(body: TaskStartParams, options?: RequestOptions): APIPromise<TaskStartResponse> {
    return this._client.post('/agent/tasks', { body, ...options });
  }

  /**
   * Starts an agent task and streams events via SSE (Content-Type:
   * text/event-stream).
   */
  startStream(body: TaskStartStreamParams, options?: RequestOptions): APIPromise<Stream<TaskStartStreamResponse>> {
    return this._client.post('/agent/tasks/stream', { body, ...options, headers: buildHeaders([{Accept: 'text/event-stream'}, options?.headers]), stream: true }) as APIPromise<Stream<TaskStartStreamResponse>>;
  }
}

export interface TaskInjectMessageResponse {
  status?: string;
}

export interface TaskPauseResponse {
  status?: string;
}

export interface TaskResumeResponse {
  status?: string;
}

export interface TaskRetrieveStatusResponse {
  exit_code?: number;

  status?: string;

  task_id?: string;
}

export interface TaskStartResponse {
  status?: string;

  task_id?: string;
}

export type TaskStartStreamResponse = string

export interface TaskInjectMessageParams {
  message?: string;
}

export interface TaskStartParams {
  agent_type?: string;

  environment_id?: string;

  instruction?: string;

  kind?: 'desktop' | 'browser';

  max_steps?: number;

  model?: string;

  persistent?: boolean;

  screenshot_mode?: 'url' | 'base64';

  temperature?: number;

  viewport_height?: number;

  viewport_width?: number;
}

export interface TaskStartStreamParams {
  agent_type?: string;

  environment_id?: string;

  instruction?: string;

  kind?: 'desktop' | 'browser';

  max_steps?: number;

  model?: string;

  persistent?: boolean;

  screenshot_mode?: 'url' | 'base64';

  temperature?: number;

  viewport_height?: number;

  viewport_width?: number;
}

export declare namespace Tasks {
  export {
    type TaskInjectMessageResponse as TaskInjectMessageResponse,
    type TaskPauseResponse as TaskPauseResponse,
    type TaskResumeResponse as TaskResumeResponse,
    type TaskRetrieveStatusResponse as TaskRetrieveStatusResponse,
    type TaskStartResponse as TaskStartResponse,
    type TaskStartStreamResponse as TaskStartStreamResponse,
    type TaskInjectMessageParams as TaskInjectMessageParams,
    type TaskStartParams as TaskStartParams,
    type TaskStartStreamParams as TaskStartStreamParams
  };
}
