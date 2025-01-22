

from abc import ABC, abstractmethod
from typing import List


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def add_all(self, entities):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def filter_by(self, **kwargs):
        pass

    @abstractmethod
    def get_total_count(self):
        pass

    @abstractmethod
    def filter(self, limit, offset, **kwargs):
        pass

    @abstractmethod
    def update(self, id, entity):
        pass

    @abstractmethod
    def sorted_group_by(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, entity):
        pass
