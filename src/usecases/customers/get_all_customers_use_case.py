
from src.usecases.exceptions import FilterClientIdException
from src.repositories.abstract_repository import AbstractRepository
from flask import Request, url_for

class GetAllCustomersUseCase:
    def __init__(self, customer_repository: AbstractRepository):
        self.customer_repository = customer_repository

    def execute(self, *args, **kwargs):
        request: Request = kwargs.get("request")
        
        dict_args = {**request.args}

        limit = dict_args.pop("limit", "30")
        offset = dict_args.pop("offset", "0")

        if "total" in request.path.split("/"):
            total = self.customer_repository.get_total_count()
            return {"total": total}

        try:
            customers = self.customer_repository.filter(limit, offset, **dict_args)
        except Exception:
            raise FilterClientIdException(f"Incorret values to parameters {list(dict_args.keys())}") 
        
        new_offset=str(int(offset) + int(limit))
        data = {"clientes":[
                        customer.to_dict() for customer in customers
                        ],
                "total_por_pagina": len(customers)}
        if len(customers) >= int(limit):
            data.update({"proxima_pagina": url_for('customers.get_all_clients', 
                                                limit=limit,
                                                offset=new_offset,
                                                **dict_args)})
        return data
            
                 

    




