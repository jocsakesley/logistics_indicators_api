
from flask import jsonify
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.exceptions import CustomerServiceDoesNotExistException


class GetOneCustomerServiceController:
    def __init__(self, get_one_customer_service_use_case: AbstractUseCase):
        self.get_one_customer_service_use_case = get_one_customer_service_use_case
    
    def handle(self, id):
        try:
            customer_service = self.get_one_customer_service_use_case.execute(id)
        except CustomerServiceDoesNotExistException as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify(customer_service.to_dict())