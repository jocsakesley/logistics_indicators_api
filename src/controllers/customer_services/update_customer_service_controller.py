

from flask import jsonify
import marshmallow

from src.usecases.exceptions import CustomerServiceDoesNotExistException
from src.entities.entities import CustomerService
from src.usecases.customer_services.update_customer_service_use_case import UpdateCustomerServiceUseCase


class UpdateCustomerServiceController:
    def __init__(self, update_customer_service_use_case: UpdateCustomerServiceUseCase):
        self.update_customer_service_use_case = update_customer_service_use_case

    def handle(self, *args, **kwargs):
        try:
            customer_service = CustomerService()
            customer_service_schema = customer_service.load(kwargs.get("request"))
            updated_customer_service = self.update_customer_service_use_case.execute(
                 kwargs.get("id"), customer_service_schema
                 )
        except marshmallow.exceptions.ValidationError as e:
            return jsonify(e.messages), 400
        except CustomerServiceDoesNotExistException as e:
            return jsonify({'error': str(e)}), 400
        return jsonify(updated_customer_service.to_dict())
