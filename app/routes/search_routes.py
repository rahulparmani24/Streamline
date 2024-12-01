# Video search endpoint
from flask import Blueprint, request, jsonify
from app.utils.db_manager import get_video_collection

search_bp = Blueprint('search', __name__)

@search_bp.route('/', methods=['GET'])
def search_videos():
    """
    Endpoint for searching videos.
    """
    query = request.args.get('q', '')
    collection = get_video_collection()

    results = collection.find({"title": {"$regex": query, "$options": "i"}})
    videos = [
        {"id": str(video["_id"]), "title": video["title"], "description": video["description"]}
        for video in results
    ]
    return jsonify(videos)
