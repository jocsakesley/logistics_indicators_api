

import json
import pytest
from src.entities.entities import CustomerService
from tests.mocks.mock_repository import MockRepository
from tests.mocks.mock_models import MockCustomerModel, MockCustomerServiceModel
from src.usecases.customers.delete_customer_use_case import DeleteCustomerUseCase
from src.usecases.customers.get_one_customer_use_case import GetOneCustomerUseCase
from src.usecases.customers.update_customer_use_case import UpdateCustomerUseCase
from src.usecases.customers.filter_all_customers_use_case import FilterAllCustomersUseCase
from tests.mocks.mock_request import MockRequest
from src.usecases.exceptions import FilterClientIdException
from src.usecases.customer_services.add_customer_service_use_case import AddCustomerServiceUseCase
from tests.usecases.customers.customers_test import customer_model
from src.usecases.customer_services.get_one_customer_service_use_case import GetOneCustomerServiceUseCase
from src.usecases.customer_services.update_customer_service_use_case import UpdateCustomerServiceUseCase
from src.usecases.customer_services.filter_all_customer_service_use_case import FilterAllCustomerServiceUseCase



@pytest.fixture
def customer_service_model():
    return MockCustomerServiceModel(id=1, 
                            angel="angel", 
                            id_cliente=1, 
                            polo="RN",
                            data_limite="01/01/2025",
                            data_de_atendimento="2025-01-30 00:00:00")


def test_add_costumer_service_use_case(customer_service_model):
    repo = MockRepository(customer_service_model)
    repo_customer = MockRepository(customer_model)
    customer_service_use_case = AddCustomerServiceUseCase(repo, repo_customer)
    result = customer_service_use_case.execute(customer_service_model)
    assert isinstance(result, MockCustomerServiceModel)
    assert result == customer_service_model

def test_get_one_customer_use_case():
    customer_service_model = MockCustomerServiceModel(id=1, 
                                              angel="teste", 
                                              polo="RJ",
                                              data_limite="02/01/2025",
                                              data_de_atendimento="02/10/2025")
    repo = MockRepository(customer_service_model)
    customer_service_use_case = GetOneCustomerServiceUseCase(repo)
    result = customer_service_use_case.execute(1)
    assert isinstance(result, MockCustomerServiceModel)
    assert result.id == 1
    assert result.angel == "teste"
    assert result.polo == "RJ"
    assert result.data_limite == "02/01/2025"
    assert result.data_de_atendimento == "02/10/2025"

def test_update_customer_services_use_case():
    customer_service_model = MockCustomerServiceModel(id=1,
                                                      id_cliente=1, 
                                                        angel="teste", 
                                                        polo="RJ",
                                                        data_limite="02/01/2025",
                                                        data_de_atendimento="02/10/2025")
    repo = MockRepository(customer_service_model)
    customer_service_use_case = UpdateCustomerServiceUseCase(repo)
    customer = CustomerService()
    customer_schema = customer.load({"id_cliente": 2, 
                                     "angel":"teste2", 
                                     "polo": "RN",
                                     "data_de_atendimento": "2025-01-03 00:00:00",
                                     "data_limite": "2025-10-03"
                                     })
    result = customer_service_use_case.execute(5, customer_schema)
    assert isinstance(result, MockCustomerServiceModel)
    assert result.id_cliente == customer_schema.get("id_cliente")
    assert result.angel == customer_schema.get("angel")
    assert result.polo == customer_schema.get("polo")
    assert result.data_de_atendimento == customer_schema.get("data_de_atendimento")
    assert result.data_limite == customer_schema.get("data_limite")

def test_filter_all_customers_use_case(customer_service_model):
    model = [
        customer_service_model,
        customer_service_model,
        customer_service_model,
    ]
    repo = MockRepository(model)
    customer_use_case = FilterAllCustomerServiceUseCase(repo)
    request = MockRequest(args={"limit": 10, "offset": 10})
    result = customer_use_case.execute(request)
    assert result == {'atendimentos': [
        {"id": 1,
        "id_cliente": 1, 
        "angel":"angel", 
        "polo": "RN",
        "data_de_atendimento": "2025-01-30 00:00:00",
        "data_limite": "01/01/2025"
        },
         {"id": 1,
        "id_cliente": 1, 
        "angel":"angel", 
        "polo": "RN",
        "data_de_atendimento": "2025-01-30 00:00:00",
        "data_limite": "01/01/2025"
        },
         {"id": 1,
        "id_cliente": 1, 
        "angel":"angel", 
        "polo": "RN",
        "data_de_atendimento": "2025-01-30 00:00:00",
        "data_limite": "01/01/2025"
        }
        

         ], 'total_por_pagina': 3}


def test_filter_all_customer_services_exception(customer_service_model):
    model = [customer_service_model]
    repo = MockRepository(model)
    repo.filter = lambda *args, **kwargs: (_ for _ in ()).throw(FilterClientIdException("Client ID not found"))
    customer_use_case = FilterAllCustomerServiceUseCase(repo)  
    request = MockRequest(args={"limit": 10, "offset": 10})
    with pytest.raises(FilterClientIdException):
        customer_use_case.execute(request) 


def test_filter_get_total(customer_service_model):
    models = [
        customer_service_model,
        customer_service_model,
        customer_service_model
    ]
    repo = MockRepository(models)
    customer_service_use_case = FilterAllCustomersUseCase(repo)
    request = MockRequest(args={"limit": 10, "offset": 10}, path="total")
    result = customer_service_use_case.execute(request)
    assert result == {'total': 3}
