
from flask import jsonify
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.exceptions import CustomerDoesNotExistException


class GetOneCustomerController:
    def __init__(self, get_one_customer_use_case: AbstractUseCase):
        self.get_one_customer_use_case = get_one_customer_use_case
    
    def handle(self, id):
        try:
            customer = self.get_one_customer_use_case.execute(id)
        except CustomerDoesNotExistException as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify(customer.to_dict())