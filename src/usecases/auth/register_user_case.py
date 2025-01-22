
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.exceptions import ExistentFieldException
from src.repositories.abstract_repository import AbstractRepository


class RegisterUseCase(AbstractUseCase):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def execute(self, *args, **kwargs):


        if self.repository.filter_by(username=args[0].username):
            raise ExistentFieldException('Username already exists')

        if self.repository.filter_by(email=args[0].email):
            raise ExistentFieldException('Email already exists')
        
        

        return self.repository.add(*args)