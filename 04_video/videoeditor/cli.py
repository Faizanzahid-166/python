"""Command-line interface for video editor."""
import argparse
import sys
from pathlib import Path

from .config import INPUT_VIDEOS, INPUT_AUDIOS, INPUT_IMAGES, INPUT_TEXTS
from .config import OUTPUT_VIDEOS, OUTPUT_AUDIOS
from .core import (
    trim_video, merge_videos, cut_segment,
    extract_audio, merge_audios, mute_audio,
    images_to_video, add_audio_to_video, replace_audio
)
from .tts import text_to_speech, subtitle_to_speech


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser with all commands."""
    parser = argparse.ArgumentParser(
        prog="videoeditor",
        description="Simple video editor with TTS support"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # === Video commands ===
    # trim
    trim_parser = subparsers.add_parser("trim", help="Trim video")
    trim_parser.add_argument("-i", "--input", required=True, help="Input video")
    trim_parser.add_argument("-o", "--output", required=True, help="Output video")
    trim_parser.add_argument("--start", type=float, default=0, help="Start time (seconds)")
    trim_parser.add_argument("--end", type=float, help="End time (seconds)")

    # cut-segment
    cut_parser = subparsers.add_parser("cut-segment", help="Cut a video segment")
    cut_parser.add_argument("-i", "--input", required=True, help="Input video")
    cut_parser.add_argument("-o", "--output", required=True, help="Output video")
    cut_parser.add_argument("--start", type=float, required=True, help="Start time (seconds)")
    cut_parser.add_argument("--duration", type=float, required=True, help="Duration (seconds)")

    # merge-videos
    merge_parser = subparsers.add_parser("merge-videos", help="Merge multiple videos")
    merge_parser.add_argument("-i", "--inputs", nargs="+", required=True, help="Input videos")
    merge_parser.add_argument("-o", "--output", required=True, help="Output video")

    # === Audio commands ===
    # extract-audio
    extract_parser = subparsers.add_parser("extract-audio", help="Extract audio from video")
    extract_parser.add_argument("-i", "--input", required=True, help="Input video")
    extract_parser.add_argument("-o", "--output", help="Output audio (default: same name .mp3)")

    # merge-audios
    merge_audio_parser = subparsers.add_parser("merge-audios", help="Merge multiple audios")
    merge_audio_parser.add_argument("-i", "--inputs", nargs="+", required=True, help="Input audios")
    merge_audio_parser.add_argument("-o", "--output", required=True, help="Output audio")

    # mute
    mute_parser = subparsers.add_parser("mute", help="Remove audio from video")
    mute_parser.add_argument("-i", "--input", required=True, help="Input video")
    mute_parser.add_argument("-o", "--output", required=True, help="Output video")

    # === Image commands ===
    # images-to-video
    img_parser = subparsers.add_parser("images-to-video", help="Create video from images")
    img_parser.add_argument("-f", "--folder", required=True, help="Folder with images")
    img_parser.add_argument("-o", "--output", required=True, help="Output video")
    img_parser.add_argument("--fps", type=int, default=24, help="Frames per second")
    img_parser.add_argument("--duration", type=float, default=1.0, help="Seconds per image")

    # === Audio+Video combine commands ===
    # add-audio
    add_audio_parser = subparsers.add_parser("add-audio", help="Add audio to video")
    add_audio_parser.add_argument("-i", "--input", required=True, help="Input video")
    add_audio_parser.add_argument("-a", "--audio", required=True, help="Audio file")
    add_audio_parser.add_argument("-o", "--output", required=True, help="Output video")
    add_audio_parser.add_argument("--loop", action="store_true", help="Loop audio if shorter than video")

    # replace-audio
    replace_audio_parser = subparsers.add_parser("replace-audio", help="Replace video audio")
    replace_audio_parser.add_argument("-i", "--input", required=True, help="Input video")
    replace_audio_parser.add_argument("-a", "--audio", required=True, help="New audio file")
    replace_audio_parser.add_argument("-o", "--output", required=True, help="Output video")

    # === TTS commands ===
    # text-to-speech
    tts_parser = subparsers.add_parser("text-to-speech", help="Convert text file to speech")
    tts_parser.add_argument("-i", "--input", required=True, help="Input text file (.otxt, .txt)")
    tts_parser.add_argument("-o", "--output", required=True, help="Output audio")
    tts_parser.add_argument("--voice", default="en-US-JennyNeural", help="TTS voice")

    # srt-to-audio
    srt_parser = subparsers.add_parser("srt-to-audio", help="Convert subtitles to timed audio")
    srt_parser.add_argument("-i", "--input", required=True, help="Input subtitle file (.srt, .osrt)")
    srt_parser.add_argument("-o", "--output", required=True, help="Output audio")
    srt_parser.add_argument("--voice", default="en-US-JennyNeural", help="TTS voice")

    return parser


def run_command(args: argparse.Namespace) -> int:
    """Execute the command and return exit code."""
    try:
        if args.command == "trim":
            result = trim_video(args.input, args.output, args.start, args.end)
        elif args.command == "cut-segment":
            result = cut_segment(args.input, args.output, args.start, args.duration)
        elif args.command == "merge-videos":
            result = merge_videos(args.inputs, args.output)
        elif args.command == "extract-audio":
            output = args.output or str(Path(args.input).with_suffix(".mp3"))
            result = extract_audio(args.input, output)
        elif args.command == "merge-audios":
            result = merge_audios(args.inputs, args.output)
        elif args.command == "mute":
            result = mute_audio(args.input, args.output)
        elif args.command == "images-to-video":
            result = images_to_video(args.folder, args.output, args.fps, args.duration)
        elif args.command == "add-audio":
            result = add_audio_to_video(args.input, args.audio, args.output, args.loop)
        elif args.command == "replace-audio":
            result = replace_audio(args.input, args.audio, args.output)
        elif args.command == "text-to-speech":
            result = text_to_speech(args.input, args.output, args.voice)
        elif args.command == "srt-to-audio":
            result = subtitle_to_speech(args.input, args.output, args.voice)
        else:
            print("Unknown command. Use --help for usage.")
            return 1

        print(f"✓ {result}")
        return 0

    except FileNotFoundError as e:
        print(f"✗ Error: {e}")
        return 1
    except ValueError as e:
        print(f"✗ Error: {e}")
        return 1
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return 1


def main(argv: list[str] | None = None) -> int:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 1

    return run_command(args)
