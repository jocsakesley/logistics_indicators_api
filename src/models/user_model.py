from sqlalchemy import Column, Integer, String
from src.models.base_model import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    email = Column(String(120), unique=True)
    password_hash = Column(String(256))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }