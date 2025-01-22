
from src.entities.entities import Customer
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerDoesNotExistException


class UpdateCustomerUseCase(AbstractUseCase):
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, id: int, customer_schema: Customer):
        customer_service = self.customer_repository.update(id, customer_schema)
        if not customer_service:
            raise CustomerDoesNotExistException('Customer does not exist')
        updated_customer_service = self.customer_repository.get(id)
        return updated_customer_service
        
