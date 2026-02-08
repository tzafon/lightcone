use std::io::Cursor;

use base64::{engine::general_purpose::STANDARD, Engine as _};
use image::imageops::FilterType;
use image::{DynamicImage, GenericImageView, ImageFormat};
use pyo3::prelude::*;

fn round_by_factor(number: u32, factor: u32) -> u32 {
    ((number as f64 / factor as f64).round() as u32) * factor
}

fn ceil_by_factor(number: u32, factor: u32) -> u32 {
    number.div_ceil(factor) * factor
}

fn floor_by_factor(number: u32, factor: u32) -> u32 {
    (number / factor) * factor
}

fn smart_resize(
    height: u32,
    width: u32,
    factor: u32,
    min_pixels: u64,
    max_pixels: u64,
    max_long_side: u32,
) -> Result<(u32, u32), String> {
    if height < 2 || width < 2 {
        return Err("height or width must be >= 2".into());
    }
    let max_dim = height.max(width) as f64;
    let min_dim = height.min(width) as f64;
    if max_dim / min_dim > 200.0 {
        return Err("absolute aspect ratio must be smaller than 200".into());
    }

    let mut height = height;
    let mut width = width;
    let max_long_side = max_long_side.max(1);
    if height.max(width) > max_long_side {
        let scale = height.max(width) as f64 / max_long_side as f64;
        height = ((height as f64) / scale) as u32;
        width = ((width as f64) / scale) as u32;
    }

    let mut h_bar = round_by_factor(height, factor);
    let mut w_bar = round_by_factor(width, factor);

    let pixels = (h_bar as u64) * (w_bar as u64);
    if pixels > max_pixels {
        let scale = ((height as f64 * width as f64) / max_pixels as f64).sqrt();
        h_bar = floor_by_factor(((height as f64) / scale) as u32, factor);
        w_bar = floor_by_factor(((width as f64) / scale) as u32, factor);
    } else if pixels < min_pixels {
        let scale = (min_pixels as f64 / (height as f64 * width as f64)).sqrt();
        h_bar = ceil_by_factor(((height as f64) * scale) as u32, factor);
        w_bar = ceil_by_factor(((width as f64) * scale) as u32, factor);
    }

    Ok((h_bar, w_bar))
}

fn resize_image(image: &DynamicImage, width: u32, height: u32) -> DynamicImage {
    image.resize_exact(width, height, FilterType::Triangle)
}

#[pyfunction]
pub fn process_image(image_bytes: &[u8], factor: u32) -> PyResult<(String, u32, u32, u32, u32)> {
    let image = image::load_from_memory(image_bytes)
        .map_err(|err| pyo3::exceptions::PyValueError::new_err(err.to_string()))?;
    let (original_width, original_height) = image.dimensions();
    let (resized_height, resized_width) = smart_resize(
        original_height,
        original_width,
        factor,
        56 * 56,
        16 * 16 * 4 * 12800,
        8192,
    )
    .map_err(|err| pyo3::exceptions::PyValueError::new_err(err))?;

    let resized = resize_image(&image, resized_width, resized_height);
    let mut buffer = Vec::new();
    resized
        .write_to(&mut Cursor::new(&mut buffer), ImageFormat::Png)
        .map_err(|err| pyo3::exceptions::PyValueError::new_err(err.to_string()))?;
    let b64 = STANDARD.encode(buffer);

    Ok((
        b64,
        resized_width,
        resized_height,
        original_width,
        original_height,
    ))
}
