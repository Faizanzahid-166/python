"""Video operations: trim, merge, cut."""
import subprocess
from pathlib import Path
from typing import Optional


def trim_video(
    input_path: str,
    output_path: str,
    start: float = 0,
    end: Optional[float] = None,
) -> str:
    """Trim video from start to end seconds.

    Args:
        input_path: Path to input video
        output_path: Path to output video
        start: Start time in seconds
        end: End time in seconds (None for until end)
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input video not found: {input_path}")

    cmd = ["ffmpeg", "-i", str(input_file)]

    if start > 0:
        cmd.extend(["-ss", str(start)])

    if end is not None:
        duration = end - start
        cmd.extend(["-t", str(duration)])

    cmd.extend(["-c", "copy", str(output_path)])

    subprocess.run(cmd, check=True, capture_output=True)
    return f"Trimmed: {output_path}"


def cut_segment(
    input_path: str,
    output_path: str,
    start: float,
    duration: float,
) -> str:
    """Cut a specific segment from video.

    Args:
        input_path: Path to input video
        output_path: Path to output video
        start: Start time in seconds
        duration: Duration of segment in seconds
    """
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"Input video not found: {input_path}")

    cmd = [
        "ffmpeg", "-i", str(input_file),
        "-ss", str(start),
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        str(output_path)
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    return f"Segment saved: {output_path}"


def merge_videos(input_paths: list[str], output_path: str) -> str:
    """Merge multiple videos into one.

    Args:
        input_paths: List of input video paths
        output_path: Path to output video
    """
    if len(input_paths) < 2:
        raise ValueError("Need at least 2 videos to merge")

    for path in input_paths:
        if not Path(path).exists():
            raise FileNotFoundError(f"Video not found: {path}")

    # Create temp file with list of inputs
    temp_list = Path(output_path).parent / "merge_list.txt"
    with open(temp_list, "w") as f:
        for path in input_paths:
            f.write(f"file '{Path(path).absolute()}'\n")

    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", str(temp_list),
        "-c", "copy",
        str(output_path)
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    temp_list.unlink(missing_ok=True)
    return f"Merged: {output_path}"
