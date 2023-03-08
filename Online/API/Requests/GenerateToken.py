import requests
from ..APIRequest import APIRequest, request_handler


class GenerateToken(APIRequest):
    def __init__(self, server_url: str):
        self.server_url = server_url

    @property
    def name(self) -> str:
        return "GenerateToken"

    @request_handler
    def create_request(self):
        return requests.get(f"{self.server_url}/api/generate-token").text
