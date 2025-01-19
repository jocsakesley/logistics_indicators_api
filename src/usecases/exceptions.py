
class CustomerDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DoesNotExistException(Exception):
    def __init__(self):
        self.message = None
        super().__init__()
    def set_message(self, message):
        self.message = message
        
    
class CustomerServiceDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FilterClientIdException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncompletedDataException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
class ExistentFieldException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)