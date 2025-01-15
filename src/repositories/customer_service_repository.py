

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

        pass

    def get_all(self):
        pass

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def exists(self, entity_id):
        pass

class ClientDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    