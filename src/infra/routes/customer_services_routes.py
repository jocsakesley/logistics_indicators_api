
# from queue import Queue
import functools
import logging
from queue import Queue
import sys
import time
from flask import Blueprint, request

from src.models.client_model import CustomerModel
from src.controllers.customer_services.load_customer_services_controller import LoadCustomerServicesController
from src.controllers.customer_services.add_customer_service_controller import AddCustomerServiceController
from src.controllers.customer_services.update_customer_service_controller import UpdateCustomerServiceController
from src.controllers.customer_services.filter_all_customer_services_controller import FilterAllCustomerServiceController
from src.controllers.customer_services.get_one_customer_service_controller import GetOneCustomerServiceController
from src.infra.db import db
from src.models.customer_service_model import CustomerServiceModel
from src.repositories.sqlalchemy_repository import SqlAlchemyRepository
from src.usecases.customer_services.update_customer_service_use_case import UpdateCustomerServiceUseCase
from src.usecases.customer_services.add_customer_service_use_case import AddCustomerServiceUseCase
from src.usecases.customer_services.get_one_customer_service_use_case import GetOneCustomerServiceUseCase
from src.usecases.customer_services.filter_all_customer_service_use_case import FilterAllCustomerServiceUseCase
from src.usecases.customer_services.load_customer_services_use_case import LoadCustomerServicesUseCase


cs_bp = Blueprint('customer_services', __name__)


@cs_bp.get('/services')
def filter_all_customer_services():
    repository = SqlAlchemyRepository(db.DbSession, CustomerServiceModel)
    use_case = FilterAllCustomerServiceUseCase(repository)
    return FilterAllCustomerServiceController(use_case).handle(request=request)

@cs_bp.get('/services/total')
def get_total_customer_services():
    repository = SqlAlchemyRepository(db.DbSession, CustomerServiceModel)
    use_case = FilterAllCustomerServiceUseCase(repository)
    return FilterAllCustomerServiceController(use_case).handle(request=request)

@cs_bp.get('/services/<int:id>')
def get_service(id):
    repository = SqlAlchemyRepository(db.DbSession, CustomerServiceModel)
    use_case = GetOneCustomerServiceUseCase(repository)
    return GetOneCustomerServiceController(use_case).handle(id=id)

@cs_bp.post('/services')
def create_service():
    customer_service_repository = SqlAlchemyRepository(db.DbSession, CustomerServiceModel)
    customer_repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = AddCustomerServiceUseCase(customer_service_repository, customer_repository)
    return AddCustomerServiceController(use_case).handle(request=request)


@cs_bp.put('/services/<int:id>')
def update_service(id):
    customer_service_repository = SqlAlchemyRepository(db.DbSession, CustomerServiceModel)
    customer_repository = SqlAlchemyRepository(db.DbSession, CustomerModel)
    use_case = UpdateCustomerServiceUseCase(customer_service_repository, customer_repository)
    return UpdateCustomerServiceController(use_case).handle(request=request, id=id)


@cs_bp.post('/services/batch')
def load_customer_services_thread():
    repository = SqlAlchemyRepository(db.DbSession, CustomerServiceModel)
    use_case = LoadCustomerServicesUseCase(repository)
    return LoadCustomerServicesController(use_case).handle(request=request, queue=Queue())

