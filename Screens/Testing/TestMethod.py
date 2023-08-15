from utils.Event import Event


class TestMethod:
    def __init__(self, name: str, event: Event):
        self.name = name
        self.call_event = event

    def __call__(self):
        print("I was called")
