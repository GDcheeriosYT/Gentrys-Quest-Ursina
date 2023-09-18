from ursina import *

from Overlays.NotificationsManager import NotificationManager
from Overlays.Notification import Notification


class ExceptionHandler:
    def __init__(self, notification_manager: NotificationManager):
        self._notification_manager = notification_manager

    def handle_exception(self, exception: Exception):
        self._notification_manager.add_notification(Notification(f"A {exception.__class__.__name__} has occurred...", color.red))
        print(exception)
        traceback.print_exc()

