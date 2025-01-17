
class CustomerDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
class CustomerServiceDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FilterClientIdException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)