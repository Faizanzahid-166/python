"""Text-to-speech from .otxt files."""
import asyncio
from pathlib import Path
import edge_tts


def text_to_speech(
    text_file: str,
    output_path: str,
    voice: str = "en-US-JennyNeural",
) -> str:
    """Convert text file to speech audio.

    Args:
        text_file: Path to .otxt or .txt file
        output_path: Path to output audio file
        voice: TTS voice name (default: en-US-JennyNeural)
    """
    text_path = Path(text_file)
    if not text_path.exists():
        raise FileNotFoundError(f"Text file not found: {text_file}")

    # Read text content
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        raise ValueError("Text file is empty")

    # Run async TTS
    asyncio.run(_generate_speech(text, output_path, voice))

    return f"Audio generated: {output_path}"


async def _generate_speech(
    text: str,
    output_path: str,
    voice: str,
) -> None:
    """Async helper to generate speech."""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

# python main.py srt-to-audio -i .\media\input\texts\test.wav.srt -o .\media\output\audios\audio.mp3  --voice en-US-JennyNeural
