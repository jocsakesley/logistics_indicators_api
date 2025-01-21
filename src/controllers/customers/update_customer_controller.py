

from flask import Request, jsonify
import marshmallow

from src.usecases.exceptions import CustomerDoesNotExistException
from src.entities.entities import Customer
from src.usecases.customer_services.update_customer_service_use_case import UpdateCustomerServiceUseCase
from src.usecases.customers.update_customer_use_case import UpdateCustomerUseCase


class UpdateCustomerController:
    def __init__(self, update_customer_use_case: UpdateCustomerUseCase):
        self.update_customer_use_case = update_customer_use_case

    def handle(self, request: Request, id: int):
        try:
            customer = Customer()
            customer_schema = customer.load(request.get_json())
            updated_customer = self.update_customer_use_case.execute(
                 id, customer_schema
                 )
        except marshmallow.exceptions.ValidationError as e:
            return jsonify(e.messages), 400
        except CustomerDoesNotExistException as e:
            return jsonify({'error': str(e)}), 400
        return jsonify(updated_customer.to_dict())
