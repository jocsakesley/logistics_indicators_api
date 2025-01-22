

from src.entities.entities import CustomerService
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerDoesNotExistException, CustomerServiceDoesNotExistException


class UpdateCustomerServiceUseCase(AbstractUseCase):
    def __init__(self, customer_service_repository: AbstractRepository, customer_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository
        self.customer_repository = customer_repository

    def execute(self, id: int, customer_service_schema: CustomerService):
        try:
            customer_service = self.customer_service_repository.update(id, customer_service_schema)
            if not customer_service:
                raise CustomerServiceDoesNotExistException('Customer Service does not exist')
        except Exception:
            raise CustomerDoesNotExistException('Client id does not exist') 
        
        updated_customer_service = self.customer_service_repository.get(id=id)
        return updated_customer_service
        
