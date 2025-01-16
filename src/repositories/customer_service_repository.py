

from src.infra.db.db import DbSession
from src.models.customer_service_model import CustomerServiceModel
from src.models.client_model import ClientModel
from src.repositories.abstract_repository import AbstractRepository


class CustomerServiceRepository(AbstractRepository):
    def __init__(self, db: DbSession):
        super().__init__()
        self.db = db.db

    def add(self, entity):
        try:
            self.db.add(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
      
    def get(self, customer_service_id):
        try:
            customer_service = self.db.query(CustomerServiceModel).filter_by(id=customer_service_id).first()
        except Exception as e:
            raise e
        return customer_service

    def get_all(self):
        try:
            customer_services = self.db.query(CustomerServiceModel).all()
        except Exception as e:
            raise e
        return customer_services

    def update(self, customer_service_id, entity):
        try:
            updated = self.db.query(CustomerServiceModel).filter_by(id=customer_service_id).update(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return updated

    def delete(self, entity):
        pass


class ClientDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
class CustomerServiceDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)