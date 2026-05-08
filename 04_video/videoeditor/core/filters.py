import ffmpeg


def apply_filter(input_file, output_file,
                 brightness=None,
                 contrast=None,
                 blur=None,
                 sharpen=None,
                 grayscale=False):

    stream = ffmpeg.input(input_file)

    vf = []

    if brightness is not None or contrast is not None:
        b = brightness or 0
        c = contrast or 1
        vf.append(f'eq=brightness={b}:contrast={c}')

    if blur:
        vf.append(f'boxblur={blur}')

    if sharpen:
        vf.append(f'unsharp=5:5:{sharpen}:5:5:0')

    if grayscale:
        vf.append('hue=s=0')

    video = stream.video.filter_multi_output(
        'split')[0] if False else stream.video

    output = ffmpeg.output(
        stream.video.filter_('fps', fps=60) if False else stream.video,
        stream.audio,
        output_file,
        vf=",".join(vf)
    )

    ffmpeg.run(output)

def youtube_shorts_filter(input_file, output_file):

    filters = (
        "scale=1080:1920,"
        "eq=contrast=1.22:"
        "brightness=-0.02:"
        "saturation=1.45,"
        "unsharp=7:7:1.8:7:7:0,"
        "hqdn3d,"
        "fps=60"
    )

    (
        ffmpeg
        .input(input_file)
        .output(
            output_file,
            vf=filters,
            vcodec="libx264",
            acodec="aac",
            crf=18,
            preset="slow"
        )
        .run()
    )


def youtube_long_filter(input_file, output_file):

    filters = (
        "scale=1920:1080,"
        "eq=contrast=1.18:"
        "brightness=-0.01:"
        "saturation=1.30,"
        "unsharp=5:5:1.5:5:5:0,"
        "hqdn3d,"
        "fps=60"
    )

    (
        ffmpeg
        .input(input_file)
        .output(
            output_file,
            vf=filters,
            vcodec="libx264",
            acodec="aac",
            crf=18,
            preset="slow"
        )
        .run()
    )