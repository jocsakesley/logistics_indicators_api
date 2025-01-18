
from datetime import datetime
from flask import Request
from sqlalchemy import case
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.indicators.base_indicators_use_case import BaseIndicatorsUseCase


class GetSLAAngelUseCase(BaseIndicatorsUseCase):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository
        super().__init__()
        self.query = [self.repository.model.angel,
                      self.repository.func.count(self.repository.model.id).label('total'),
                      self.repository.func.avg(
                          self.repository.model.data_limite - self.repository.model.data_de_atendimento
                      ).label('avg_time'),
                      self.repository.func.sum(case(
                          (self.repository.model.data_de_atendimento <= self.repository.model.data_limite, 1
                           ), else_=0)).label('total_sla')
                      ]
    
    def format_results(self):
        return  {"sla_angel":[{
            'angel': result.angel,
            'total_de_atendimentos': result.total,
            'total_de_atendimentos_no_prazo': result.total_sla,
            'sla': f'{round((result.total_sla / result.total)*100, 2)}%'
        } for result in self.results]}

class GetSLAPoloUseCase(BaseIndicatorsUseCase):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository
        super().__init__()
        self.query = [self.repository.model.polo,
                      self.repository.func.count(self.repository.model.id).label('total'),
                      self.repository.func.avg(
                          self.repository.model.data_limite - self.repository.model.data_de_atendimento
                      ).label('avg_time'),
                      self.repository.func.sum(case(
                          (self.repository.model.data_de_atendimento <= self.repository.model.data_limite, 1
                           ), else_=0)).label('total_sla')
                      ]
    
    def format_results(self):
        return  {"sla_polo":[{
            'polo': result.polo,
            'total_de_atendimentos': result.total,
            'total_de_atendimentos_no_prazo': result.total_sla,
            'sla': f'{round((result.total_sla / result.total)*100, 2)}%'
        } for result in self.results]}
