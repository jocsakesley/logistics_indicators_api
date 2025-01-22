

from datetime import datetime
from flask import Request

from src.usecases.abstract_use_case import AbstractUseCase


class BaseIndicatorsUseCase(AbstractUseCase):
    def __init__(self):
        self.query = []
        self.results = []

    def execute(self, *args, **kwargs):
        request: Request = kwargs.get("request")
        params = self._extract_params(request)
        if params.get("start_date") and params.get("end_date"):
            params["filters"] = self._build_filters(params.get("start_date"), params.get("end_date"))
        
        self.results = self.repository.sorted_group_by(**params)
        return self.format_results()

    def _extract_params(self, request: Request) -> dict:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        desc = request.args.get("desc", "True")
        
        
        sort_field = request.args.get("sort_field", "total")
        return {
            "start_date": start_date,
            "end_date": end_date,
            "desc": desc,
            "query": self.query,
            "sort_field": sort_field
        }

    def _build_filters(self, start_date: str, end_date: str) -> list:
        return [
            self.repository.model.data_de_atendimento >= datetime.strptime(start_date, '%Y-%m-%d'),
            self.repository.model.data_de_atendimento <= datetime.strptime(end_date, '%Y-%m-%d')
        ]

    def format_results(self) -> list:
        return {}
