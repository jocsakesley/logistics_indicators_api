
from queue import Queue
from flask import Blueprint, jsonify, request
import marshmallow

from src.entities.entities import Service
from src.infra.db import db
from src.models.client_model import ClientModel
from src.models.service_model import CustomerServiceModel
from src.repositories.customer_service_repository import ClientDoesNotExistException, CustomerServiceDoesNotExistException, CustomerServiceRepository
from src.usecase.file_handler import FileHandler


cs_bp = Blueprint('services', __name__)

@cs_bp.get('/services')
def get_all_services():
    try:
        customer_service_repository = CustomerServiceRepository(db.db_session)
        customer_services = customer_service_repository.get_all()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify([customer_service.to_dict() for customer_service in customer_services])

@cs_bp.get('/services/<int:service_id>')
def get_service(service_id):
    try:
        customer_service_repository = CustomerServiceRepository(db.db_session)
        customer_service = customer_service_repository.get(service_id)
    except CustomerServiceDoesNotExistException as e:
        return jsonify({'error': str(e)}), 404
    return jsonify(customer_service.to_dict())

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

@cs_bp.put('/services/<int:customer_service_id>')
def update_service(customer_service_id):
    schema = Service()
    try:
        customer_service_schema = schema.load(request.get_json())
        customer_service_repository = CustomerServiceRepository(db.db_session)
        updated_customer_service = customer_service_repository.update(customer_service_id, customer_service_schema)
    except marshmallow.exceptions.ValidationError as e:
        return jsonify(e.messages), 400
    except CustomerServiceDoesNotExistException as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(updated_customer_service.to_dict())

@cs_bp.post('/services/batch')
def load_clients():
    file = request.files['file']
    FileHandler(file).set_queue(Queue())

    return jsonify({'message': 'ok'})

