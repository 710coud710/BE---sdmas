from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mariadb+mariadbconnector://dbpgf29754552:Lam2409@'
        'serverless-us-central1.sysp0000.db2.skysql.com:4000/sdmas_db'
        '?ssl_verify_cert=True'
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Tắt theo dõi thay đổi (optional)

    db.init_app(app)


    from app.controllers.API_auth import auth_bp
    from app.controllers.hello import hello_bp

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(hello_bp)

    return app
