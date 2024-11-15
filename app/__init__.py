from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    # Initialize database
    db.init_app(app)

    # Register blueprints
    from app.controllers.API_auth import auth_bp
    from app.controllers.hello import hello_bp

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(hello_bp)

    return app
