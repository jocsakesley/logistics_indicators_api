
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base_model import BaseModel


class CustomerServiceModel(BaseModel):
    __tablename__ = 'customer_services'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('ClientModel', back_populates='services')
    angel = Column(String(50))
    polo = Column(String(50))
    data_limite = Column(Date)
    data_de_atendimento = Column(DateTime)

    def __init__(self, client_id, angel, polo, data_limite, data_de_atendimento):
        self.client_id = client_id
        self.angel = angel
        self.polo = polo
        self.data_limite = data_limite
        self.data_de_atendimento = data_de_atendimento
    
    def __repr__(self):
        return f'<Service {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'angel': self.angel,
            'polo': self.polo,
            'data_limite': self.data_limite,
            'data_de_atendimento': self.data_de_atendimento
        }