"""Configuration management for video editor."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
MEDIA_DIR = BASE_DIR / "media"
TEMP_DIR = BASE_DIR / "temp"

INPUT_DIR = MEDIA_DIR / "input"
OUTPUT_DIR = MEDIA_DIR / "output"

# Input subdirectories
INPUT_VIDEOS = INPUT_DIR / "videos"
INPUT_AUDIOS = INPUT_DIR / "audios"
INPUT_IMAGES = INPUT_DIR / "images"
INPUT_TEXTS = INPUT_DIR / "texts"

# Output subdirectories
OUTPUT_VIDEOS = OUTPUT_DIR / "videos"
OUTPUT_AUDIOS = OUTPUT_DIR / "audios"
OUTPUT_IMAGES = OUTPUT_DIR / "images"

# Default TTS voice
DEFAULT_VOICE = os.getenv("TTS_VOICE", "en-US-JennyNeural")

# Ensure directories exist
for directory in [INPUT_VIDEOS, INPUT_AUDIOS, INPUT_IMAGES, INPUT_TEXTS,
                  OUTPUT_VIDEOS, OUTPUT_AUDIOS, OUTPUT_IMAGES, TEMP_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
