
from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.abstract_use_case import AbstractUseCase

class FilterAllCustomersController(AbstractController):
    def __init__(self, filter_all_customers_use_case: AbstractUseCase):
        self.filter_all_customers_use_case = filter_all_customers_use_case
    
    def handle(self, request):
        try:
            result = self.filter_all_customers_use_case.execute(request)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify(result)