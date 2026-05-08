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
python main.py srt-to-audio -i .\media\input\texts\test.wav.srt -o .\media\output\audios\audio.mp3  --voice en-US-JennyNeural
python main.py srt-to-audio -i .\media\input\texts\ -o .\media\output\audios\audio.mp3  --voice en-US-JennyNeural

# Increase brightness
python main.py filter -i input.mp4 -o bright.mp4 --brightness 0.1

# Sharpen video
python main.py filter -i input.mp4 -o sharp.mp4 --sharpen 5

# Blur video
python main.py filter -i input.mp4 -o blur.mp4 --blur 2

# Coding style enhancement
python main.py filter -i code.mp4 -o enhanced.mp4 --coding-mode

# 2x faster
python main.py speed -i input.mp4 -o fast.mp4 --rate 2.0

# Slow motion
python main.py speed -i input.mp4 -o slow.mp4 --rate 0.5

# Coding timelapse
python main.py speed -i coding.mp4 -o coding_fast.mp4 --rate 3

python main.py youtube-shorts -i input.mp4 -o shorts.mp4
python main.py youtube-long -i input.mp4 -o youtube.mp4
```

## Available TTS Voices

List available voices:
```bash
edge-tts --list-voices
python -m edge_tts --list-voices



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
# rm -r venv
# python -m venv venv
# venv\Scripts\activate
# pip freeze > requirements.txt
# pip install -r requirements.txt

# load .env variables
# pip install python-dotenv

# for video editing, we will use ffmpeg command line tool, which can be installed from https://ffmpeg.org/download.html
# pip install moviepy numpy 

# for text to speech, we will use edge-tts, which is a python wrapper for Microsoft Edge's text-to-speech API. It can be installed from https://pypi.org/project/edge-tts/
#  pip install srt
#  pip install edge-tts 
#  pip install pydub  
# pip install ffmpeg-python


-voice en-US-JennyNeural
-voice en-US-GuyNeural

en-AU-NatashaNeural                Female    General                Friendly, Positive
en-AU-WilliamMultilingualNeural    Male      General                Friendly, Positive
en-CA-ClaraNeural                  Female    General                Friendly, Positive
en-CA-LiamNeural                   Male      General                Friendly, Positive
en-GB-LibbyNeural                  Female    General                Friendly, Positive
en-GB-MaisieNeural                 Female    General                Friendly, Positive
en-GB-RyanNeural                   Male      General                Friendly, Positive
en-GB-SoniaNeural                  Female    General                Friendly, Positive
en-GB-ThomasNeural                 Male      General                Friendly, Positive
en-HK-SamNeural                    Male      General                Friendly, Positive
en-HK-YanNeural                    Female    General                Friendly, Positive
en-IE-ConnorNeural                 Male      General                Friendly, Positive
en-IE-EmilyNeural                  Female    General                Friendly, Positive
en-IN-NeerjaExpressiveNeural       Female    General                Friendly, Positive
en-IN-NeerjaNeural                 Female    General                Friendly, Positive
en-IN-PrabhatNeural                Male      General                Friendly, Positive
en-KE-AsiliaNeural                 Female    General                Friendly, Positive
en-KE-ChilembaNeural               Male      General                Friendly, Positive
en-NG-AbeoNeural                   Male      General                Friendly, Positive
en-NG-EzinneNeural                 Female    General                Friendly, Positive
en-NZ-MitchellNeural               Male      General                Friendly, Positive
en-NZ-MollyNeural                  Female    General                Friendly, Positive
en-PH-JamesNeural                  Male      General                Friendly, Positive
en-PH-RosaNeural                   Female    General                Friendly, Positive
en-SG-LunaNeural                   Female    General                Friendly, Positive
en-SG-WayneNeural                  Male      General                Friendly, Positive
en-TZ-ElimuNeural                  Male      General                Friendly, Positive
en-TZ-ImaniNeural                  Female    General                Friendly, Positive
en-US-AnaNeural                    Female    Cartoon, Conversation  Cute
en-US-AndrewMultilingualNeural     Male      Conversation, Copilot  Warm, Confident, Authentic, Honest
en-US-AndrewNeural                 Male      Conversation, Copilot  Warm, Confident, Authentic, Honest
en-US-AriaNeural                   Female    News, Novel            Positive, Confident
en-US-AvaMultilingualNeural        Female    Conversation, Copilot  Expressive, Caring, Pleasant, Friendly
en-US-AvaNeural                    Female    Conversation, Copilot  Expressive, Caring, Pleasant, Friendly
en-US-BrianMultilingualNeural      Male      Conversation, Copilot  Approachable, Casual, Sincere
en-US-BrianNeural                  Male      Conversation, Copilot  Approachable, Casual, Sincere
en-US-ChristopherNeural            Male      News, Novel            Reliable, Authority
en-US-EmmaMultilingualNeural       Female    Conversation, Copilot  Cheerful, Clear, Conversational
en-US-EmmaNeural                   Female    Conversation, Copilot  Cheerful, Clear, Conversational
en-US-EricNeural                   Male      News, Novel            Rational
en-US-GuyNeural                    Male      News, Novel            Passion
en-US-JennyNeural                  Female    General                Friendly, Considerate, Comfort
en-US-MichelleNeural               Female    News, Novel            Friendly, Pleasant
en-US-RogerNeural                  Male      News, Novel            Lively
en-US-SteffanNeural                Male      News, Novel            Rational
```
