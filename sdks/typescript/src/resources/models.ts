// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../core/resource';
import { APIPromise } from '../core/api-promise';
import { RequestOptions } from '../internal/request-options';

export class Models extends APIResource {
  /**
   * Show Available Models
   */
  list(options?: RequestOptions): APIPromise<unknown> {
    return this._client.get('/v1/models', options);
  }
}

export type ModelListResponse = unknown

export declare namespace Models {
  export {
    type ModelListResponse as ModelListResponse
  };
}
