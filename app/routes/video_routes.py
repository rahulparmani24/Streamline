# Video upload and streaming endpoints
from flask import Blueprint, request, jsonify
from app.utils.s3_utils import upload_file_to_s3
from app.utils.ffmpeg_utils import transcode_video
from app.utils.db_manager import save_video_metadata
import os

video_bp = Blueprint('video', __name__)

@video_bp.route('/upload', methods=['POST'])
def upload_video():
    """
    Endpoint for uploading a video file.
    """
    file = request.files['file']
    title = request.form['title']
    description = request.form['description']

    # Save locally
    input_path = os.path.join("uploads", file.filename)
    file.save(input_path)

    # Transcode video
    transcoded_files = transcode_video(input_path, "transcoded_videos")

    # Upload to S3
    s3_urls = {
        resolution: upload_file_to_s3(open(path, 'rb'), path)
        for resolution, path in transcoded_files.items()
    }

    # Save metadata to MongoDB
    video_metadata = {
        'title': title,
        'description': description,
        's3_urls': s3_urls,
    }
    video_id = save_video_metadata(video_metadata)

    return jsonify({'message': 'Video uploaded successfully', 'video_id': video_id, 's3_urls': s3_urls}), 201
