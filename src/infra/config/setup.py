

from datetime import timedelta
import os

from flask import Flask
from flask_jwt_extended import JWTManager

from src.infra.db import db
from src.infra.routes.customer_services_routes import cs_bp
from src.infra.routes.customers_routes import customer_bp
from src.infra.routes.indicators_routes import indicator_bp
from src.infra.routes.auth_routes import auth_bp


class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

def create_app():
    app = Flask(__name__)
    jwt = JWTManager()
    app.config.from_object(Config)
    
    db.init_db()
    jwt.init_app(app)
    
    app.register_blueprint(cs_bp, url_prefix='/v1')
    app.register_blueprint(customer_bp, url_prefix='/v1')
    app.register_blueprint(indicator_bp, url_prefix='/v1')
    app.register_blueprint(auth_bp, url_prefix='/v1/auth')
    
    return app