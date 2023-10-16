import requests
from ursina import *

import Game
from Overlays.Notification import Notification
from .API.Requests.GenerateToken import GenerateToken


class ServerConnection:
    def __init__(self, url: str):
        self.url = url
        self.connected = False
        try:
            response = requests.head(url, timeout=1)
            if response.status_code < 400:
                self.token = GenerateToken(self.url).create_request()
                self.connected = True
                Game.notification_manager.add_notification(Notification(Game.language.connected_server, color.green))
        except requests.exceptions.RequestException:
            Game.notification_manager.add_notification(Notification(Game.language.connect_server_error, color.red))
