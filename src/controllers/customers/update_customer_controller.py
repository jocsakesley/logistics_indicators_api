

from flask import Request, jsonify
import marshmallow

from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerDoesNotExistException
from src.entities.entities import Customer


class UpdateCustomerController:
    def __init__(self, update_customer_use_case: AbstractUseCase):
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
