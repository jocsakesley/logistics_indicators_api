

import json
import pytest
from src.entities.entities import Customer
from src.usecases.customers.add_customer_use_case import AddCustomerUseCase
from tests.mocks.mock_repository import MockRepository
from tests.mocks.mock_models import MockCustomerModel
from src.usecases.customers.delete_customer_use_case import DeleteCustomerUseCase
from src.usecases.customers.get_one_customer_use_case import GetOneCustomerUseCase
from src.usecases.customers.update_customer_use_case import UpdateCustomerUseCase
from src.usecases.customers.filter_all_customers_use_case import FilterAllCustomersUseCase
from tests.mocks.mock_request import MockRequest
from src.usecases.exceptions import FilterClientIdException



@pytest.fixture
def customer_model():
    return MockCustomerModel(id=1, 
                            nome="teste", 
                            email="teste@teste.com", 
                            telefone="9999999")


def test_add_custumer_use_case(customer_model):
    repo = MockRepository(customer_model)
    customer_use_case = AddCustomerUseCase(repo)
    result = customer_use_case.execute(customer_model)
    assert isinstance(result, MockCustomerModel)
    assert result == customer_model

def test_delete_customer_use_case(customer_model):
    repo = MockRepository(customer_model)
    customer_use_case = DeleteCustomerUseCase(repo)
    result = customer_use_case.execute(customer_model.id)
    assert result == None

def test_get_one_customer_use_case():
    customer_model = MockCustomerModel(id=5, nome="teste", email="teste@teste.com")
    repo = MockRepository(customer_model)
    customer_use_case = GetOneCustomerUseCase(repo)
    result = customer_use_case.execute(5)
    assert isinstance(result, MockCustomerModel)
    assert result.id == 5
    assert result.nome == "teste"
    assert result.email == "teste@teste.com"
    assert result.telefone == None

def test_update_customer_use_case():
    customer_model = MockCustomerModel(id=5, nome="teste", email="teste@teste.com")
    repo = MockRepository(customer_model)
    customer_use_case = UpdateCustomerUseCase(repo)
    customer = Customer()
    customer_schema = customer.load({"nome": "teste", "email":"teste@teste.com", "telefone": "9999999"})
    result = customer_use_case.execute(5, customer_schema)
    assert isinstance(result, MockCustomerModel)
    assert result.nome == customer_schema.get("nome")
    assert result.email == customer_schema.get("email")
    assert result.telefone == customer_schema.get("telefone")

def test_filter_all_customers_use_case():
    customers_model = [
        MockCustomerModel(id=5, nome="teste", email="teste@teste.com"),
        MockCustomerModel(id=4, nome="teste4", email="teste4@teste.com"),
    ]
    repo = MockRepository(customers_model)
    customer_use_case = FilterAllCustomersUseCase(repo)
    request = MockRequest(args={"limit": 10, "offset": 10})
    result = customer_use_case.execute(request)
    assert result == {'clientes': [
        {'email': 'teste@teste.com', 'id': 5, 'nome': 'teste', "telefone": None},
        {'email': 'teste4@teste.com', 'id': 4, 'nome': 'teste4', "telefone": None}

         ], 'total_por_pagina': 2}


def test_filter_all_exception():
    customer_model = [MockCustomerModel(id=5, nome="teste", email="teste@teste.com")]
    repo = MockRepository(customer_model)
    repo.filter = lambda *args, **kwargs: (_ for _ in ()).throw(FilterClientIdException("Client ID not found"))
    customer_use_case = FilterAllCustomersUseCase(repo)  
    request = MockRequest(args={"limit": 10, "offset": 10})
    with pytest.raises(FilterClientIdException):
        customer_use_case.execute(request) 


def test_filter_get_total():
    customer_model = [
        MockCustomerModel(id=5, nome="teste", email="teste@teste.com"),
        MockCustomerModel(id=4, nome="teste", email="teste@teste.com")
    ]
    repo = MockRepository(customer_model)
    customer_use_case = FilterAllCustomersUseCase(repo)
    request = MockRequest(args={"limit": 10, "offset": 10}, path="total")
    result = customer_use_case.execute(request)
    assert result == {'total': 2}
