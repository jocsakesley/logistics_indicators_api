
from datetime import datetime
from abc import abstractmethod
from src.infra.db.db import Base


class BaseModel(Base):
    __abstract__ = True

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def load_by_file(self, *args, **kwargs) -> dict:
        pass

    def date_converter(self, date):
        formats = [
            "%d/%m/%Y",
            "%Y-%m-%d %H:%M:%S",
            "%d/%m%Y %H:%M",
            "%d/%m/%Y %H:%M:%S"
        ]
        
        for format in formats:
            try:
                date_obj = datetime.strptime(date, format)
                return date_obj.strftime("%Y%m%d %H%M%S")
            except ValueError:
                continue


if __name__ == "__main__":
    base = BaseModel.convert_date("01/05/2025")
    print(base)