from abc import ABC, abstractmethod

class AbstractUseCase(ABC):
    
    @abstractmethod
    def execute(*args, **kwargs):
        pass