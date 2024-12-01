# Health check endpoint
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/', methods=['GET'])
def health_check():
    """
    Endpoint for health check.
    """
    return jsonify({'status': 'healthy'}), 200
