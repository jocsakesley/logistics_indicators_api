
from flask import jsonify
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from src.controllers.abstract_controller import AbstractController
from src.entities.entities import Customer
from src.models.client_model import CustomerModel
from src.usecases.customers.add_customer_use_case import AddCustomerUseCase


class AddCustomerController(AbstractController):
    def __init__(self, add_customer_use_case: AddCustomerUseCase):
        self.add_customer_use_case = add_customer_use_case
    
    def handle(self, *args, **kwargs):
        try:
            customer = Customer()
            customer_schema = customer.load(kwargs.get("request")) 
            customer_model = CustomerModel(**customer_schema)  
            self.add_customer_use_case.execute(customer_model)
        except ValidationError as e:
            return jsonify(e.messages), 400
        except IntegrityError:
            return jsonify({'error': 'Email already exists'}), 409
        return jsonify(customer_model.to_dict()), 201