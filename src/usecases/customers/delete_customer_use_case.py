
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerDoesNotExistException


class DeleteCustomerUseCase(AbstractUseCase):
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, id):
        customer = self.customer_repository.get(id)
        if not customer:
            raise CustomerDoesNotExistException('Customer does not exist')
        self.customer_repository.delete(customer)
