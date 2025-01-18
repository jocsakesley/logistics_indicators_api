
from src.usecases.exceptions import CustomerDoesNotExistException
from src.repositories.abstract_repository import AbstractRepository


class GetOneCustomerUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        customer_service = self.customer_repository.get(**kwargs)
        if not customer_service:
            raise CustomerDoesNotExistException('Client does not exist')
        return customer_service