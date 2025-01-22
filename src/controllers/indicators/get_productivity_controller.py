

from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.abstract_use_case import AbstractUseCase

class GetProductivityController(AbstractController):
    def __init__(self, get_productivity_use_case: AbstractUseCase):
        self.get_productivity_use_case = get_productivity_use_case
    
    def handle(self, request):
        try:
            results = self.get_productivity_use_case.execute(request)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify(results)