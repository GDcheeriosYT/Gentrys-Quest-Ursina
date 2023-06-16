from ursina import *

from Overlays.Notification import Notification
from typing import List


class NotificationManager:
    def __init__(self):
        self.notifications: List[Notification] = []
        self.notification_tracker: int = 0

    def add_notification(self, notification: Notification):
        self.notifications.append(notification)
        self.notification_tracker += 1
        y = 0.5 - self.notification_tracker * 0.04

        notification.fade_in(1, 0.2)
        notification.y = y

        def notification_checker():
            if len(self.notifications) == 0:
                self.notification_tracker = 0

        invoke(lambda: notification.fade_out(0, 1), delay=3)
        destroy(notification, 5)
        invoke(lambda: self.notifications.pop(0), delay=5)
        invoke(notification_checker, delay=5)
