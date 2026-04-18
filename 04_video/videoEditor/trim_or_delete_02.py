import subprocess

def remove_first_25_seconds(input_path, output_path):
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    command = [
        "ffmpeg",
        "-i", input_path,
        "-ss", "25",
        "-c", "copy",
        output_path
    ]

    subprocess.run(command, check=True)
    return f"✅ Trimmed: {output_path}"