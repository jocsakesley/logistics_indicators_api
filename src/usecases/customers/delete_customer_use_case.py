
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.exceptions import CustomerDoesNotExistException


class DeleteCustomerUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        customer = self.customer_repository.get(**kwargs)
        if not customer:
            raise CustomerDoesNotExistException('Customer does not exist')
        self.customer_repository.delete(customer)
