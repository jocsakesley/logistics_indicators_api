
from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.customers.get_all_customers_use_case import GetAllCustomersUseCase


class GetAllCustomersController(AbstractController):
    def __init__(self, get_all_customers_use_case: GetAllCustomersUseCase):
        self.get_all_customers_use_case = get_all_customers_use_case
    
    def handle(self, *args, **kwargs):
        try:
            customers = self.get_all_customers_use_case.execute()
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify([customer.to_dict() for customer in customers])