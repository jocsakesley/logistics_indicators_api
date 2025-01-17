
from src.models.client_model import CustomerModel
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.file_handler_chunks import FileHandler


class LoadCustomersUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        FileHandler(**kwargs, repository=self.customer_repository, model=CustomerModel)