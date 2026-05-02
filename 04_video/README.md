# Video Editor

A simple video editing toolkit with text-to-speech support.

## Features

- **Video Operations**: Trim, cut segments, merge videos
- **Audio Operations**: Extract audio, merge audios, mute video
- **Image to Video**: Create slideshow videos from images
- **Text-to-Speech**: Convert `.otxt` text files to audio
- **Subtitle-to-Audio**: Convert `.srt/.osrt` subtitles to timed audio

## Installation

```bash
pip install -r requirements.txt
```

Make sure `ffmpeg` is installed and available in your PATH.

## Usage

```bash
# Show help
python main.py --help

# Video operations
python main.py trim -i media/input/videos/video.mp4 -o media/output/videos/trimmed.mp4 --start 10 --end 60
python main.py cut-segment -i video.mp4 -o segment.mp4 --start 30 --duration 15
python main.py merge-videos -i vid1.mp4 vid2.mp4 -o merged.mp4

# Audio operations
python main.py extract-audio -i video.mp4 -o audio.mp3
python main.py mute -i video.mp4 -o muted.mp4
python main.py merge-audios -i audio1.mp3 audio2.mp3 -o merged.mp3

# Combine audio and video
python main.py add-audio -i video.mp4 -a background.mp3 -o output.mp4
python main.py replace-audio -i video.mp4 -a new_audio.mp3 -o output.mp4

# Image to video
python main.py images-to-video -f media/input/images -o slideshow.mp4 --duration 2

# Text-to-speech
python main.py text-to-speech -i media/input/texts/script.otxt -o speech.mp3 --voice en-US-JennyNeural
python main.py srt-to-audio -i media/input/texts/subs.srt -o audio.mp3
```

## Available TTS Voices

List available voices:
```bash
edge-tts --list-voices
```

Popular voices:
- `en-US-JennyNeural` (English US, Female)
- `en-US-GuyNeural` (English US, Male)
- `en-GB-SoniaNeural` (English UK, Female)
- `ja-JP-NanamiNeural` (Japanese, Female)
- `zh-CN-XiaoxiaoNeural` (Chinese, Female)

## Folder Structure

```
04_video/
├── media/
│   ├── input/          # Source files
│   │   ├── videos/
│   │   ├── audios/
│   │   ├── images/
│   │   └── texts/      # .otxt, .srt files
│   └── output/         # Generated files
├── videoeditor/        # Main package
├── main.py             # CLI entry point
└── requirements.txt
```
