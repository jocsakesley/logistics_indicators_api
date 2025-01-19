
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.exceptions import CustomerDoesNotExistException


class UpdateCustomerUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        customer_service = self.customer_repository.update(*args)
        if not customer_service:
            raise CustomerDoesNotExistException('Customer does not exist')
        updated_customer_service = self.customer_repository.get(id=args[0])
        return updated_customer_service
        
