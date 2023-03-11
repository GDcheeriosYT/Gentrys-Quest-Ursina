import requests
from ..APIRequest import APIRequest, request_handler


class Login(APIRequest):
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.data = None

    @property
    def name(self) -> str:
        return "Login"

    @request_handler
    def create_request(self):
        self.data = requests.post(f"{self.server_url}/api/login").json()["metadata"]["Gentrys Quest Data"]