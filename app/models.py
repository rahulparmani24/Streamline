# Database models
from pymongo.collection import Collection
from app import mongo_client

def get_video_collection() -> Collection:
    """
    Returns the MongoDB collection for storing video metadata.
    """
    db = mongo_client['video_streaming']
    return db['videos']

def save_video_metadata(metadata: dict):
    """
    Saves video metadata to MongoDB.
    """
    collection = get_video_collection()
    result = collection.insert_one(metadata)
    return str(result.inserted_id)

def fetch_video_metadata(video_id: str):
    """
    Fetches video metadata by video ID.
    """
    collection = get_video_collection()
    return collection.find_one({"_id": video_id})
