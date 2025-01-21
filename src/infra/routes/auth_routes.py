from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.controllers.auth.refresh_controller import RefreshController
from src.controllers.auth.login_controller import LoginController
from src.controllers.auth.register_controller import RegisterController
from src.infra.db import db
from src.models.user_model import UserModel
from src.repositories.repository import Repository
from src.usecases.auth.register_user_case import RegisterUseCase
from src.usecases.auth.login_use_case import LoginUseCase
from src.usecases.auth.refresh_use_case import RefreshUseCase


auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')
def register():
    repository = Repository(db.DbSession, UserModel)
    use_case = RegisterUseCase(repository)
    return RegisterController(use_case).handle(request=request)

@auth_bp.post('/login')
def login():
    repository = Repository(db.DbSession, UserModel)
    use_case = LoginUseCase(repository)
    return LoginController(use_case).handle(request=request)

@auth_bp.post('/refresh')
@jwt_required(refresh=True)
def refresh():
    use_case = RefreshUseCase()
    return RefreshController(use_case).handle()