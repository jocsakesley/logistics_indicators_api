

from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.indicators.get_productivity_use_case import GetProductivityUseCase


class GetProductivityController(AbstractController):
    def __init__(self, get_productivity_use_case: GetProductivityUseCase):
        self.get_productivity_use_case = get_productivity_use_case
    
    def handle(self, *args, **kwargs):
        try:
            results = self.get_productivity_use_case.execute(**kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify(results)