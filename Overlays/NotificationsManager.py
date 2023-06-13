from ursina import *
from ursina.curve import *

from Overlays.Notification import Notification
from typing import List


class NotificationManager:
    notifications: List[Notification] = []
    notification_tracker: int = 0

    @staticmethod
    def add_nofication(notification: Notification):
        NotificationManager.notifications.append(notification)
        NotificationManager.notification_tracker += 1
        y = 0.5 - NotificationManager.notification_tracker * 0.04

        notification.fade_in(1, 0.2)
        notification.y = y

        def notification_checker():
            if len(NotificationManager.notifications) == 0:
                NotificationManager.notification_tracker = 0

        invoke(lambda: notification.fade_out(0, 1), delay=5)
        destroy(notification, 7)
        invoke(lambda: NotificationManager.notifications.pop(0), delay=7)
        invoke(notification_checker, delay=7)
