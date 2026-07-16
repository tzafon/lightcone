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
  injectMessage(
    id: string,
    body: TaskInjectMessageParams,
    options?: RequestOptions,
  ): APIPromise<TaskInjectMessageResponse> {
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
  startStream(
    body: TaskStartStreamParams,
    options?: RequestOptions,
  ): APIPromise<Stream<TaskStartStreamResponse>> {
    return this._client.post('/agent/tasks/stream', {
      body,
      ...options,
      headers: buildHeaders([{ Accept: 'text/event-stream' }, options?.headers]),
      stream: true,
    }) as APIPromise<Stream<TaskStartStreamResponse>>;
  }
}

export interface TaskInjectMessageResponse {
  status: string;
}

export interface TaskPauseResponse {
  status: string;
}

export interface TaskResumeResponse {
  status: string;
}

export interface TaskRetrieveStatusResponse {
  status: string;

  task_id: string;

  exit_code?: number;
}

export interface TaskStartResponse {
  status: string;

  task_id: string;

  idempotency_key?: string;

  reused?: boolean;
}

export type TaskStartStreamResponse = string;

export interface TaskInjectMessageParams {
  message: string;
}

export interface TaskStartParams {
  /**
   * Instruction is the task prompt for the agent.
   */
  instruction: string;

  /**
   * AgentIcon is optional client metadata used by task history UIs. It is captured
   * by go-backend before proxying and ignored by older agent servers.
   */
  agent_icon?: string;

  /**
   * AgentType is accepted for legacy clients. Current agent servers ignore it.
   */
  agent_type?: string;

  /**
   * ComputerID reuses a live computer session, or restores a saved persistent
   * session with the same ID if it is not currently live.
   */
  computer_id?: string;

  /**
   * Context seeds the worker transcript with recent conversation turns, oldest
   * first.
   */
  context?: Array<TaskStartParams.Context>;

  /**
   * EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
   * with the saved computer/session ID for new integrations.
   */
  environment_id?: string;

  /**
   * HarnessVersion selects which agent harness implementation runs the task. "v1" is
   * the stable/core harness with broader shell/search tools. "v2" is the
   * training-aligned GUI harness.
   */
  harness_version?: 'v1' | 'v2';

  /**
   * IdempotencyKey deduplicates retried task start requests.
   */
  idempotency_key?: string;

  /**
   * KeepAlive is a user-friendly alias for terminate_on_completion=false.
   */
  keep_alive?: boolean;

  /**
   * Kind selects the virtual environment type. Omit to use the agent default:
   * browser when start_url is set, otherwise desktop. Saved computer_id sessions
   * restore using the stored session kind.
   */
  kind?: 'desktop' | 'browser';

  /**
   * MaxDurationSeconds caps wall-clock runtime before the server cancels the task.
   */
  max_duration_seconds?: number;

  /**
   * MaxSteps caps how many agent loop steps can run before max-steps termination.
   */
  max_steps?: number;

  /**
   * Metadata is customer-defined task metadata for correlating with external
   * workflows.
   */
  metadata?: { [key: string]: string };

  /**
   * Model is the LLM model to use. Omit to use the agent server default.
   */
  model?: string;

  /**
   * OnMissingComputer controls fallback when ComputerID is not live: "restore"
   * (default) restores a saved persistent session or returns 404, "fail" always
   * returns 404, "create_new" restores when possible and otherwise creates a fresh
   * computer.
   */
  on_missing_computer?: 'fail' | 'restore' | 'create_new';

  /**
   * Persistent controls whether the computer session should persist state on
   * teardown.
   */
  persistent?: boolean;

  /**
   * SaveSession is a user-friendly alias for Persistent.
   */
  save_session?: boolean;

  /**
   * ScreenshotMode controls whether task screenshots are emitted as URLs or base64
   * data URLs.
   */
  screenshot_mode?: 'url' | 'base64';

  /**
   * StartURL opens this URL before the agent starts. Omitted kind defaults to
   * browser.
   */
  start_url?: string;

  /**
   * StreamDeltas streams per-token text deltas as progress_update events when
   * supported.
   */
  stream_deltas?: boolean;

  /**
   * StreamMode controls event verbosity. "verbose" emits all events; "concise" emits
   * product-facing progress, screenshots, completion, and errors.
   */
  stream_mode?: 'verbose' | 'concise';

  /**
   * SystemPrompt is appended to the harness system message.
   */
  system_prompt?: string;

  /**
   * Temperature controls LLM sampling temperature. Omit to use the harness default.
   */
  temperature?: number;

  /**
   * TerminateOnCompletion controls whether the task should terminate its computer
   * automatically. Set false to keep the computer alive for handoff or inspection.
   */
  terminate_on_completion?: boolean;

  /**
   * ThreadID is optional client metadata for grouping task history by chat thread.
   * It is captured by go-backend before proxying and ignored by older agent servers.
   */
  thread_id?: string;

