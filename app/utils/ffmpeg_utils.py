# FFmpeg video transcoding utility
import os
import subprocess

def transcode_video(input_path, output_folder, resolutions=("360p", "720p", "1080p")):
    """
    Transcodes a video into multiple resolutions using FFmpeg.
    Args:
        input_path (str): Path to the input video file.
        output_folder (str): Folder to save transcoded files.
        resolutions (tuple): Resolutions to transcode into.
    Returns:
        dict: A dictionary with resolution keys and paths to the transcoded files.
    """
    resolution_map = {
        "360p": "640x360",
        "720p": "1280x720",
        "1080p": "1920x1080"
    }
    transcoded_files = {}

    os.makedirs(output_folder, exist_ok=True)

    for resolution in resolutions:
        output_path = os.path.join(output_folder, f"{resolution}.mp4")
        ffmpeg_command = [
            "ffmpeg",
            "-i", input_path,
            "-vf", f"scale={resolution_map[resolution]}",
            "-c:v", "libx264",
            "-crf", "23",
            "-preset", "fast",
            "-c:a", "aac",
            "-b:a", "128k",
            output_path
        ]
        subprocess.run(ffmpeg_command, check=True)
        transcoded_files[resolution] = output_path

    return transcoded_files
