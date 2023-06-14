from ursina import *
import traceback

import Game
from Overlays.Notification import Notification


def request_handler(func):
    def wrapper(self):
        try:
            result = func(self)
            self.on_success()
            return result
        except Exception:
            self.on_fail()
            print(traceback.format_exc())

        APIRequest.counter += 1

    return wrapper


class APIRequest:
    counter = 1

    @property
    def name(self) -> str:
        """
        name of the APIRequest
        """
        raise NotImplementedError

    def on_fail(self) -> None:
        message = f"{self.name}Request failed"
        print(message)
        Game.notification_manager.add_notification(Notification(message, color.red))

    def on_success(self) -> None:
        message = f"{self.name}Request succeeded"
        print(message)
        Game.notification_manager.add_notification(Notification(message, color.green))
