


from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.abstract_use_case import AbstractUseCase


class GetSLAController(AbstractController):
    def __init__(self, get_sla_use_case: AbstractUseCase):
        self.get_sla_use_case = get_sla_use_case
    
    def handle(self, *args, **kwargs):
        try:
            results = self.get_sla_use_case.execute(**kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        return jsonify(results)
