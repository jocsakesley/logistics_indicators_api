

from queue import Queue
from flask import Blueprint, request
from src.controllers.customers.load_customers_controller import LoadCustomersController
from src.controllers.customers.delete_customer_controller import DeleteCustomerController
from src.controllers.customers.update_customer_controller import UpdateCustomerController
from src.controllers.customers.get_one_customer_controller import GetOneCustomerController
from src.controllers.customers.get_all_customers_controller import GetAllCustomersController
from src.controllers.customers.add_customer_controller import AddCustomerController
from src.repositories.customer_repository import CustomerRepository
from src.infra.db import db
from src.usecases.customers.add_customer_use_case import AddCustomerUseCase
from src.usecases.customers.get_all_customers_use_case import GetAllCustomersUseCase
from src.usecases.customers.get_one_customer_use_case import GetOneCustomerUseCase
from src.usecases.customers.update_customer_use_case import UpdateCustomerUseCase
from src.usecases.customers.delete_customer_use_case import DeleteCustomerUseCase
from src.usecases.customers.load_customers_use_case import LoadCustomersUseCase

customer_bp = Blueprint('customers', __name__)

@customer_bp.post('/customers')
def create_customer():
    repository = CustomerRepository(db.DbSession)
    use_case = AddCustomerUseCase(repository)
    return AddCustomerController(use_case).handle(request=request.get_json())


@customer_bp.get('/customers')
def get_all_clients():
    repository = CustomerRepository(db.DbSession)
    use_case = GetAllCustomersUseCase(repository)
    return GetAllCustomersController(use_case).handle(request=request)

@customer_bp.get('/customers/total')
def get_total_clients():
    repository = CustomerRepository(db.DbSession)
    use_case = GetAllCustomersUseCase(repository)
    return GetAllCustomersController(use_case).handle(request=request)

@customer_bp.get('/customers/<int:customer_id>')
def get_one_client(customer_id):
    repository = CustomerRepository(db.DbSession)
    use_case = GetOneCustomerUseCase(repository)
    return GetOneCustomerController(use_case).handle(customer_id=customer_id)

@customer_bp.put('/customers/<int:customer_id>')
def update_client(customer_id):
    repository = CustomerRepository(db.DbSession)
    use_case = UpdateCustomerUseCase(repository)
    return UpdateCustomerController(use_case).handle(request=request.get_json(), customer_id=customer_id)

@customer_bp.delete('/customers/<int:customer_id>')
def delete_client(customer_id):
    repository = CustomerRepository(db.DbSession)
    use_case = DeleteCustomerUseCase(repository)
    return DeleteCustomerController(use_case).handle(customer_id=customer_id)

@customer_bp.post('/customers/batch')
def load_customer_thread():
    repository = CustomerRepository(db.DbSession)
    use_case = LoadCustomersUseCase(repository)
    return LoadCustomersController(use_case).handle(file=request.files['file'], queue=Queue())
