

from queue import Queue
from flask import Request, jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.customers.load_customers_use_case import LoadCustomersUseCase


class LoadCustomersController(AbstractController):
    def __init__(self, load_customers_use_case: LoadCustomersUseCase):
        self.load_customers_use_case = load_customers_use_case

    def handle(self, request: Request, queue: Queue):

        try:
            self.load_customers_use_case.execute(request, queue)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        return jsonify({'message': 'received load'}), 202

