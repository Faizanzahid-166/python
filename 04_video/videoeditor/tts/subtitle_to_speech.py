"""Convert subtitle files (.srt/.osrt) to timed audio."""
import asyncio
from pathlib import Path
from typing import Optional
import edge_tts
import srt
from pydub import AudioSegment


def subtitle_to_speech(
    subtitle_file: str,
    output_path: str,
    voice: str = "en-US-JennyNeural",
    temp_dir: Optional[str] = None,
) -> str:
    """Convert subtitle file to audio with proper timing.

    Each subtitle is spoken at its designated time, with silence
    between subtitles matching the original timing.

    Args:
        subtitle_file: Path to .srt or .osrt file
        output_path: Path to output audio file
        voice: TTS voice name (default: en-US-JennyNeural)
        temp_dir: Directory for temporary audio files
    """
    sub_path = Path(subtitle_file)
    if not sub_path.exists():
        raise FileNotFoundError(f"Subtitle file not found: {subtitle_file}")

    # Parse subtitles
    with open(sub_path, "r", encoding="utf-8") as f:
        subtitles = list(srt.parse(f.read()))

    if not subtitles:
        raise ValueError("No subtitles found in file")

    # Run async conversion
    asyncio.run(
        _generate_timed_audio(
            subtitles, output_path, voice, temp_dir
        )
    )

    return f"Audio generated from subtitles: {output_path}"


async def _generate_timed_audio(
    subtitles: list,
    output_path: str,
    voice: str,
    temp_dir: Optional[str],
) -> None:
    """Generate audio with proper subtitle timing."""
    temp_path = Path(temp_dir) if temp_dir else Path(output_path).parent / "temp_tts"
    temp_path.mkdir(parents=True, exist_ok=True)

    # Create silent base audio matching total duration
    total_duration_ms = int(subtitles[-1].end.total_seconds() * 1000)
    final_audio = AudioSegment.silent(duration=total_duration_ms)

    # Generate TTS for each subtitle and place at correct timestamp
    for i, sub in enumerate(subtitles):
        temp_file = temp_path / f"sub_{i}.mp3"

        # Generate speech for this subtitle
        communicate = edge_tts.Communicate(sub.content, voice)
        await communicate.save(str(temp_file))

        # Load generated audio
        segment = AudioSegment.from_mp3(str(temp_file))

        # Calculate start time in milliseconds
        start_ms = int(sub.start.total_seconds() * 1000)

        # Overlay at correct position
        final_audio = final_audio.overlay(segment, position=start_ms)

        # Cleanup temp file
        temp_file.unlink(missing_ok=True)

    # Export final audio
    final_audio.export(output_path, format="mp3")

    # Remove temp directory if empty
    try:
        temp_path.rmdir()
    except OSError:
        pass
