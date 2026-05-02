"""Combine audio and video."""
from pathlib import Path
from moviepy import VideoFileClip, AudioFileClip


def add_audio_to_video(
    video_path: str,
    audio_path: str,
    output_path: str,
    loop_audio: bool = False,
) -> str:
    """Add audio track to video (replaces existing audio).

    Args:
        video_path: Path to video file
        audio_path: Path to audio file
        output_path: Path to output video
        loop_audio: If True, loop audio to match video duration
    """
    video_file = Path(video_path)
    audio_file = Path(audio_path)

    if not video_file.exists():
        raise FileNotFoundError(f"Video not found: {video_path}")
    if not audio_file.exists():
        raise FileNotFoundError(f"Audio not found: {audio_path}")

    video = VideoFileClip(str(video_file))
    audio = AudioFileClip(str(audio_file))

    if loop_audio and audio.duration < video.duration:
        # Loop audio to match video
        from moviepy import CompositeAudioClip
        loops_needed = int(video.duration / audio.duration) + 1
        audio_clips = [audio] * loops_needed
        audio = CompositeAudioClip([
            audio.set_start(i * audio.duration)
            for i in range(loops_needed)
        ])

    # Trim or extend audio to match video
    if audio.duration > video.duration:
        audio = audio.subclipped(0, video.duration)

    final_video = video.with_audio(audio)
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    video.close()
    audio.close()

    return f"Audio added: {output_path}"


def replace_audio(
    video_path: str,
    audio_path: str,
    output_path: str,
) -> str:
    """Replace video audio with new audio file.

    Args:
        video_path: Path to video file
        audio_path: Path to new audio file
        output_path: Path to output video
    """
    return add_audio_to_video(video_path, audio_path, output_path)


def mix_audio_with_video(
    video_path: str,
    audio_path: str,
    output_path: str,
    video_volume: float = 0.5,
    audio_volume: float = 0.5,
) -> str:
    """Mix external audio with video's existing audio (background music).

    Args:
        video_path: Path to video file
        audio_path: Path to background audio
        output_path: Path to output video
        video_volume: Original video volume (0.0-1.0)
        audio_volume: Background audio volume (0.0-1.0)
    """
    video_file = Path(video_path)
    audio_file = Path(audio_path)

    if not video_file.exists():
        raise FileNotFoundError(f"Video not found: {video_path}")
    if not audio_file.exists():
        raise FileNotFoundError(f"Audio not found: {audio_path}")

    video = VideoFileClip(str(video_file))
    bg_audio = AudioFileClip(str(audio_file))

    # Adjust volumes
    if video.audio is not None:
        video_audio = video.audio.with_volume_scaled(video_volume)
    else:
        video_audio = None

    bg_audio = bg_audio.with_volume_scaled(audio_volume)

    # Loop background audio if needed
    if bg_audio.duration < video.duration:
        from moviepy import CompositeAudioClip
        loops_needed = int(video.duration / bg_audio.duration) + 1
        bg_audio = CompositeAudioClip([
            bg_audio.set_start(i * bg_audio.duration)
            for i in range(loops_needed)
        ])

    # Trim to video duration
    if bg_audio.duration > video.duration:
        bg_audio = bg_audio.subclipped(0, video.duration)

    # Mix audio tracks
    if video_audio is not None:
        from moviepy import CompositeAudioClip
        mixed_audio = CompositeAudioClip([video_audio, bg_audio])
        final_video = video.with_audio(mixed_audio)
    else:
        final_video = video.with_audio(bg_audio)

    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    video.close()
    bg_audio.close()

    return f"Audio mixed: {output_path}"
