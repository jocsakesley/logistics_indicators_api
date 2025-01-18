
from datetime import datetime
from flask import Request
from src.repositories.abstract_repository import AbstractRepository
from src.usecases.indicators.base_indicators_use_case import BaseIndicatorsUseCase


class GetProductivityUseCase(BaseIndicatorsUseCase):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository
        super().__init__()
        self.query = [self.repository.model.angel,
                    self.repository.func.count(self.repository.model.id).label('total'),
                    self.repository.func.avg(
                        self.repository.model.data_limite - self.repository.model.data_de_atendimento
                    ).label('avg_time')]
    
    def format_results(self):
        return  {"produtividade":[{
            'angel': result.angel,
            'total_de_atendimentos': result.total,
            'tempo_medio_atendimento': str(result.avg_time),
            'produtividade': round(result.total / (result.avg_time.total_seconds() / 86400), 2)
        } for result in self.results]}


