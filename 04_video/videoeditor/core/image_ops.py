"""Image operations: create video from images."""
from pathlib import Path
from PIL import Image
import numpy as np
from moviepy import ImageSequenceClip


def images_to_video(
    image_folder: str,
    output_path: str,
    fps: int = 24,
    seconds_per_image: float = 1.0,
    codec: str = "libx264",
) -> str:
    """Create video from sequence of images.

    Args:
        image_folder: Folder containing images
        output_path: Path to output video
        fps: Output frames per second
        seconds_per_image: How long each image displays
        codec: Video codec
    """
    folder = Path(image_folder)
    if not folder.exists():
        raise FileNotFoundError(f"Image folder not found: {image_folder}")

    # Find all images
    extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    images = [
        f for f in folder.iterdir()
        if f.suffix.lower() in extensions
    ]

    if not images:
        raise ValueError(f"No images found in {image_folder}")

    images.sort(key=lambda x: x.name)

    # Process images to same size
    first_img = Image.open(images[0])
    target_size = first_img.size
    resized_images = []

    for img_path in images:
        img = Image.open(img_path).convert("RGB")
        if img.size != target_size:
            img = img.resize(target_size)
        resized_images.append(np.array(img))

    # Create video
    durations = [seconds_per_image] * len(resized_images)
    clip = ImageSequenceClip(resized_images, durations=durations)
    clip.write_videofile(
        output_path,
        fps=fps,
        codec=codec,
        audio=False
    )

    return f"Video created: {output_path}"
