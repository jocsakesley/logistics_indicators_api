

from src.models.base_model import BaseModel
from src.infra.db.db import DbSession
from src.models.customer_service_model import CustomerServiceModel
from src.repositories.abstract_repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, db: DbSession, model: BaseModel):
        super().__init__()
        self.db = db.db
        self.func = db.func
        self.model = model

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
      
    def get(self, id):
        try:
            customer_service = self.db.query(self.model).filter_by(id=id).first()
        except Exception as e:
            raise e
        return customer_service

    def get_all(self):
        try:
            customer_services = self.db.query(self.func.count(self.model.id)).scalar()
        except Exception as e:
            self.db.rollback()
            raise e  
        return customer_services

    def filter(self, limit, offset, **kwargs):
        try:
            filtered_customer_services = self.db.query(self.model).filter_by(**kwargs).limit(limit).offset(offset).all()
        except Exception as e:
            self.db.rollback()
            raise e
        return filtered_customer_services
    
    def update(self, id, entity):
        try:
            updated = self.db.query(self.model).filter_by(id=id).update(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return updated

    def delete(self, entity):
        try:
            self.db.delete(entity)
            self.db.commit()
        except Exception as e:
            raise e


