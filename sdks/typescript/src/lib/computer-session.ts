import type { Lightcone } from '../client';
import type {
  ActionResult,
  ComputerAction,
  ComputerBatchResponse,
  ComputerCreateParams,
  ComputerKeepaliveResponse,
  ComputerResponse,
} from '../resources/computers/computers';

export class ComputerSession {
  readonly id: string;
  private _client: Lightcone;
  width: number;
  height: number;

  constructor(client: Lightcone, id: string, width = 1024, height = 768) {
    this._client = client;
    this.id = id;
    this.width = width;
    this.height = height;
  }

  static async create(client: Lightcone, params: ComputerCreateParams = {}): Promise<ComputerSession> {
    const response = await client.computers.create(params);
    if (!response.id) throw new Error('Computer creation did not return an id');
    const width = params.display?.width ?? 1024;
    const height = params.display?.height ?? 768;
    return new ComputerSession(client, response.id, width, height);
  }

  // Navigation

  navigate(url: string): Promise<ActionResult> {
    return this._client.computers.navigate(this.id, { url });
  }

  // Mouse

  click(x: number, y: number): Promise<ActionResult> {
    return this._client.computers.click(this.id, { x, y });
  }

  doubleClick(x: number, y: number): Promise<ActionResult> {
    return this._client.computers.doubleClick(this.id, { x, y });
  }

  rightClick(x: number, y: number): Promise<ActionResult> {
    return this._client.computers.rightClick(this.id, { x, y });
  }

  drag(x1: number, y1: number, x2: number, y2: number): Promise<ActionResult> {
    return this._client.computers.drag(this.id, { x1, y1, x2, y2 });
  }

  mouseDown(x: number, y: number): Promise<ActionResult> {
    return this._client.computers.mouseDown(this.id, { x, y });
  }

  mouseUp(x: number, y: number): Promise<ActionResult> {
    return this._client.computers.mouseUp(this.id, { x, y });
  }

  // Keyboard

  type(text: string): Promise<ActionResult> {
    return this._client.computers.type(this.id, { text });
  }

  hotkey(...keys: string[]): Promise<ActionResult> {
    return this._client.computers.hotkey(this.id, { keys });
  }

  keyDown(key: string): Promise<ActionResult> {
    return this._client.computers.keyDown(this.id, { key });
  }

  keyUp(key: string): Promise<ActionResult> {
    return this._client.computers.keyUp(this.id, { key });
  }

  // Scrolling & viewport

  scroll(dx = 0, dy = 0, x = 0, y = 0): Promise<ActionResult> {
    return this._client.computers.scroll(this.id, { dx, dy, x, y });
  }

  async setViewport(width: number, height: number, scaleFactor = 1): Promise<ActionResult> {
    const result = await this._client.computers.viewport(this.id, { width, height, scale_factor: scaleFactor });
    this.width = width;
    this.height = height;
    return result;
  }

  // Content

  screenshot(base64 = false): Promise<ActionResult> {
    return this._client.computers.screenshot(this.id, { base64 });
  }

  html(autoDetectEncoding = false): Promise<ActionResult> {
    return this._client.computers.html(this.id, { auto_detect_encoding: autoDetectEncoding });
  }

  // Shell / debug

  debug(command: string, timeoutSeconds = 120, maxOutputLength = 65536): Promise<ActionResult> {
    return this._client.computers.debug(this.id, {
      command,
      timeout_seconds: timeoutSeconds,
      max_output_length: maxOutputLength,
    });
  }

  // Timing

  wait(seconds: number): Promise<ActionResult> {
    return this._client.computers.execute(this.id, {
      action: { type: 'wait', ms: Math.round(seconds * 1000) },
    });
  }

  // Generic / batch

  execute(action: ComputerAction): Promise<ActionResult> {
    return this._client.computers.execute(this.id, { action });
  }

  batch(actions: ComputerAction[]): Promise<ComputerBatchResponse> {
    return this._client.computers.batch(this.id, { actions });
  }

  // Session management

  keepAlive(): Promise<ComputerKeepaliveResponse> {
    return this._client.computers.keepalive(this.id);
  }

  retrieve(): Promise<ComputerResponse> {
    return this._client.computers.retrieve(this.id);
  }

  terminate(): Promise<void> {
    return this._client.computers.delete(this.id);
  }

  // Result helpers

  static getScreenshotUrl(result: ActionResult): string | undefined {
    return result.result?.['screenshot_url'] as string | undefined;
  }

  static getHtmlContent(result: ActionResult): string | undefined {
    return result.result?.['html_content'] as string | undefined;
  }

  static getDebugResponse(result: ActionResult): string | undefined {
    return result.result?.['debug_response'] as string | undefined;
  }
}
