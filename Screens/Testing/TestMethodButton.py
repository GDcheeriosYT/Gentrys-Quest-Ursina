from ursina import *

from utils.Event import Event


class TestMethodButton(Button):
    def __init__(self, name: str, event: Event, *args, **kwargs):
        super().__init__(
            name,
            *args,
            **kwargs
        )
        self.name = name
        self.call_event = event
        self.time = 0
        self.activated = False
        self.disable()

    def on_click(self):
        start_time = time.time()
        self.call_event()
        self.time = time.time() - start_time
        self.text = f"{self.name} {self.time}"
