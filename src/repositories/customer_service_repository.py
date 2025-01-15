

from src.models.service_model import CustomerServiceModel
from src.models.client_model import ClientModel
from src.repositories.abstract_repository import AbstractRepository


class CustomerServiceRepository(AbstractRepository):
    def __init__(self, db):
        super().__init__()
        self.db = db

    def add(self, entity):
        try:
            client = self.db.query(ClientModel).filter_by(id=entity.client_id).first()
            if not client:
                raise ClientDoesNotExistException('Client does not exist')
            self.db.add(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
      

    def get(self, entity_id):
        try:
            customer_service = self.db.query(CustomerServiceModel).filter_by(id=entity_id).first()
            if not customer_service:
                raise CustomerServiceDoesNotExistException('Customer Service does not exist')
            return customer_service
        except Exception as e:
            raise e


    def get_all(self):
        try:
            customer_services = self.db.query(CustomerServiceModel).all()
        except Exception as e:
            raise e
        return customer_services

    def update(self, customer_service_id, entity):
        try:
            self.db.query(CustomerServiceModel).filter_by(id=customer_service_id).update(entity)
            self.db.commit()
            updated_customer_service = self.db.query(CustomerServiceModel).filter_by(id=customer_service_id).first()
        except Exception as e:
            self.db.rollback()
            raise e
        return updated_customer_service

    def delete(self, entity):
        pass

    def exists(self, entity_id):
        pass

class ClientDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
class CustomerServiceDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)