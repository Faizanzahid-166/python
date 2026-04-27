import subprocess
import os

def extract_audio(input_video, output_audio="output.mp3"):
    if not os.path.exists(input_video):
        print("Video file not found!")
        return

    command = [
        "ffmpeg",
        "-i", input_video,
        "-q:a", "0",
        "-map", "a",
        output_audio
    ]

    try:
        subprocess.run(command, check=True)
        print("Audio extracted successfully!")
    except subprocess.CalledProcessError:
        print("Error extracting audio")