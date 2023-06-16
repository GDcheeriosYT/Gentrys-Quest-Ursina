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
            parent=camera.ui
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
        memory_info = self.process.memory_info()
        memory_usage = psutil.virtual_memory()
        self.content.text = f"--game details--\n" \
                            f"version: {Game.version}\n" \
                            f"{Game.state}\n" \
                            f"{Game.state_affected}\n" \
                            f"notifications: {len(Game.notification_manager.notifications)}\n" \
                            f"volume: {round(GameConfiguration.volume, 2)}\n" \
                            f"fullscreen: {GameConfiguration.fullscreen}\n" \
                            f"extra ui: {GameConfiguration.extra_ui_info}\n" \
                            f"pitch range: {GameConfiguration.random_pitch_range}\n" \
                            f"--engine--\n" \
                            f"entities: {window.entity_counter.text}\n" \
                            f"colliders: {window.collider_counter.text}\n" \
                            f"--performance--\n" \
                            f"fps: {window.fps_counter.text}\n" \
                            f"memory: {format_memory_size(memory_usage.used)}/{format_memory_size(memory_usage.total)}\n" \
                            f"memory available: {format_memory_size(memory_usage.available)}\n" \
                            f"program using: {format_memory_size(memory_info.rss)}"
