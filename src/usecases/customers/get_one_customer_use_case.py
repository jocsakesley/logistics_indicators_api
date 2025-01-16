
from src.repositories.abstract_repository import AbstractRepository


class GetOneCustomerUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        return self.customer_repository.get(**kwargs)