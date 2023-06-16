from ursina import *
from ursina.prefabs.input_field import InputField

import Game
from Overlays.NotificationsManager import NotificationManager
from Overlays.Notification import Notification


class MoneyUpgradeUI(Entity):
    def __init__(self, entity, update_method, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs
        )

        self.money_input = InputField(
            default_value="0",
            position=(0, 0.2),
            parent=self
        )
        self.money_input.scale_x = 0.5
        self.money_input.scale_y = 0.2
        self.money_input.text_field.scale = (6, 18)

        self.submit_button = Button(
            "Upgrade",
            position=(0, -0.2),
            scale=(1, 0.5),
            parent=self
        )

        self.submit_button.on_click = lambda: self._on_click(entity, update_method)

    def _on_click(self, entity, update_method):
        try:
            amount = int(self.money_input.text)
            if amount > Game.user.user_data.money:
                Game.notification_manager.add_notification(Notification("Can't afford", color=color.red))
            else:
                Game.user.user_data.remove_money(amount)
                entity.add_xp(amount * 10)
                update_method()

        except ValueError:
            Game.notification_manager.add_notification(Notification("This isn't a number", color=color.red))
