
from flask import Request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from src.models.user_model import UserModel
from src.controllers.abstract_controller import AbstractController
from src.entities.entities import User
from src.usecases.auth.register_user_case import RegisterUseCase
from src.usecases.exceptions import ExistentFieldException


class RegisterController(AbstractController):
    def __init__(self, register_use_case: RegisterUseCase):
        self.register_use_case = register_use_case

    def handle(self, *args, **kwargs):
        request: Request = kwargs.get("request")
        try:
            user = User()
            user_schema = user.load(request.get_json())
            user_model = UserModel(**user_schema)
            self.register_use_case.execute(user_model)
        except ValidationError as e:
            return jsonify(e.messages), 400
        except IntegrityError as e:
            return jsonify({"error": str(e)}), 400
        except ExistentFieldException as e:
            return jsonify({"error": "User already exists"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


        return user_model.to_dict(), 201
    
