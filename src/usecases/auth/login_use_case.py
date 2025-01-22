
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from src.models.base_model import BaseModel
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.abstract_use_case import AbstractUseCase


class LoginUseCase(AbstractUseCase):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def execute(self, user_login: dict):

        user: BaseModel = self.repository.filter_by(username=user_login.get("username"))

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