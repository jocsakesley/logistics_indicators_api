from abc import ABC, abstractmethod

class AbstractController(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        pass