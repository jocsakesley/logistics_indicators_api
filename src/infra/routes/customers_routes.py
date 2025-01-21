

from queue import Queue
from flask import Blueprint, request
from src.models.client_model import CustomerModel
from src.repositories.sqlalchemy_repository import SqlAlchemyRepository
from src.controllers.customers.load_customers_controller import LoadCustomersController
from src.controllers.customers.delete_customer_controller import DeleteCustomerController
from src.controllers.customers.update_customer_controller import UpdateCustomerController
from src.controllers.customers.get_one_customer_controller import GetOneCustomerController
from src.controllers.customers.filter_all_customers_controller import FilterAllCustomersController
from src.controllers.customers.add_customer_controller import AddCustomerController
from src.infra.db import db
from src.usecases.customers.add_customer_use_case import AddCustomerUseCase
from src.usecases.customers.filter_all_customers_use_case import FilterAllCustomersUseCase
from src.usecases.customers.get_one_customer_use_case import GetOneCustomerUseCase
from src.usecases.customers.update_customer_use_case import UpdateCustomerUseCase
from src.usecases.customers.delete_customer_use_case import DeleteCustomerUseCase
from src.usecases.customers.load_customers_use_case import LoadCustomersUseCase

customer_bp = Blueprint('customers', __name__)

@customer_bp.post('/customers')
def create_customer():
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = AddCustomerUseCase(repository)
    return AddCustomerController(use_case).handle(request=request.get_json())


@customer_bp.get('/customers')
def get_all_clients():
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = FilterAllCustomersUseCase(repository)
    return FilterAllCustomersController(use_case).handle(request=request)

@customer_bp.get('/customers/total')
def get_total_clients():
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = FilterAllCustomersUseCase(repository)
    return FilterAllCustomersController(use_case).handle(request=request)

@customer_bp.get('/customers/<int:id>')
def get_one_client(id):
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = GetOneCustomerUseCase(repository)
    return GetOneCustomerController(use_case).handle(id)

@customer_bp.put('/customers/<int:id>')
def update_client(id):
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = UpdateCustomerUseCase(repository)
    return UpdateCustomerController(use_case).handle(request=request, id=id)

@customer_bp.delete('/customers/<int:id>')
def delete_client(id):
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = DeleteCustomerUseCase(repository)
    return DeleteCustomerController(use_case).handle(id=id)

@customer_bp.post('/customers/batch')
def load_customer_thread():
    repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = LoadCustomersUseCase(repository)
    return LoadCustomersController(use_case).handle(request=request, queue=Queue())
