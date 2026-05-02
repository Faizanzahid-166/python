"""File and path validation utilities."""
from pathlib import Path


def validate_file(path: str, file_type: str = "file") -> Path:
    """Validate that a file or directory exists.

    Args:
        path: Path to validate
        file_type: 'file' or 'dir'

    Returns:
        Path object

    Raises:
        FileNotFoundError: If path doesn't exist
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{file_type.title()} not found: {path}")
    return p


def validate_video(path: str) -> Path:
    """Validate video file exists and has video extension."""
    video_extensions = {".mp4", ".avi", ".mkv", ".mov", ".webm", ".flv"}
    p = validate_file(path, "file")
    if p.suffix.lower() not in video_extensions:
        raise ValueError(f"Not a video file: {path}")
    return p


def validate_audio(path: str) -> Path:
    """Validate audio file exists and has audio extension."""
    audio_extensions = {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"}
    p = validate_file(path, "file")
    if p.suffix.lower() not in audio_extensions:
        raise ValueError(f"Not an audio file: {path}")
    return p


def validate_image(path: str) -> Path:
    """Validate image file exists and has image extension."""
    image_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp"}
    p = validate_file(path, "file")
    if p.suffix.lower() not in image_extensions:
        raise ValueError(f"Not an image file: {path}")
    return p
