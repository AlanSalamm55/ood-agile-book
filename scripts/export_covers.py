import os
import sys
from pathlib import Path
import win32com.client

def export_covers():
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    pptx_path = repo_root / "OOD_Agile_BookCover.pptx"
    if not pptx_path.exists():
        pptx_path = repo_root / "OOP_Agile_BookCover.pptx"

    if not pptx_path.exists():
        print(f"Error: {pptx_path} not found")
        sys.exit(1)

    print(f"Opening presentation: {pptx_path}")
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    try:
        # Open in read-only and without window
        pres = ppt.Presentations.Open(str(pptx_path), ReadOnly=True, Untitled=False, WithWindow=False)
        slide_count = pres.Slides.Count
        print(f"Total slides: {slide_count}")

        # Page setup dimensions
        page_width = pres.PageSetup.SlideWidth
        page_height = pres.PageSetup.SlideHeight
        print(f"Slide points: {page_width} x {page_height}")

        # High resolution A4 ratio (approx 300 DPI: 2480 x 3508)
        target_w = 2480
        target_h = 3508
        print(f"Export target resolution: {target_w} x {target_h}")

        static_images = repo_root / "static" / "images"
        assets_images = repo_root / "assets" / "images"
        root_images = repo_root / "images"
        scratch_dir = repo_root / "scratch"
        static_images.mkdir(parents=True, exist_ok=True)
        assets_images.mkdir(parents=True, exist_ok=True)
        root_images.mkdir(parents=True, exist_ok=True)
        scratch_dir.mkdir(parents=True, exist_ok=True)

        # Slide 1 -> front cover
        slide_front = pres.Slides(1)
        front_targets = [
            static_images / "front-image.png",
            static_images / "cover-front.png",
            assets_images / "front-image.png",
            root_images / "cover-front.png",
            scratch_dir / "slide_1.png",
        ]
        for t in front_targets:
            slide_front.Export(str(t), "PNG", target_w, target_h)
        print(f"Exported Slide 1 to front-image.png and cover-front.png across static, assets, images, and scratch")

        # Slide last -> back cover
        slide_back = pres.Slides(slide_count)
        back_targets = [
            static_images / "back-image.png",
            static_images / "cover-back.png",
            assets_images / "cover-back.png",
            root_images / "cover-back.png",
            scratch_dir / "slide_2.png",
        ]
        for t in back_targets:
            slide_back.Export(str(t), "PNG", target_w, target_h)
        print(f"Exported Slide {slide_count} to back-image.png and cover-back.png across static, assets, images, and scratch")

        pres.Close()
    finally:
        ppt.Quit()

if __name__ == "__main__":
    export_covers()
