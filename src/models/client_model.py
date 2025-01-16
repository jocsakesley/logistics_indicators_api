from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.base_model import BaseModel

class ClientModel(BaseModel):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(50), unique=True)
    telefone = Column(String(11), nullable=True)
    services = relationship('CustomerServiceModel', back_populates='client')

    def __init__(self, nome, email, telefone=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def __repr__(self):
        return f'<Client {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }
