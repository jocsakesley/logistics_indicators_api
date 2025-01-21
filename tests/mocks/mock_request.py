
class MockRequest:
    args: dict
    path: str
    files: dict
    def __init__(self, args: dict, path: str = "/", files: dict = None):
        self.args = args
        self.path = path
        self.files = files
