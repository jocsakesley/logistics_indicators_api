

from flask import Request, jsonify, request
import marshmallow
from sqlalchemy.exc import IntegrityError
from src.controllers.abstract_controller import AbstractController
from src.entities.entities import CustomerService
from src.models.customer_service_model import CustomerServiceModel
from src.usecases.exceptions import CustomerDoesNotExistException
from src.usecases.customer_services.add_customer_service_use_case import AddCustomerServiceUseCase


class AddCustomerServiceController(AbstractController):
    def __init__(self, add_customer_service_use_case: AddCustomerServiceUseCase):
        self.add_customer_service_use_case = add_customer_service_use_case
    
    def handle(self, request: Request):
        try:
            customer_service = CustomerService()
            customer_service_schema = customer_service.load(request.get_json()) 
            customer_service_model = CustomerServiceModel(**customer_service_schema)  
            self.add_customer_service_use_case.execute(customer_service_model)
        except marshmallow.exceptions.ValidationError as e:
            return jsonify(e.messages), 400
        except CustomerDoesNotExistException as e:
            return jsonify({'error': str(e)}), 400

        return jsonify(customer_service_model.to_dict()), 201