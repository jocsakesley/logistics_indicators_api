
from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.customer_services.get_all_customer_service_use_case import GetAllCustomerServiceUseCase


class GetAllCustomerServiceController(AbstractController):
    def __init__(self, get_all_customer_service_use_case: GetAllCustomerServiceUseCase):
        self.get_all_customer_service_use_case = get_all_customer_service_use_case
    
    def handle(self, *args, **kwargs):
        try:
            customer_services = self.get_all_customer_service_use_case.execute()
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify([customer_service.to_dict() for customer_service in customer_services])