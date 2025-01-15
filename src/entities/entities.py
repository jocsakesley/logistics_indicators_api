

from marshmallow import Schema, fields


class Client(Schema):
    nome = fields.Str(required=True)
    email = fields.Email(required=True, unique=True)
    telefone = fields.Str()
    

class ClientResponse(Client):
    id = fields.Int()

class Service(Schema):
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

class ServiceResponse(Service):
    id = fields.Int()


