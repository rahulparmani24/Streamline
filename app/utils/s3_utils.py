# S3 utility functions
import boto3
from flask import current_app

def upload_file_to_s3(file, filename):
    """
    Uploads a file to AWS S3.
    Args:
        file (file-like object): The file to upload.
        filename (str): The filename to use in S3.
    Returns:
        str: The public URL of the uploaded file.
    """
    s3_client = boto3.client(
        's3',
        aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
        region_name=current_app.config['AWS_REGION']
    )

    bucket_name = current_app.config['AWS_BUCKET_NAME']
    s3_client.upload_fileobj(
        file,
        bucket_name,
        filename,
        ExtraArgs={'ACL': 'public-read'}
    )

    return f"https://{bucket_name}.s3.{current_app.config['AWS_REGION']}.amazonaws.com/{filename}"
