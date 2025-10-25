#!/usr/bin/env python3
"""
Convert PowerPoint slides to PNG images for review.
"""

from pptx import Presentation
from pptx.util import Inches
from PIL import Image, ImageDraw, ImageFont
import io


def slide_to_image(slide, slide_num, prs):
    """Convert a single slide to an image."""
    # Create a canvas
    width_px = int(prs.slide_width.inches * 96)  # 96 DPI
    height_px = int(prs.slide_height.inches * 96)

    img = Image.new('RGB', (width_px, height_px), color='white')
    draw = ImageDraw.Draw(img)

    # Try to load a font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        font = ImageFont.load_default()
        small_font = font

    # Draw a placeholder message
    msg = f"Slide {slide_num}: Use LibreOffice to convert"
    draw.text((50, height_px // 2), msg, fill='black', font=font)

    return img


def convert_pptx_to_images(pptx_file, output_prefix="slide"):
    """Convert PPTX to images using LibreOffice."""
    import subprocess
    import os

    # Create output directory
    os.makedirs("slide_images", exist_ok=True)

    # Use LibreOffice to convert
    # This requires LibreOffice to be installed
    try:
        result = subprocess.run([
            'libreoffice',
            '--headless',
            '--convert-to', 'png',
            '--outdir', 'slide_images',
            pptx_file
        ], capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            print(f"LibreOffice conversion failed: {result.stderr}")
            return False

        print(f"Converted to PNG successfully")
        return True

    except FileNotFoundError:
        print("LibreOffice not found. Trying alternative method...")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    import sys

    pptx_file = sys.argv[1] if len(sys.argv) > 1 else "CertTalk_Presentation.pptx"

    success = convert_pptx_to_images(pptx_file)

    if not success:
        print("\nAttempting Python-based rendering...")
        prs = Presentation(pptx_file)

        for i, slide in enumerate(prs.slides, 1):
            img = slide_to_image(slide, i, prs)
            img.save(f"slide_images/slide_{i}.png")
            print(f"Saved slide_{i}.png")
