
from src.repositories.abstract_repository import AbstractRepository


class GetAllCustomerServiceUseCase:
    def __init__(self, customer_service_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository

    def execute(self, *args, **kwargs):
        return self.customer_service_repository.get_all()