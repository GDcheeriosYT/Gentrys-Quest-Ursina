from ursina import *


class Notification(Text):
    def __init__(self, text: str, color: Color = rgb(17, 17, 17)):
        super().__init__(
            text,
            position=(1.5, 0.5),
            origin=(0.8, 0.5),
            parent=camera.ui,
        )
        self.create_background(padding=self.size*2, radius=self.size, color=color)

    def disappear(self) -> None:
        self.fade_out(0, 1)
        invoke(lambda: self.disable(), delay=1.1)
