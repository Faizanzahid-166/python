#!/usr/bin/env python3
"""
Video Editor - Main Entry Point

Usage:
    python main.py --help
    python main.py trim -i video.mp4 -o trimmed.mp4 --start 10 --end 60
    python main.py extract-audio -i video.mp4 -o audio.mp3
    python main.py text-to-speech -i script.otxt -o speech.mp3
    python main.py srt-to-audio -i subs.srt -o audio.mp3
"""
import sys
from videoeditor.cli import main

if __name__ == "__main__":
    sys.exit(main())
