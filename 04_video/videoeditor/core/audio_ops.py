"""Audio operations: extract, merge, mute."""
import subprocess
from pathlib import Path
from typing import Optional


def extract_audio(
    input_video: str,
    output_audio: Optional[str] = None,
    quality: str = "0",
) -> str:
    """Extract audio from video file.

    Args:
        input_video: Path to input video
        output_audio: Path to output audio (default: same name with .mp3)
        quality: Audio quality 0-9 (0=best)
    """
    input_file = Path(input_video)
    if not input_file.exists():
        raise FileNotFoundError(f"Video file not found: {input_video}")

    if output_audio is None:
        output_audio = str(input_file.with_suffix(".mp3"))

    cmd = [
        "ffmpeg",
        "-i", str(input_file),
        "-q:a", quality,
        "-map", "a",
        output_audio
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    return f"Audio extracted: {output_audio}"


def merge_audios(input_paths: list[str], output_path: str) -> str:
    """Merge multiple audio files into one.

    Args:
        input_paths: List of input audio paths
        output_path: Path to output audio
    """
    if len(input_paths) < 2:
        raise ValueError("Need at least 2 audio files to merge")

    for path in input_paths:
        if not Path(path).exists():
            raise FileNotFoundError(f"Audio not found: {path}")

    # Create temp file with list of inputs
    temp_list = Path(output_path).parent / "audio_merge_list.txt"
    with open(temp_list, "w") as f:
        for path in input_paths:
            f.write(f"file '{Path(path).absolute()}'\n")

    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", str(temp_list),
        "-c", "copy",
        output_path
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    temp_list.unlink(missing_ok=True)
    return f"Audios merged: {output_path}"


def mute_audio(input_video: str, output_path: str) -> str:
    """Remove audio from video (mute).

    Args:
        input_video: Path to input video
        output_path: Path to output video
    """
    input_file = Path(input_video)
    if not input_file.exists():
        raise FileNotFoundError(f"Video not found: {input_video}")

    cmd = [
        "ffmpeg",
        "-i", str(input_file),
        "-an",
        "-c:v", "copy",
        output_path
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    return f"Audio muted: {output_path}"

    # python main.py extract-audio -i media/input/videos/sample.mp4 -o media/output/audio.mp3
