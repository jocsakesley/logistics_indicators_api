
from src.models.client_model import CustomerModel
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.file_handler_chunks import FileHandler


class LoadCustomersUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        file = kwargs.get("file")
        if not file:
            raise ValueError("File is required")
        
        if not hasattr(file, 'read'):
            raise TypeError("Invalid file object")
        
        if file.content_type not in ["application/json", "text/csv"]:
            raise ValueError("Unsupported file type")
        FileHandler(**kwargs, repository=self.customer_repository, model=CustomerModel)