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
        NotificationManager.notifications[-1].y = y
        NotificationManager.notifications[-1].animate_position(
            (1, NotificationManager.notifications[-1].y, 0),
            duration=2,
            curve=in_expo
        )

        invoke(lambda: NotificationManager.notifications[-1].animate_position(
            (1.5, NotificationManager.notifications[-1].y, 0),
            duration=2,
            curve=out_expo
        ), delay = 5)

        invoke(lambda: NotificationManager.notifications[0].disappear(), delay = 10)
        invoke(lambda: NotificationManager.notifications.pop(0), delay = 15)
