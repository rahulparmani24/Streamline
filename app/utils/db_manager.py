# MongoDB utility functions
from app import mongo_client

def get_video_collection():
    """
    Returns the MongoDB collection for storing video metadata.
    """
    db = mongo_client['video_streaming']
    return db['videos']

def save_video_metadata(metadata):
    """
    Saves video metadata to the MongoDB collection.
    Args:
        metadata (dict): The metadata to save.
    Returns:
        str: The ID of the inserted document.
    """
    collection = get_video_collection()
    result = collection.insert_one(metadata)
    return str(result.inserted_id)

def fetch_video_metadata(video_id):
    """
    Fetches video metadata by ID.
    Args:
        video_id (str): The ID of the video.
    Returns:
        dict: The metadata of the video.
    """
    collection = get_video_collection()
    return collection.find_one({"_id": video_id})

def search_videos(query):
    """
    Searches videos by title using a regex query.
    Args:
        query (str): The search query.
    Returns:
        list: A list of matching video documents.
    """
    collection = get_video_collection()
    return collection.find({"title": {"$regex": query, "$options": "i"}})
