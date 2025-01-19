
from flask import Request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from typing import Dict
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from src.models.base_model import BaseModel
from src.entities.entities import User, UserLogin
from src.models.user_model import UserModel
from src.usecases.exceptions import ExistentFieldException, IncompletedDataException
from src.repositories.abstract_repository import AbstractRepository


class LoginUseCase:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def execute(self, user_login: dict):

        user: BaseModel = self.repository.get(username=user_login.get("username"))

        if not user or not user.check_password(user_login.get("password")):
            return {'message': 'Bad credentials'}
        
        additional_claims = {
            'username': user.username,
            'email': user.email,
            'sub': 'logistcs-service'
        }
        
        access_token = create_access_token(
            identity=user.id,
            additional_claims=additional_claims
        )
        refresh_token = create_refresh_token(
            identity=user.id,
            additional_claims=additional_claims
        )

        return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': user.to_dict()
            }