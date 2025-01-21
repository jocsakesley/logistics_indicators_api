
from flask import jsonify
from src.usecases.exceptions import CustomerDoesNotExistException
from src.usecases.customer_services.get_one_customer_service_use_case import GetOneCustomerServiceUseCase
from src.usecases.customers.get_one_customer_use_case import GetOneCustomerUseCase


class GetOneCustomerController:
    def __init__(self, get_one_customer_use_case: GetOneCustomerUseCase):
        self.get_one_customer_use_case = get_one_customer_use_case
    
    def handle(self, id):
        try:
            customer = self.get_one_customer_use_case.execute(id)
        except CustomerDoesNotExistException as e:
            return jsonify({'error': str(e)}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify(customer.to_dict())