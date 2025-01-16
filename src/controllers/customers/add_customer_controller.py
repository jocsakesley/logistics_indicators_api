
from flask import jsonify
import marshmallow
import sqlalchemy
from src.controllers.abstract_controller import AbstractController
from src.entities.entities import Client
from src.models.client_model import ClientModel
from src.usecases.customers.add_customer_use_case import AddCustomerUseCase


class AddCustomerController(AbstractController):
    def __init__(self, add_customer_use_case: AddCustomerUseCase):
        self.add_customer_use_case = add_customer_use_case
    
    def handle(self, *args, **kwargs):
        try:
            schema = Client()
            customer_schema = schema.load(kwargs.get("request")) 
            customer_model = ClientModel(**customer_schema)  
            self.add_customer_use_case.execute(customer_model)
        except marshmallow.exceptions.ValidationError as e:
            return jsonify(e.messages), 400
        except sqlalchemy.exc.IntegrityError:
            return jsonify({'error': 'Email already exists'}), 409
        return jsonify(customer_model.to_dict()), 201