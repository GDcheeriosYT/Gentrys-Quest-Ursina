from ursina import *
import os

from User.User import User


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
        for file in os.listdir('Data'):
            user = User(file[:-5])
            user.replace_data(open(file, 'r').read())
            self._user_list.append(user)

    def create_guest(self) -> None:
        self._user_list.append(User(self._username_entry.text))
        self._username_entry.text = "username"
        self.update_list()

    def update_list(self):
        self._guest_entity_list.clear()
        y = 0.25
        for user in self._user_list:
            self._guest_entity_list.append(
                Text(f"{user.username} {user.gp} GP", position=(-0.35, y), scale=(2.5, 1.5), parent=self)
            )
            y -= 0.05
