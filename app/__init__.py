from flask import Flask
from app.config import Config
from app.extensions import jwt, db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    jwt.init_app(app)
    db.init_app(app)

    # Register blueprints
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app