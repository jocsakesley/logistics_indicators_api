

from flask import jsonify
from src.entities.entities import Client
from src.usecases.exceptions import CustomerDoesNotExistException
from src.controllers.abstract_controller import AbstractController
from src.usecases.customers.delete_customer_use_case import DeleteCustomerUseCase


class DeleteCustomerController(AbstractController):

    def __init__(self, delete_customer_use_case: DeleteCustomerUseCase):
        self.delete_customer_use_case = delete_customer_use_case

    def handle(self, *args, **kwargs):
        try:
            self.delete_customer_use_case.execute(
                 **kwargs
                 )
        except CustomerDoesNotExistException as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify({'message': f'Client id {kwargs.get("id")} deleted'})