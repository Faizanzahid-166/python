import ffmpeg


def change_speed(input_file, output_file, speed=1.0):

    video_speed = f"setpts={1/speed}*PTS"

    if speed <= 0.5:
        audio_speed = f"atempo=0.5,atempo={speed/0.5}"
    elif speed >= 2:
        audio_speed = f"atempo=2.0,atempo={speed/2}"
    else:
        audio_speed = f"atempo={speed}"

    (
        ffmpeg
        .input(input_file)
        .output(
            output_file,
            vf=video_speed,
            af=audio_speed
        )
        .run()
    )