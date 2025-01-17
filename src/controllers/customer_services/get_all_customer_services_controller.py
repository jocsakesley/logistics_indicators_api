
from flask import jsonify, url_for
from src.controllers.abstract_controller import AbstractController
from src.usecases.customer_services.get_all_customer_service_use_case import GetAllCustomerServiceUseCase


class GetAllCustomerServiceController(AbstractController):
    def __init__(self, get_all_customer_service_use_case: GetAllCustomerServiceUseCase):
        self.get_all_customer_service_use_case = get_all_customer_service_use_case
    
    def handle(self, *args, **kwargs):
        try:
            result = self.get_all_customer_service_use_case.execute(**kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
        return jsonify(result)