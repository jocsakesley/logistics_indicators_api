from queue import Queue
from flask import Blueprint, Flask, jsonify, request
import marshmallow
import sqlalchemy

from src.infra.db import db
from src.infra.routes.customer_services_routes import cs_bp
from src.entities.entities import Service, Client
from src.models.service_model import CustomerServiceModel
from src.models.client_model import ClientModel
from src.usecase.file_handler import FileHandler

app = Flask(__name__)

db.init_db()

app.register_blueprint(cs_bp, url_prefix='/v1')

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.post('/clients')
def create_client():
    schema = Client()
    try:
        result = schema.load(request.get_json())
        model = ClientModel(**result)
        db.db_session.add(model)
        db.db_session.commit()
    except marshmallow.exceptions.ValidationError as e:
        return jsonify(e.messages), 400
    except sqlalchemy.exc.IntegrityError:
        db.db_session.rollback()
        return jsonify({'error': 'Email already exists'}), 409
    return jsonify(model.to_dict()), 201

@app.get('/clients')
def get_clients():
    clients = db.db_session.query(ClientModel).all()
    return jsonify([client.to_dict() for client in clients])






