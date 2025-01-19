
from flask import Request, jsonify
from src.controllers.abstract_controller import AbstractController
from src.usecases.auth.refresh_use_case import RefreshUseCase



class RefreshController(AbstractController):
    def __init__(self, refresh_use_case: RefreshUseCase):
        self.refresh_use_case = refresh_use_case

    def handle(self):
        try:
            result = self.refresh_use_case.execute()

        except Exception as e:
            return jsonify({"error": str(e)}), 500


        return jsonify(result)
    
