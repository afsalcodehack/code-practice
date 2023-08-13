class ResponseBase:
    def __init__(self, code, msg):
        self.ErrorCode = code;
        self.ErrorMessage = msg;


class Display:
    def __init__(self, res: ResponseBase):
        self.response = res;

    def print(self):
        print(self.response.ErrorCode)
        print(self.response.ErrorMessage)


