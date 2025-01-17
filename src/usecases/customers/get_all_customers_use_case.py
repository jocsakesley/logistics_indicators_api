
from flask import Request
from src.repositories.abstract_repository import AbstractRepository


class GetAllCustomersUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        request: Request = kwargs.get("request")
        if "total" in request.path.split("/"):
            total = self.customer_repository.get_all()
            return {"total": total}
        customers = self.customer_repository.get_all()
        return [customer.to_dict() for customer in customers]