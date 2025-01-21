

from abc import ABC, abstractmethod
from typing import List


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def add_all(self, entities: list):
        pass

    @abstractmethod
    def get(self, entity_id: int):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity) -> None:
        pass
