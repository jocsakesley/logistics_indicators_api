
from src.usecases.abstract_use_case import AbstractUseCase
from src.usecases.shared.exceptions import FilterClientIdException
from src.repositories.abstract_repository import AbstractRepository
from flask import Request, url_for

class FilterAllCustomerServiceUseCase(AbstractUseCase):
    def __init__(self, customer_service_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository

    def execute(self, request: Request):        
        dict_args = self._get_request_args(request)
        limit, offset = self._get_pagination_params(dict_args)

        limit = dict_args.pop("limit", "30")
        offset = dict_args.pop("offset", "0")

        if self._is_total_request(request):
            return self._get_total_count_response()
        
        customer_services = self._filter_customer_services(dict_args, limit, offset)
        return self._build_response(customer_services, limit, offset, dict_args)
            
    def _filter_customer_services(self, dict_args, limit, offset):
        try:
            return self.customer_service_repository.filter(limit, offset, **dict_args)
        except Exception:
            raise FilterClientIdException(f"Incorrect values for parameters {list(dict_args.keys())}")
             
    def _get_request_args(self, request: Request):
        return {**request.args}

    def _get_pagination_params(self, dict_args):
        limit = dict_args.pop("limit", "30")
        offset = dict_args.pop("offset", "0")
        return limit, offset
    
    def _is_total_request(self, request: Request):
        return "total" in request.path.split("/")

    def _get_total_count_response(self):
        total = self.customer_service_repository.get_total_count()
        return {"total": total}
    

    def _build_response(self, customer_services, limit, offset, dict_args):
        new_offset = str(int(offset) + int(limit))
        data = {
            "atendimentos": [customer_service.to_dict() for customer_service in customer_services],
            "total_por_pagina": len(customer_services)
        }
        if len(customer_services) >= int(limit):
            data.update({
                "proxima_pagina": url_for('customer_services.filter_all_customer_services', limit=limit, offset=new_offset, **dict_args)
            })
        return data



