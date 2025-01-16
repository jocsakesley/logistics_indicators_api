

from flask import jsonify, request
import marshmallow
from src.repositories.abstract_repository import AbstractRepository
from src.entities.entities import Service
from src.repositories.customer_service_repository import CustomerServiceDoesNotExistException


class UpdateCustomerServiceUseCase:
    def __init__(self, customer_service_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository

    def execute(self, *args, **kwargs):
        customer_service = self.customer_service_repository.update(*args)
        if not customer_service:
            raise CustomerServiceDoesNotExistException('Customer Service does not exist')
        updated_customer_service = self.customer_service_repository.get(args[0])
        return updated_customer_service
        
