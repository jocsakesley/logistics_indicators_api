
from flask import jsonify, url_for
from src.controllers.abstract_controller import AbstractController
from src.usecases.customer_services.filter_all_customer_service_use_case import FilterAllCustomerServiceUseCase


class FilterAllCustomerServiceController(AbstractController):
    def __init__(self, filter_all_customer_service_use_case: FilterAllCustomerServiceUseCase):
        self.filter_all_customer_service_use_case = filter_all_customer_service_use_case
    
    def handle(self, request):
        try:
            result = self.filter_all_customer_service_use_case.execute(request)

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
        return jsonify(result)