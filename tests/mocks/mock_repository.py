from src.repositories.abstract_repository import AbstractRepository


class MockFunc:
    total = None
    avg_time = None
    total_sla = None
    def count(self, value):
        self.total = value
        return self
    def sum(self, value):
        self.total_sla = len(str(value))
        return self
    def label(self, name):
        self.name = name
    def avg(self, value):   
        class TotalSeconds:
            def total_seconds(self):
                return value
            def __str__(self):
                return str(value)
        self.avg_time = TotalSeconds()
        return self
        

class MockRepository(AbstractRepository):
    def __init__(self, model, exception=None):
        self.model = model
        self.total = 0
        self.exception = exception
        self.func = MockFunc()

        if isinstance(self.model, list):
            self.total = len(self.model)

        if self.exception:
            raise self.exception

    def add(self, model):
        return model
    def delete(self, model):
        pass
    def get(self, id: int):
        self.model.id = id
        return self.model
    
    def update(self, id: int, schema):
        self.model.id = id
        for key, value in schema.items():
            setattr(self.model, key, value)
        return self.model 
    
    def filter(self, limit, offset, **dict_args):
        return self.model
    
    def get_total_count(self):
        return self.total
    
    def sorted_group_by(self, **kwargs):
        self.model.total = self.func.total
        self.model.avg_time = self.func.avg_time
        self.model.total_sla = self.func.total_sla
        return [self.model]

    def add_all(self, entities):
        return super().add_all(entities)
    
    def filter_by(self, **kwargs):
        return super().filter_by(**kwargs)