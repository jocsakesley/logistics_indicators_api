
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerServiceDoesNotExistException
from src.repositories.abstract_repository import AbstractRepository


class GetOneCustomerServiceUseCase(AbstractUseCase):
    def __init__(self, customer_service_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository

    def execute(self, id):
        customer_service = self.customer_service_repository.get(id)
        if not customer_service:
            raise CustomerServiceDoesNotExistException('Customer Service does not exist')
        return customer_service