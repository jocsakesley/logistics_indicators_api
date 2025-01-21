
from queue import Queue
from flask import Request
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.file_handler_chunks import FileHandler


class LoadCustomersUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, request: Request, queue: Queue):
        file = request.files['file']
        if not file:
            raise ValueError("File is required")
        
        if not hasattr(file, 'read'):
            raise TypeError("Invalid file object")
        
        if file.content_type not in ["application/json", "text/csv"]:
            raise ValueError("Unsupported file type")
        FileHandler(file, queue, repository=self.customer_repository)