

from abc import ABC, abstractmethod
from typing import List
from marshmallow import Schema
from src.models.base_model import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: BaseModel) -> None:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> BaseModel:
        pass

    @abstractmethod
    def get_all(self) -> List[BaseModel]:
        pass

    @abstractmethod
    def update(self, entity: BaseModel) -> None:
        pass

    @abstractmethod
    def delete(self, entity: BaseModel) -> None:
        pass

    @abstractmethod
    def exists(self, entity_id: int) -> bool:
        pass