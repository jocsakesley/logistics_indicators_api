
from src.usecases.exceptions import CustomerDoesNotExistException
from src.repositories.abstract_repository import AbstractRepository


class AddCustomerServiceUseCase:
    def __init__(self, customer_service_repository: AbstractRepository, customer_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        client = self.customer_repository.get(id=args[0].id_cliente)
        
        if not client:
            raise CustomerDoesNotExistException('Client id does not exist') 
        self.customer_service_repository.add(*args)
        return client