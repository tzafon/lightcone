// File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import Lightcone from '@tzafon/lightcone';

const client = new Lightcone({
  apiKey: 'My API Key',
  baseURL: process.env['TEST_API_BASE_URL'] ?? 'http://127.0.0.1:4010',
});

describe('resource chat', () => {
  // Mock server tests are disabled
  test.skip('createCompletion: only required params', async () => {
    const responsePromise = client.chat.createCompletion({
      messages: [{ content: 'string', role: 'developer' }],
    });
    const rawResponse = await responsePromise.asResponse();
    expect(rawResponse).toBeInstanceOf(Response);
    const response = await responsePromise;
    expect(response).not.toBeInstanceOf(Response);
    const dataAndResponse = await responsePromise.withResponse();
    expect(dataAndResponse.data).toBe(response);
    expect(dataAndResponse.response).toBe(rawResponse);
  });

  // Mock server tests are disabled
  test.skip('createCompletion: required and optional params', async () => {
    const response = await client.chat.createCompletion({
      messages: [
        {
          content: 'string',
          role: 'developer',
          name: 'name',
        },
      ],
      add_generation_prompt: true,
      add_special_tokens: true,
      allowed_token_ids: [0],
      bad_words: ['string'],
      cache_salt: 'cache_salt',
      chat_template: 'chat_template',
      chat_template_kwargs: { foo: 'bar' },
      continue_final_message: true,
      documents: [{ foo: 'string' }],
      echo: true,
      frequency_penalty: 0,
      ignore_eos: true,
      include_reasoning: true,
      include_stop_str_in_output: true,
      kv_transfer_params: { foo: 'bar' },
      length_penalty: 0,
      logit_bias: { foo: 0 },
      logits_processors: ['string'],
      logprobs: true,
      max_completion_tokens: 0,
      max_tokens: 0,
      min_p: 0,
      min_tokens: 0,
      mm_processor_kwargs: { foo: 'bar' },
      model: 'model',
      n: 0,
      parallel_tool_calls: true,
      presence_penalty: 0,
      priority: 0,
      prompt_logprobs: 0,
      reasoning_effort: 'low',
      repetition_penalty: 0,
      request_id: 'request_id',
      response_format: {
        type: 'text',
        json_schema: {
          name: 'name',
          description: 'description',
          schema: { foo: 'bar' },
          strict: true,
        },
      },
      return_token_ids: true,
      return_tokens_as_token_ids: true,
      seed: -9007199254740991,
      skip_special_tokens: true,
      spaces_between_special_tokens: true,
      stop: 'string',
      stop_token_ids: [0],
      stream: true,
      stream_options: { continuous_usage_stats: true, include_usage: true },
      structured_outputs: {
        _backend: '_backend',
        _backend_was_auto: true,
        choice: ['string'],
        disable_additional_properties: true,
        disable_any_whitespace: true,
        disable_fallback: true,
        grammar: 'grammar',
        json: 'string',
        json_object: true,
        regex: 'regex',
        structural_tag: 'structural_tag',
        whitespace_pattern: 'whitespace_pattern',
      },
      temperature: 0,
      tool_choice: 'none',
      tools: [
        {
          function: {
            name: 'name',
            description: 'description',
            parameters: { foo: 'bar' },
          },
          type: 'function',
        },
      ],
      top_k: 0,
      top_logprobs: 0,
      top_p: 0,
      truncate_prompt_tokens: -1,
      use_beam_search: true,
      user: 'user',
      vllm_xargs: { foo: 'string' },
    });
  });
});
