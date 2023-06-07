from ursina import *
from ursina.curve import *

from Overlays.Notification import Notification
from typing import List


class NotificationManager:
    notifications: List[Notification] = []

    @staticmethod
    def add_nofication(notification: Notification):
        NotificationManager.notifications.append(notification)
        y = 0.5 - len(NotificationManager.notifications) * 0.04

        notification.fade_in(1, 0.2)
        notification.y = y

        invoke(lambda: notification.fade_out(0, 1), delay=5)
        destroy(notification, 7)
        invoke(lambda: NotificationManager.notifications.pop(0), delay=7)
