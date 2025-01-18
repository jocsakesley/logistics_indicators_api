

from abc import ABC, abstractmethod
from typing import List
from marshmallow import Schema
from src.models.base_model import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: BaseModel) -> None:
        pass

    @abstractmethod
    def add_all(self, entities: List[BaseModel]) -> None:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> BaseModel:
        pass

    @abstractmethod
    def update(self, entity: BaseModel) -> None:
        pass

    @abstractmethod
    def delete(self, entity: BaseModel) -> None:
        pass
