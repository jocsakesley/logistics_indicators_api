
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.file_handler import FileHandler


class LoadCustomerServicesUseCase:
    def __init__(self, customer_service_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository

    def execute(self, *args, **kwargs):
        FileHandler(**kwargs, repository=self.customer_service_repository)