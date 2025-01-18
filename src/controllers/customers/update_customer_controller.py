

from flask import jsonify
import marshmallow

from src.usecases.exceptions import CustomerServiceDoesNotExistException
from src.entities.entities import Client, Service
from src.usecases.customer_services.update_customer_service_use_case import UpdateCustomerServiceUseCase
from src.usecases.customers.update_customer_use_case import UpdateCustomerUseCase


class UpdateCustomerController:
    def __init__(self, update_customer_use_case: UpdateCustomerUseCase):
        self.update_customer_use_case = update_customer_use_case

    def handle(self, *args, **kwargs):
        try:
            schema = Client()
            customer_schema = schema.load(kwargs.get("request"))
            updated_customer = self.update_customer_use_case.execute(
                 kwargs.get("id"), customer_schema
                 )
        except marshmallow.exceptions.ValidationError as e:
            return jsonify(e.messages), 400
        except CustomerServiceDoesNotExistException as e:
            return jsonify({'error': str(e)}), 400
        return jsonify(updated_customer.to_dict())
