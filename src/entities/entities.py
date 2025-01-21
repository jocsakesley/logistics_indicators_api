

from marshmallow import Schema, fields


class Customer(Schema):
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    telefone = fields.Str()
    

class CustomerResponse(Customer):
    id = fields.Int()

class CustomerService(Schema):
    id_cliente = fields.Int(required=True)
    angel = fields.Str(required=True)
    polo = fields.Str(required=True)
    data_limite = fields.Date(required=True, 
                              error_messages={
                                  'invalid': 'Date must be in the format YYYY-MM-DD'
                                  })
    data_de_atendimento = fields.DateTime(required=True,
                              error_messages={
                                  'invalid': 'Date must be in the format YYYY-MM-DD HH:MM:SS'
                                  })

class CustomerServiceResponse(CustomerService):
    id = fields.Int()

class UserLogin(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class User(UserLogin):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    


