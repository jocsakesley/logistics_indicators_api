

from abc import ABC, abstractmethod
from typing import List
from marshmallow import Schema


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: Schema) -> None:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> Schema:
        pass

    @abstractmethod
    def get_all(self) -> List[Schema]:
        pass

    @abstractmethod
    def update(self, entity: Schema) -> None:
        pass

    @abstractmethod
    def delete(self, entity: Schema) -> None:
        pass

    @abstractmethod
    def exists(self, entity_id: int) -> bool:
        pass