from flask import Flask
from redis import Redis

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Redis client (load host from config at runtime)
    app.redis = Redis(
        host=app.config["REDIS_HOST"],
        port=app.config["REDIS_PORT"],
        db=app.config["REDIS_DB"],
        decode_responses=True
    )

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
