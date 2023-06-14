from ursina import *


class Notification(Text):
    def __init__(self, text: str, color: Color = rgb(17, 17, 17)):
        super().__init__(
            text,
            position=(0.5, 0.5, -5),
            origin=(0.6, 0.5),
            color=color,
            parent=camera.ui,
        )
        self.fade_out(0, 0)

    def disappear(self) -> None:
        self.fade_out(0, 1)
        invoke(lambda: self.disable(), delay=1.1)

    def __del__(self):
        print("notificaton eleted 2")

    def on_destroy(self):
        print("notificaton eleted")
