
from flask import Request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from src.controllers.abstract_controller import AbstractController
from src.entities.entities import UserLogin
from src.usecases.abstract_use_case import AbstractUseCase



class LoginController(AbstractController):
    def __init__(self, login_use_case: AbstractUseCase):
        self.login_use_case = login_use_case

    def handle(self, request: Request):
        try:
            user_login = UserLogin()
            user_login_schema = user_login.load(request.get_json())
            result = self.login_use_case.execute(user_login_schema)
        except ValidationError as e:
            return jsonify(e.messages), 400
        except IntegrityError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


        return jsonify(result), 200
    
