
from queue import Queue
from flask import Blueprint, jsonify, request
import marshmallow

from src.entities.entities import Service
from src.infra.db import db
from src.models.client_model import ClientModel
from src.models.service_model import CustomerServiceModel
from src.repositories.customer_service_repository import ClientDoesNotExistException, CustomerServiceRepository
from src.usecase.file_handler import FileHandler


cs_bp = Blueprint('services', __name__)

@cs_bp.get('/services')
def get_services():
    services = db.db_session.query(CustomerServiceModel).all()
    return jsonify([service.to_dict() for service in services])

@cs_bp.post('/services')
def create_service():
    schema = Service()
    try:
        customer_service_schema = schema.load(request.get_json())
        customer_service_model = CustomerServiceModel(**customer_service_schema)
        customer_service_repository = CustomerServiceRepository(db.db_session)
        customer_service_repository.add(customer_service_model)
    except marshmallow.exceptions.ValidationError as e:
        return jsonify(e.messages), 400
    except ClientDoesNotExistException as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(customer_service_model.to_dict()), 201

@cs_bp.post('/services/batch')
def load_clients():
    file = request.files['file']
    FileHandler(file).set_queue(Queue())

    return jsonify({'message': 'ok'})

