# Flask app factory
from flask import Flask
from flask_redis import FlaskRedis
from pymongo import MongoClient

# Initialize global clients
redis_client = FlaskRedis()
mongo_client = None

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize Redis and MongoDB
    redis_client.init_app(app)
    global mongo_client
    mongo_client = MongoClient(app.config['MONGO_URI'])

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.video_routes import video_bp
    from app.routes.search_routes import search_bp
    from app.routes.health_routes import health_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(video_bp, url_prefix="/videos")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(health_bp, url_prefix="/health")

    return app
