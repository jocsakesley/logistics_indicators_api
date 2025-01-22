

from flask import Request, jsonify
import marshmallow
from src.controllers.abstract_controller import AbstractController
from src.entities.entities import CustomerService
from src.models.customer_service_model import CustomerServiceModel
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerDoesNotExistException


class AddCustomerServiceController(AbstractController):
    def __init__(self, add_customer_service_use_case: AbstractUseCase):
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