from ursina import *
from ursina.curve import *

from Overlays.Notification import Notification
from typing import List


class NotificationManager:
    notifications: List[Notification] = []

    @staticmethod
    def add_nofication(notification: Notification):
        NotificationManager.notifications.append(notification)
        y = 0.55 - len(NotificationManager.notifications) * 0.12
        notification.animate_position(
            (1, y, -2),
            duration=2,
            curve=in_expo
        )

        invoke(lambda: notification.animate_position(
            (1.5, y, -2),
            duration=2,
            curve=out_expo
        ), delay=5)
#
        destroy(notification, 7)
        invoke(lambda: NotificationManager.notifications.pop(0), delay=7)
