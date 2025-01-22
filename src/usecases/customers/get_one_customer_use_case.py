
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.exceptions import CustomerDoesNotExistException
from src.repositories.abstract_repository import AbstractRepository


class GetOneCustomerUseCase(AbstractUseCase):
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, id):
        customer = self.customer_repository.get(id)
        if not customer:
            raise CustomerDoesNotExistException('Client does not exist')
        return customer