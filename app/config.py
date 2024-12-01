# Configuration file
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/video_streaming')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME', '')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    UPLOAD_FOLDER = "uploads/"
    TRANSCODE_FOLDER = "transcoded_videos/"
