import time
from flask import json, request
from flask_jwt_extended import verify_jwt_in_request
from werkzeug.exceptions import HTTPException

from src.infra.config.logger import logger


def set_middlewares(app):
    @app.before_request
    def measure_time():
        start_time = time.time()
        request.start_time = start_time

    @app.after_request
    def log_time(response):
        if hasattr(request, 'start_time'):
            end_time = time.time()
            logger.info(f"{request.endpoint} durou {end_time - request.start_time:.4f} segundos")
        return response

    @app.before_request
    def require_jwt():
        public_endpoints = ['auth.login', 'auth.register', 'auth.refresh', 'monitoring.health']
        if request.endpoint and request.endpoint not in public_endpoints:
            verify_jwt_in_request()

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response