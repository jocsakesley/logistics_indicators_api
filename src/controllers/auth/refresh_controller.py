
from flask import jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.abstract_use_case import AbstractUseCase


class RefreshController(AbstractController):
    def __init__(self, refresh_use_case: AbstractUseCase):
        self.refresh_use_case = refresh_use_case

    def handle(self):
        try:
            result = self.refresh_use_case.execute()

        except Exception as e:
            return jsonify({"error": str(e)}), 500


        return jsonify(result)
    
