
from abc import abstractmethod
from src.infra.db.db import Base


class BaseModel(Base):
    __abstract__ = True

    @abstractmethod
    def to_dict(self) -> dict:
        pass