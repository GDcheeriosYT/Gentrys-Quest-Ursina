from ursina import *
from .GuestConfirmBox import GuestConfirmBox


class GuestElement(Button):
    def __init__(self, username: str, gp: int, *args, **kwargs):
        super().__init__(
            model=Quad(0.07),
            origin=(0, 0),
            color=rgb(77, 77, 77),
            scale=(0.7, 0.1),
            *args,
            **kwargs
        )

        self._username_element = Text(username, origin=(-0.5, 0), position=(-0.45, 0), scale=(2, 12), color=color.white, parent=self)
        self._gp_element = Text(f"{gp} GP", origin=(0.5, 0), position=(0.45, 0), scale=(2, 12), color=color.white, parent=self)

    def on_click(self):
        GuestConfirmBox(self._username_element.text)
