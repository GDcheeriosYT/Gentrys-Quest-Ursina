from ursina import *

import Game
from Overlays.NotificationsManager import NotificationManager
from Overlays.Notification import Notification


class ExceptionHandler:
    def __init__(self, notification_manager: NotificationManager):
        self._notification_manager = notification_manager

    def handle_exception(self, exception: Exception):
        self._notification_manager.add_notification(Notification(Game.language.get_localized_text(Game.language.exception_occured, exception.__class__.__name__), color.red))
        print(exception)
        traceback.print_exc()

