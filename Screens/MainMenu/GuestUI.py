from ursina import *
import os
import json

import Game
from User.User import User
from Overlays.NotificationsManager import NotificationManager
from Overlays.Notification import Notification
from .GuestElement import GuestElement


class GuestUI(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model="quad",
            origin=(0, 0),
            scale=(0.95, 0.8),
            color=rgb(117, 117, 117, 0),
            parent=camera.ui,
            *args,
            **kwargs
        )

        self._user_list = []
        self._guest_entity_list = []

        self._bottom_bar = Entity(
            model='quad',
            position=(0, -0.3, -1),
            scale=(0.78, 0.01),
            color=color.black,
            parent=self
        )

        self._add_button = Button(
            "Create Guest",
            position=(0.2, -0.45, -1),
            scale=(0.3, 0.15),
            parent=self
        )

        self._username_entry = InputField("username", position=(-0.165, -0.45, -1), parent=self)
        self._username_entry.scale_x = 0.4
        self._username_entry.scale_y = 0.04

        self._add_button.on_click = self.create_guest

    def load_guest_data(self) -> None:
        self._user_list = []
        for file in os.listdir('Data'):
            user = User(file[:-5], True)
            user.replace_data(open(f"Data/{file}", 'r').read())
            user.calculate_gp()
            self._user_list.append(user)

    def create_guest(self) -> None:
        username = self._username_entry.text
        username_available = True
        for file in os.listdir("Data"):
            if file[:-5] == username:
                username_available = False
                break

        if username_available:
            with open(f"Data/{username}.json", "w+") as user_file:
                user = User(username, True)
                user_file.write(json.dumps(user.user_data.jsonify_data(), indent=4))
                user_file.close()

            self._username_entry.text = "username"
            self.update_list()
        else:
            Game.notification_manager.add_notification(Notification("Username taken", color.red))

    def update_list(self) -> None:
        [destroy(guest) for guest in self._guest_entity_list]
        self.load_guest_data()
        y = 0.25
        if len(self._guest_entity_list) == 0:
            self._guest_entity_list.append(Text("No guest users found...", scale=(2.5, 2.5), origin=(0, 0), position=(0, 0.25), parent=self))

        for user in self._user_list:
            guest_element = GuestElement(user, self, position=(0, y), parent=self)
            self._guest_entity_list.append(
                guest_element
            )
            y -= 0.12
