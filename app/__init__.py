from flask import Flask
from .config import Config
from .extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    from .auth.routes import auth_bp
    from .open_routes import open_bp  # Import the open_bp Blueprint

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(open_bp, url_prefix='/api')  # Register the open_bp Blueprint

    return app