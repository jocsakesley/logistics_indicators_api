
from flask import Request
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from src.entities.entities import User
from src.models.user_model import UserModel
from src.usecases.exceptions import ExistentFieldException, IncompletedDataException
from src.repositories.abstract_repository import AbstractRepository


class RegisterUseCase:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def execute(self, *args, **kwargs):


        if self.repository.filter_by(username=args[0].username):
            raise ExistentFieldException('Username already exists')

        if self.repository.filter_by(email=args[0].email):
            raise ExistentFieldException('Email already exists')
        
        

        return self.repository.add(*args)