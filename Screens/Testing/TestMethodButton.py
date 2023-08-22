from ursina import *

from utils.Event import Event
from utils.IntMethods import format_seconds


class TestMethodButton(Button):
    def __init__(self, name: str, event: 'Callable', *args, **kwargs):
        super().__init__(
            name,
            scale=(1, 0.05),
            *args,
            **kwargs
        )
        self.name = name
        self.call_event = event
        self.time_text = Text("", origin=(0.5, 0), scale=(3, 20), position=(0.5, 0, -1), parent=self)
        self.time = 0
        self.activated = False
        self.text_entity.scale = (0.1, 1)
        self.disable()

    def on_click(self):
        start_time = time.time()
        self.call_event()
        self.time = time.time() - start_time
        self.time_text.text = format_seconds(self.time)
