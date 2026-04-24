// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import { APIResource } from '../../core/resource';
import * as TasksAPI from './tasks';
import { TaskInjectMessageParams, TaskInjectMessageResponse, TaskPauseResponse, TaskResumeResponse, TaskRetrieveStatusResponse, TaskStartParams, TaskStartResponse, TaskStartStreamParams, TaskStartStreamResponse, Tasks } from './tasks';

export class Agent extends APIResource {
  tasks: TasksAPI.Tasks = new TasksAPI.Tasks(this._client);
}

Agent.Tasks = Tasks;

export declare namespace Agent {
  export {
    Tasks as Tasks,
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
