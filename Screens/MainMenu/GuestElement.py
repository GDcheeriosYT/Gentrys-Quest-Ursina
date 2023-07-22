from ursina import *
from .GuestConfirmBox import GuestConfirmBox
from Graphics.TextStyles.GPText import GPText
from User.User import User


class GuestElement(Button):
    def __init__(self, user: User, menu, *args, **kwargs):
        super().__init__(
            model=Quad(0.07),
            origin=(0, 0),
            color=rgb(77, 77, 77),
            scale=(0.7, 0.1),
            *args,
            **kwargs
        )

        self._user = user
        self._menu = menu
        if user.gp == 0:
            self._username_element = Text(user.username, origin=(-0.5, 0), position=(-0.45, 0), scale=(2, 12), color=color.white, parent=self)
            self._gp_element = Text('unrated', origin=(0.5, 0), position=(0.45, 0), scale=(2, 12), color=color.yellow, parent=self)
        else:
            self._username_element = Text(user.username, origin=(-0.5, 0), position=(-0.45, 0), scale=(2, 12), color=color.white, parent=self)
            self._gp_element = GPText(user.gp, user.ranking[0], origin=(0.5, 0), position=(0.45, 0), scale=(2, 12), parent=self)

    def on_click(self):
        GuestConfirmBox(self._user, self._menu)
