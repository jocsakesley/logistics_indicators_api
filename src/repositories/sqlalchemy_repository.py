

from datetime import datetime
from src.models.base_model import BaseModel
from src.infra.db.db import DbSession
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
            result = self.db.query(self.model).filter_by(id=id).first()
        except Exception as e:
            raise e
        return result

    def filter_by(self, **kwargs):
        try:
            result = self.db.query(self.model).filter_by(**kwargs).first()
        except Exception as e:
            raise e
        return result

    def get_total_count(self):
        try:
            total = self.db.query(self.func.count(self.model.id)).scalar()
        except Exception as e:
            self.db.rollback()
            raise e  
        return total

    def filter(self, limit, offset, **kwargs):
        try:
            filtered = self.db.query(self.model).filter_by(**kwargs).limit(limit).offset(offset).all()
        except Exception as e:
            self.db.rollback()
            raise e
        return filtered
    
    def update(self, id, entity):
        try:
            updated = self.db.query(self.model
                                    ).filter_by(id=id).update(entity)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        return updated

    def sorted_group_by(self, **kwargs):
        try:
            desc = kwargs.get("desc", "True")
            query_params = kwargs.get("query", self.model)
            filters = kwargs.get("filters")
            sort_field = kwargs.get("sort_field")
            
            query = self._build_query(query_params, filters)
            results = query.all()
            self._sort_results(results, sort_field, desc)
        except Exception as e:
            raise e
        return results

    def _build_query(self, query_params, filters):
        query = self.db.query(*query_params).group_by(query_params[0])
        if filters:
            query = query.filter(*filters)
        return query

    def _sort_results(self, results, sort_field, desc):
        results.sort(key=lambda x: getattr(x, sort_field), 
                     reverse=eval(desc.capitalize()))  
    
    def delete(self, entity):
        try:
            self.db.delete(entity)
            self.db.commit()
        except Exception as e:
            raise e


