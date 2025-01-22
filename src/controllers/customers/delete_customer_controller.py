

from flask import jsonify
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import CustomerDoesNotExistException
from src.controllers.abstract_controller import AbstractController


class DeleteCustomerController(AbstractController):

    def __init__(self, delete_customer_use_case: AbstractUseCase):
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