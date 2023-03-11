from .API.Requests.GenerateToken import GenerateToken


class ServerConnection:
    def __init__(self, url: str):
        self.url = url
        self.token = GenerateToken(self.url).create_request()
