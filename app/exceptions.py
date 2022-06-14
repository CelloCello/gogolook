
class BaseError(Exception):
    def __init__(self, message, status_code=400, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload


class ParamError(BaseError):
    def __init__(self, message, payload=None):
        super().__init__(message, 400, payload)
