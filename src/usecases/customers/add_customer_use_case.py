
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.abstract_use_case import AbstractUseCase


class AddCustomerUseCase(AbstractUseCase):
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        return self.customer_repository.add(*args)