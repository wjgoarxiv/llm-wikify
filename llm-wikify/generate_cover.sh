#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_PATH="$SCRIPT_DIR/cover.png"

python3 - "$OUT_PATH" <<'PY'
from __future__ import annotations

import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

out_path = sys.argv[1]

W, H = 2560, 1280
DPI = 400
CORNER_RADIUS = 80

BASE = (12, 14, 20)
BLOBS = [
    (28, 92, 196, 190, 620, 520, 680, 460, 130),
    (70, 32, 168, 170, 1820, 250, 620, 420, 110),
    (0, 148, 122, 135, 1420, 980, 760, 320, 95),
    (86, 214, 255, 80, 2050, 720, 420, 250, 90),
]

TITLE_TEXT = "llm-wikify"
SUBTITLE_TEXT = "Local wiki maintenance for the directory you are actually working in."


def find_font(candidates: list[str], size: int):
    search_paths = [
        "/System/Library/Fonts/",
        "/Library/Fonts/",
        os.path.expanduser("~/Library/Fonts/"),
        "/usr/share/fonts/truetype/",
        "/usr/share/fonts/",
    ]
    for name in candidates:
        if os.path.isabs(name) and os.path.exists(name):
            try:
                return ImageFont.truetype(name, size), name
            except OSError:
                pass
        for path in search_paths:
            for ext in (".ttf", ".otf", ".ttc"):
                full = os.path.join(path, name + ext)
                if os.path.exists(full):
                    try:
                        return ImageFont.truetype(full, size), full
                    except OSError:
                        pass
        try:
            return ImageFont.truetype(name, size), name
        except OSError:
            pass
    return ImageFont.load_default(), "PIL-default-font"


def create_blob(size, rgba, cx, cy, rx, ry, blur_radius):
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=rgba)
    return layer.filter(ImageFilter.GaussianBlur(radius=blur_radius))


def add_film_grain(img: Image.Image, opacity: float = 0.14) -> Image.Image:
    arr = np.array(img).astype(np.float32)
    noise = np.random.default_rng(42).normal(128, 26, (H, W)).clip(0, 255)
    noise_rgba = np.stack([noise, noise, noise, np.full((H, W), 255)], axis=-1)
    blended = arr * (1 - opacity) + noise_rgba * opacity
    return Image.fromarray(blended.clip(0, 255).astype(np.uint8), "RGBA")


def draw_centered_glow_text(img, text, y, font, color, glow_color, glow_layers, blur_step):
    measure = ImageDraw.Draw(img)
    bbox = measure.textbbox((0, 0), text, font=font)
    x = (img.width - (bbox[2] - bbox[0])) // 2 - bbox[0]

    for i in range(glow_layers, 0, -1):
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)
        draw.text((x, y), text, font=font, fill=(*glow_color, 32 * i))
        layer = layer.filter(ImageFilter.GaussianBlur(radius=blur_step * i))
        img = Image.alpha_composite(img, layer)

    final = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(final).text((x, y), text, font=font, fill=color)
    return Image.alpha_composite(img, final)


def apply_rounded_corners(img, radius=CORNER_RADIUS):
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, img.width - 1, img.height - 1], radius=radius, fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, mask=mask)
    return out


img = Image.new("RGBA", (W, H), (*BASE, 255))
for r, g, b, a, cx, cy, rx, ry, blur in BLOBS:
    img = Image.alpha_composite(img, create_blob((W, H), (r, g, b, a), cx, cy, rx, ry, blur))

img = img.filter(ImageFilter.GaussianBlur(radius=8))
img = add_film_grain(img, opacity=0.14)

title_font, title_font_name = find_font([
    os.path.expanduser("~/Library/Fonts/JetBrainsMonoNerdFont-Bold.ttf"),
    os.path.expanduser("~/Library/Fonts/JetBrainsMonoNerdFontPropo-Bold.ttf"),
    os.path.expanduser("~/Library/Fonts/JetBrainsMonoNerdFontMono-Bold.ttf"),
    "JetBrainsMonoNerdFont-Bold",
    "JetBrainsMonoNerdFontPropo-Bold",
    "JetBrainsMonoNerdFontMono-Bold",
    "SFMono-Bold",
    "JetBrainsMono-Bold",
    "FiraCode-Bold",
    "Menlo-Bold",
    "Monaco",
], 190)
subtitle_font, subtitle_font_name = find_font([
    os.path.expanduser("~/Library/Fonts/JetBrainsMonoNerdFont-Regular.ttf"),
    os.path.expanduser("~/Library/Fonts/JetBrainsMonoNerdFontPropo-Regular.ttf"),
    os.path.expanduser("~/Library/Fonts/JetBrainsMonoNerdFontMono-Regular.ttf"),
    "JetBrainsMonoNerdFont-Regular",
    "JetBrainsMonoNerdFontPropo-Regular",
    "JetBrainsMonoNerdFontMono-Regular",
    "SFMono-Regular",
    "JetBrainsMono-Regular",
    "FiraCode-Regular",
    "Menlo",
    "Monaco",
], 52)

img = draw_centered_glow_text(
    img,
    TITLE_TEXT,
    H // 2 - 170,
    title_font,
    (247, 250, 255, 250),
    (110, 198, 255),
    3,
    8,
)
img = draw_centered_glow_text(
    img,
    SUBTITLE_TEXT,
    H // 2 + 85,
    subtitle_font,
    (186, 196, 214, 220),
    (90, 120, 180),
    2,
    6,
)

img = apply_rounded_corners(img)
img = img.filter(ImageFilter.GaussianBlur(radius=1))
img.save(out_path, "PNG", dpi=(DPI, DPI))
print(f"Title font: {title_font_name}")
print(f"Subtitle font: {subtitle_font_name}")
print(f"Cover saved to {out_path} ({W}x{H} @ {DPI} DPI)")
PY
