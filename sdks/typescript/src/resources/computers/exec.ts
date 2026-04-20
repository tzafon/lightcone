// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import { APIPromise } from '../../core/api-promise';
import { buildHeaders } from '../../internal/headers';
import { RequestOptions } from '../../internal/request-options';
import { JSONLDecoder } from '../../internal/decoders/jsonl';
import { path } from '../../internal/utils/path';

export class Exec extends APIResource {
  /**
   * Execute a shell command (desktop sessions only) and stream output back as
   * newline-delimited JSON. Each line is a `types.ExecOutput` object whose `type` is
   * one of `stdout`, `stderr`, `exit`, or `error`. The stream terminates with a
   * single `{"type":"exit","code":<int>}` line; code `-1` indicates timeout or
   * abnormal termination.
   *
   * **Error model:** this endpoint always returns HTTP 200 and reports failures
   * (invalid JSON body, missing command, stream-setup failure) as a single
   * `{"type":"error","code":"<CODE>","message":"..."}` NDJSON line followed by
   * connection close. Clients MUST parse the first line rather than relying on HTTP
   * status codes.
   *
   * Output is filtered server-side by request ID, so concurrent `/exec` calls on the
   * same computer don't interleave. Defaults: `cwd=/workspace`,
   * `timeout_seconds=120`.
   *
   * @example
   * ```ts
   * const exec = await client.computers.exec.create('id');
   * ```
   */
  create(
    id: string,
    body: ExecCreateParams,
    options?: RequestOptions,
  ): APIPromise<JSONLDecoder<ExecCreateResponse>> {
    return this._client
      .post(path`/computers/${id}/exec`, {
        body,
        ...options,
        headers: buildHeaders([{ Accept: 'application/x-ndjson' }, options?.headers]),
        stream: true,
        __binaryResponse: true,
      })
      ._thenUnwrap((_, props) => JSONLDecoder.fromResponse(props.response, props.controller)) as APIPromise<
      JSONLDecoder<ExecCreateResponse>
    >;
  }

  /**
   * Execute a shell command and wait for completion, returning buffered
   * stdout/stderr.
   *
   * @example
   * ```ts
   * const response = await client.computers.exec.sync('id');
   * ```
   */
  sync(id: string, body: ExecSyncParams, options?: RequestOptions): APIPromise<ExecSyncResponse> {
    return this._client.post(path`/computers/${id}/exec/sync`, { body, ...options });
  }
}

export interface ExecCreateResponse {
  /**
   * for exit
   */
  code?: number;

  /**
   * for stdout/stderr
   */
  data?: string;

  /**
   * for error
   */
  message?: string;

  /**
   * "stdout", "stderr", "exit", "error"
   */
  type?: string;
}

export interface ExecSyncResponse {
  exit_code?: number;

  stderr?: string;

  stdout?: string;
}

export interface ExecCreateParams {
  command?: string;

  cwd?: string;

  env?: { [key: string]: string };

  timeout_seconds?: number;
}

export interface ExecSyncParams {
  command?: string;

  cwd?: string;

  env?: { [key: string]: string };

  timeout_seconds?: number;
}

export declare namespace Exec {
  export {
    type ExecCreateResponse as ExecCreateResponse,
    type ExecSyncResponse as ExecSyncResponse,
    type ExecCreateParams as ExecCreateParams,
    type ExecSyncParams as ExecSyncParams,
  };
}
