

from src.models.client_model import ClientModel
from src.repositories.abstract_repository import AbstractRepository
from src.infra.db.db import DbSession


class CustomerRepository(AbstractRepository):
    def __init__(self, db: DbSession):
        super().__init__()
        self.db = db.db
        self.func = db.func

    def add(self, entity):
        try:
            self.db.add(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
      
    def add_all(self, entities):
        try:
            self.db.add_all(entities)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        
    def get(self, customer_id):
        try:
            customer = self.db.query(ClientModel).filter_by(id=customer_id).first()
            if not customer:
                raise CustomerDoesNotExistException('Customer does not exist')
            return customer
        except Exception as e:
            raise e

    def get_all(self):
        try:
            customer = self.db.query(self.func.count(ClientModel.id)).scalar()
        except Exception as e:
            raise e  
        return customer

    def update(self, customer_id, entity):
        try:
            customer = self.db.query(ClientModel).filter_by(id=customer_id).update(entity)
            if not customer:
                raise CustomerDoesNotExistException('Customer does not exist')
            self.db.commit()
            updated_customer = self.db.query(ClientModel).filter_by(id=customer_id).first()
        except Exception as e:
            self.db.rollback()
            raise e
        return updated_customer

    def delete(self, customer_id):
        try:
            customer = self.db.query(ClientModel).filter_by(id=customer_id).first()
            if not customer:
                raise CustomerDoesNotExistException('Customer does not exist')
            self.db.delete(customer)
            self.db.commit()
        except Exception as e:
            raise e
        


class CustomerDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
class CustomerServiceDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)