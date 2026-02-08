"""Image processing utilities.

``process_image`` delegates to the native (Rust) extension for the full
decode-resize-encode-base64 pipeline in a single GIL-free call.  All other
helpers are pure Python — the FFI overhead would exceed their computation.
"""

from __future__ import annotations

import base64
from typing import Optional

try:
    from lightcone import _rust as _native
except Exception as exc:  # pragma: no cover
    raise RuntimeError(
        "Native extension is required. Build it with: "
        "uv run maturin develop -m native/Cargo.toml"
    ) from exc


# ---------------------------------------------------------------------------
# Native (Rust) — justified: heavy image pipeline in one GIL-free call
# ---------------------------------------------------------------------------


def process_image(image_bytes: bytes, factor: int = 32) -> tuple[str, int, int, int, int]:
    """Decode, smart-resize, PNG-encode, and base64-encode an image.

    Returns ``(base64_str, resized_w, resized_h, original_w, original_h)``.
    """
    return _native.process_image(image_bytes, factor)


# ---------------------------------------------------------------------------
# Pure Python — trivial operations, not worth crossing FFI boundary
# ---------------------------------------------------------------------------


def encode_image(image_bytes: bytes) -> str:
    """Base64-encode raw image bytes."""
    return base64.b64encode(image_bytes).decode("ascii")


def ensure_data_url(value: str, default_mime: str = "image/png") -> str:
    """Ensure *value* is a data-URL or HTTP(S) URL; prepend header if needed."""
    if not value:
        return value
    if value.startswith(("data:", "http://", "https://")):
        return value
    # Infer MIME from base64 prefix
    mime = default_mime
    if value.startswith("/9j/"):
        mime = "image/jpeg"
    elif value.startswith("iVBORw0K"):
        mime = "image/png"
    elif value.startswith("R0lGOD"):
        mime = "image/gif"
    return f"data:{mime};base64,{value}"


def decode_data_url(data_url: str) -> Optional[bytes]:
    """Extract raw bytes from a ``data:…;base64,…`` URL."""
    if not data_url.startswith("data:"):
        return None
    parts = data_url.split(",", 1)
    if len(parts) != 2:
        return None
    header, b64_data = parts
    if ";base64" not in header:
        return None
    try:
        return base64.b64decode(b64_data)
    except Exception:
        return None


def scale_coordinates(x: int, y: int, viewport_width: int, viewport_height: int) -> tuple[int, int]:
    """Scale normalised 0-999 model coordinates to actual viewport pixels."""
    x_scale = (viewport_width - 1) / 999.0 if viewport_width > 1 else 1.0
    y_scale = (viewport_height - 1) / 999.0 if viewport_height > 1 else 1.0
    return round(x * x_scale), round(y * y_scale)
