
from src.repositories.customer_service_repository import ClientDoesNotExistException
from src.repositories.abstract_repository import AbstractRepository


class AddCustomerServiceUseCase:
    def __init__(self, customer_service_repository: AbstractRepository, customer_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        client = self.customer_repository.get(args[0].id_cliente)
        self.customer_service_repository.add(*args)
        if not client:
            raise ClientDoesNotExistException('Client does not exist') 
        return client