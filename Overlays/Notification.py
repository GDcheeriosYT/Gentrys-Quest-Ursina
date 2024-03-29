from ursina import *

from Graphics.GameText import GameText


class Notification(GameText):
    def __init__(self, text: str, color: Color = rgb(17, 17, 17)):
        super().__init__(
            text,
            position=window.top_right,
            origin=(0.6, 0.5),
            color=color,
            parent=camera.ui,
        )
        self.always_on_top = True
        self.fade_out(0, 0)
        print(f"{text} [{color}]")

    def disappear(self) -> None:
        self.fade_out(0, 1)
        invoke(lambda: self.disable(), delay=1.1)
