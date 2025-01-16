
# from queue import Queue
from queue import Queue
from flask import Blueprint, jsonify, request
import marshmallow

from src.repositories.customer_repository import CustomerRepository
from src.controllers.customer_services.load_customer_services_controller import LoadCustomerServicesController
from src.controllers.customer_services.add_customer_service_controller import AddCustomerServiceController
from src.controllers.customer_services.update_customer_service_controller import UpdateCustomerServiceController
from src.controllers.customer_services.get_all_customer_services_controller import GetAllCustomerServiceController
from src.controllers.customer_services.get_one_customer_service_controller import GetOneCustomerServiceController
from src.entities.entities import Service
from src.infra.db import db
from src.models.client_model import ClientModel
from src.models.customer_service_model import CustomerServiceModel
from src.repositories.customer_service_repository import ClientDoesNotExistException, CustomerServiceDoesNotExistException, CustomerServiceRepository
from src.usecases.file_handler import FileHandler
from src.usecases.customer_services.update_customer_service_use_case import UpdateCustomerServiceUseCase
from src.usecases.customer_services.add_customer_service_use_case import AddCustomerServiceUseCase
from src.usecases.customer_services.get_one_customer_service_use_case import GetOneCustomerServiceUseCase
from src.usecases.customer_services.get_all_customer_service_use_case import GetAllCustomerServiceUseCase
from src.usecases.customer_services.load_customer_services_use_case import LoadCustomerServicesUseCase


cs_bp = Blueprint('services', __name__)


@cs_bp.get('/services')
def get_all_services():
    repository = CustomerServiceRepository(db.DbSession)
    use_case = GetAllCustomerServiceUseCase(repository)
    return GetAllCustomerServiceController(use_case).handle()

@cs_bp.get('/services/<int:customer_service_id>')
def get_service(customer_service_id):
    repository = CustomerServiceRepository(db.DbSession)
    use_case = GetOneCustomerServiceUseCase(repository)
    return GetOneCustomerServiceController(use_case).handle(customer_service_id=customer_service_id)

@cs_bp.post('/services')
def create_service():
    customer_service_repository = CustomerServiceRepository(db.DbSession)
    customer_repository = CustomerRepository(db.DbSession)
    use_case = AddCustomerServiceUseCase(customer_service_repository, customer_repository)
    return AddCustomerServiceController(use_case).handle(request=request.get_json())


@cs_bp.put('/services/<int:customer_service_id>')
def update_service(customer_service_id):
    repository = CustomerServiceRepository(db.DbSession)
    use_case = UpdateCustomerServiceUseCase(repository)
    return UpdateCustomerServiceController(use_case).handle(request=request.get_json(), customer_service_id=customer_service_id)


@cs_bp.post('/services/batch')
async def load_customer_services_thread():
    repository = CustomerServiceRepository(db.DbSession)
    use_case = LoadCustomerServicesUseCase(repository)
    return LoadCustomerServicesController(use_case).handle(file=request.files['file'], queue=Queue())


@cs_bp.post('/services/batch_async')
async def load_customer_services_async():
    file = request.files['file']

    async_file_handler =  AsyncFileHandler(file, Queue())
    await async_file_handler.start_tasks()

    return jsonify({'message': 'ok'})