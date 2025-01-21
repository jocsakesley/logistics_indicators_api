

from queue import Queue
from flask import Request, jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.customer_services.load_customer_services_use_case import LoadCustomerServicesUseCase


class LoadCustomerServicesController(AbstractController):
    def __init__(self, load_customer_services_use_case: LoadCustomerServicesUseCase):
        self.load_customer_services_use_case = load_customer_services_use_case

    def handle(self, request: Request, queue: Queue):
        try:
            self.load_customer_services_use_case.execute(request, queue)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify({'message': 'received load'}), 202

