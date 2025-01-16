
from datetime import datetime
from abc import abstractmethod
from src.infra.db.db import Base


class BaseModel(Base):
    __abstract__ = True

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @staticmethod
    def convert_date(date: str):
        """Convert date from %d/%m/%Y to %Y-%m-%d format"""
        datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
