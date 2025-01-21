
class MockRequest:
    args: dict
    path: str
    def __init__(self, args: dict, path: str = "/"):
        self.args = args
        self.path = path