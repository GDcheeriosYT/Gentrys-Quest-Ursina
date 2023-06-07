from ursina import *
from Graphics.Container import Container
import Game


class DebugOverlay(Container):
    def __init__(self):
        super().__init__(
            model=Quad(0.06),
            position=(0.88, -0.5),
            origin=(0.5, -0.5),
            scale=(0.24, 0.3),
            color=rgb(0, 0, 0, 200),
            parent=camera.ui
        )
        self.content = Text(
            "",
            origin=(0.5, 0.5),
            position=(-0.04, 0.96),
            scale=(2.3, 2.3),
            parent=self
        )
        self.always_on_top = True

    def update(self):
        self.content.text = f"{Game.state}\n" \
                            f"{Game.state_affected}\n" \
                            f"notifications: {len(Game.notification_manager.notifications)}"