
class MockCustomerModel:

    def __call__(self, *args, **kwds):
        return self

    def __init__(self, id, nome, email, telefone=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

    def load_by_file(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        return self
        
    
class MockCustomerServiceModel:

    def __call__(self, *args, **kwds):
        return self

    def __init__(self, id, id_cliente=None, angel=None, polo=None, data_limite=None, data_de_atendimento=None):
        self.id = id
        self.id_cliente = id_cliente
        self.angel = angel
        self.polo = polo
        self.data_limite = data_limite
        self.data_de_atendimento = data_de_atendimento

        
    def to_dict(self) -> dict:
        return {
                    'id': self.id,
                    'id_cliente': self.id_cliente,
                    'angel': self.angel,
                    'polo': self.polo,
                    'data_limite': self.data_limite,
                    'data_de_atendimento': self.data_de_atendimento
                }
    
    def load_by_file(self, id, id_cliente, angel, polo, data_limite, data_de_atendimento):
        self.id = id
        self.id_cliente = id_cliente
        self.angel = angel
        self.polo = polo
        self.data_limite = data_limite
        self.data_de_atendimento = data_de_atendimento
        return self