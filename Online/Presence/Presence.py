from pypresence import Presence


class GamePresence:
    def __init__(self):
        self.id = 1115885237910634587
        self.RPC = Presence(self.id)
        self.RPC.connect()
        self.update_status("Loading...")

    def update_status(self, state: str):
        self.RPC.update(
            state=state
        )

    def end(self):
        self.RPC.close()
