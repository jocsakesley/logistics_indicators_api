

from flask import Request, jsonify
import marshmallow

from src.usecases.abstract_use_case import AbstractUseCase
from src.entities.entities import CustomerService


class UpdateCustomerServiceController:
    def __init__(self, update_customer_service_use_case: AbstractUseCase):
        self.update_customer_service_use_case = update_customer_service_use_case

    def handle(self, request: Request, id: int):
        try:
            customer_service = CustomerService()
            customer_service_schema = customer_service.load(request.get_json())
            updated_customer_service = self.update_customer_service_use_case.execute(
                 id, customer_service_schema
                 )
        except marshmallow.exceptions.ValidationError as e:
            return jsonify(e.messages), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        return jsonify(updated_customer_service.to_dict())