  /**
   * ViewportHeight is the browser viewport height in pixels.
   */
  viewport_height?: number;

  /**
   * ViewportWidth is the browser viewport width in pixels.
   */
  viewport_width?: number;
}

export namespace TaskStartParams {
  export interface Context {
    /**
     * Content is the text of this prior conversation turn.
     */
    content: string;

    /**
     * Role is the speaker for this prior conversation turn.
     */
    role: 'user' | 'assistant';
  }
}

export interface TaskStartStreamParams {
  /**
   * Instruction is the task prompt for the agent.
   */
  instruction: string;

  /**
   * AgentIcon is optional client metadata used by task history UIs. It is captured
   * by go-backend before proxying and ignored by older agent servers.
   */
  agent_icon?: string;

  /**
   * AgentType is accepted for legacy clients. Current agent servers ignore it.
   */
  agent_type?: string;

  /**
   * ComputerID reuses a live computer session, or restores a saved persistent
   * session with the same ID if it is not currently live.
   */
  computer_id?: string;

  /**
   * Context seeds the worker transcript with recent conversation turns, oldest
   * first.
   */
  context?: Array<TaskStartStreamParams.Context>;

  /**
   * EnvironmentID restores a previous persistent session snapshot. Prefer ComputerID
   * with the saved computer/session ID for new integrations.
   */
  environment_id?: string;

  /**
   * HarnessVersion selects which agent harness implementation runs the task. "v1" is
   * the stable/core harness with broader shell/search tools. "v2" is the
   * training-aligned GUI harness.
   */
  harness_version?: 'v1' | 'v2';

  /**
   * IdempotencyKey deduplicates retried task start requests.
   */
  idempotency_key?: string;

  /**
   * KeepAlive is a user-friendly alias for terminate_on_completion=false.
   */
  keep_alive?: boolean;

  /**
   * Kind selects the virtual environment type. Omit to use the agent default:
   * browser when start_url is set, otherwise desktop. Saved computer_id sessions
   * restore using the stored session kind.
   */
  kind?: 'desktop' | 'browser';

  /**
   * MaxDurationSeconds caps wall-clock runtime before the server cancels the task.
   */
  max_duration_seconds?: number;

  /**
   * MaxSteps caps how many agent loop steps can run before max-steps termination.
   */
  max_steps?: number;

  /**
   * Metadata is customer-defined task metadata for correlating with external
   * workflows.
   */
  metadata?: { [key: string]: string };

  /**
   * Model is the LLM model to use. Omit to use the agent server default.
   */
  model?: string;

  /**
   * OnMissingComputer controls fallback when ComputerID is not live: "restore"
   * (default) restores a saved persistent session or returns 404, "fail" always
   * returns 404, "create_new" restores when possible and otherwise creates a fresh
   * computer.
   */
  on_missing_computer?: 'fail' | 'restore' | 'create_new';

  /**
   * Persistent controls whether the computer session should persist state on
   * teardown.
   */
  persistent?: boolean;

  /**
   * SaveSession is a user-friendly alias for Persistent.
   */
  save_session?: boolean;

  /**
   * ScreenshotMode controls whether task screenshots are emitted as URLs or base64
   * data URLs.
   */
  screenshot_mode?: 'url' | 'base64';

  /**
   * StartURL opens this URL before the agent starts. Omitted kind defaults to
   * browser.
   */
  start_url?: string;

  /**
   * StreamDeltas streams per-token text deltas as progress_update events when
   * supported.
   */
  stream_deltas?: boolean;

  /**
   * StreamMode controls event verbosity. "verbose" emits all events; "concise" emits
   * product-facing progress, screenshots, completion, and errors.
   */
  stream_mode?: 'verbose' | 'concise';

  /**
   * SystemPrompt is appended to the harness system message.
   */
  system_prompt?: string;

  /**
   * Temperature controls LLM sampling temperature. Omit to use the harness default.
   */
  temperature?: number;

  /**
   * TerminateOnCompletion controls whether the task should terminate its computer
   * automatically. Set false to keep the computer alive for handoff or inspection.
   */
  terminate_on_completion?: boolean;

  /**
   * ThreadID is optional client metadata for grouping task history by chat thread.
   * It is captured by go-backend before proxying and ignored by older agent servers.
   */
  thread_id?: string;

  /**
   * ViewportHeight is the browser viewport height in pixels.
   */
  viewport_height?: number;

  /**
   * ViewportWidth is the browser viewport width in pixels.
   */
  viewport_width?: number;
}

export namespace TaskStartStreamParams {
  export interface Context {
    /**
     * Content is the text of this prior conversation turn.
     */
    content: string;

    /**
     * Role is the speaker for this prior conversation turn.
     */
    role: 'user' | 'assistant';
  }
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
    type TaskStartStreamParams as TaskStartStreamParams,
  };
}
