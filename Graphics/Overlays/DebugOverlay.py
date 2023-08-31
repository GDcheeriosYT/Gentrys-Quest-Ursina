from ursina import *
import GameConfiguration
from Graphics.Container import Container
import Game
import psutil
from utils.IntMethods import *


class DebugOverlay(Container):
    def __init__(self):
        super().__init__(
            model=Quad(0.06),
            position=window.bottom_right,
            origin=(0.5, -0.5),
            scale=(0.24, 0.3),
            color=rgb(0, 0, 0, 200),
            parent=camera.ui,
            allow_highlighting=False
        )
        self.content = Text(
            "",
            origin=(0.5, 0.5),
            position=(-0.04, 1),
            scale=(2.3, 2.3),
            parent=self
        )
        self.always_on_top = True
        self.pid = os.getpid()
        self.process = psutil.Process(self.pid)

    def update(self):
        self.content.text = f"--game details--\n" \
                            f"{Game.state}\n" \
                            f"notifications: {len(Game.notification_manager.notifications)}\n" \
                            f"musicV: {round(GameConfiguration.music_volume, 2)}\n" \
                            f"soundV: {round(GameConfiguration.sound_volume, 2)}\n" \
                            f"--engine--\n" \
                            f"entities: {window.entity_counter.text}\n" \
                            f"colliders: {window.collider_counter.text}\n" \
                            f"--performance--\n" \
                            f"fps: {window.fps_counter.text}\n"

        self.position = window.bottom_right
