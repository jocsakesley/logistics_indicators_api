

from tests.mocks.mock_models import MockCustomerModel


class MockRepository:
    def __init__(self, model, exception=None):
        self.model = model
        self.total = 0
        self.exception = exception

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