
from src.usecases.indicators.get_productivity_use_case import GetProductivityUseCase
from src.usecases.indicators.get_sla_use_case import GetSLAAngelUseCase, GetSLAPoloUseCase
from tests.mocks.mock_models import MockCustomerServiceModel
from tests.mocks.mock_repository import MockRepository
from tests.mocks.mock_request import MockRequest


def test_get_productivity_use_case():
    customer_service_model = MockCustomerServiceModel(id=1, 
                            angel="angel", 
                            id_cliente=1, 
                            polo="RN",
                            data_limite=10,
                            data_de_atendimento=5)
    
    repo = MockRepository(customer_service_model)
    productivity_use_case = GetProductivityUseCase(repo)
    request = MockRequest(args={})
    result = productivity_use_case.execute(request)
    assert result == {'produtividade': [
        {'angel': 'angel', 'produtividade': 17280.0, 'tempo_medio_atendimento': '5', "total_de_atendimentos": 1},
         ]}
    
def test_get_sla_angel_use_case():
    customer_service_model = MockCustomerServiceModel(id=1, 
                            angel="angel", 
                            id_cliente=1, 
                            polo="RN",
                            data_limite=10,
                            data_de_atendimento=5)
    
    repo = MockRepository(customer_service_model)
    sla_angel_use_case = GetSLAAngelUseCase(repo)
    request = MockRequest(args={})
    result = sla_angel_use_case.execute(request)
    assert result == {'sla_angel': [
        {'angel': 'angel', 'sla': '5000.0%', 'total_de_atendimentos': 1, "total_de_atendimentos_no_prazo": 50},
         ]}

def test_get_sla_polo_use_case():
    customer_service_model = MockCustomerServiceModel(id=1, 
                            angel="angel", 
                            id_cliente=1, 
                            polo="RN",
                            data_limite=10,
                            data_de_atendimento=5)
    
    repo = MockRepository(customer_service_model)
    sla_angel_use_case = GetSLAPoloUseCase(repo)
    request = MockRequest(args={})
    result = sla_angel_use_case.execute(request)
    assert result == {'sla_polo': [
        {'polo': 'RN', 'sla': '5000.0%', 'total_de_atendimentos': 1, "total_de_atendimentos_no_prazo": 50},
         ]}