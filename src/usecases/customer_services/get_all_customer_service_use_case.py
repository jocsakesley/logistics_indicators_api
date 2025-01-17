
from src.repositories.customer_service_repository import FilterClientIdException
from src.repositories.abstract_repository import AbstractRepository
from flask import Request, url_for

class GetAllCustomerServiceUseCase:
    def __init__(self, customer_service_repository: AbstractRepository):
        self.customer_service_repository = customer_service_repository

    def execute(self, *args, **kwargs):
        request: Request = kwargs.get("request")
        
        dict_args = {**request.args}

        limit = dict_args.pop("limit", "30")
        offset = dict_args.pop("offset", "0")

        if "total" in request.path.split("/"):
            total = self.customer_service_repository.get_all()
            return {"total": total}

        # if not dict_args:
        #     customer_services = self.customer_service_repository.get_all(limit, offset)
        # else:
        try:
            customer_services = self.customer_service_repository.filter(limit, offset, **dict_args)
        except Exception:
            raise FilterClientIdException(f"Incorret values to parameters {list(dict_args.keys())}") 
        
        new_offset=str(int(offset) + int(limit))
        data = {"atendimentos":[
                        customer_service.to_dict() for customer_service in customer_services
                        ],
                "total_por_pagina": len(customer_services)}
        if len(customer_services) >= int(limit):
            data.update({"proxima_pagina": url_for('services.get_all_customer_services', 
                                                limit=limit,
                                                offset=new_offset,
                                                **dict_args)})
        return data
            
                 

    




