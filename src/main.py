
from datetime import timedelta
import os
from dotenv import load_dotenv
from flask import Flask, json, request
from flask_jwt_extended import verify_jwt_in_request

from src.infra.jwt.jwt import jwt
from src.infra.db import db
from src.infra.routes.customer_services_routes import cs_bp
from src.infra.routes.customers_routes import customer_bp
from src.infra.routes.indicators_routes import indicator_bp
from src.infra.routes.auth_routes import auth_bp

load_dotenv()

app = Flask(__name__)

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_db()
    jwt.init_app(app)
    
    app.register_blueprint(cs_bp, url_prefix='/v1')
    app.register_blueprint(customer_bp, url_prefix='/v1')
    app.register_blueprint(indicator_bp, url_prefix='/v1')
    app.register_blueprint(auth_bp, url_prefix='/v1/auth')
    
    return app

app = create_app()

# @app.before_request
# def require_jwt():
#     public_endpoints = ['/login', '/register', '/refresh']
    
#     if request.endpoint and request.endpoint not in public_endpoints:
#         verify_jwt_in_request()
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True)








