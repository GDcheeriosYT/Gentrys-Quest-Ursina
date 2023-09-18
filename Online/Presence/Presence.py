import pypresence.exceptions
from pypresence import Presence


class GamePresence:
    def __init__(self):
        try:
            self.id = 1115885237910634587
            self.RPC = Presence(self.id)
            self.RPC.connect()
            self.update_status("Loading...")
        except pypresence.exceptions.DiscordNotFound:
            print("discord not found")

    def update_status(self, state: str):
        try:
            self.RPC.update(
                state=state
            )
        except Exception as e:
            print(e)

    def end(self):
        self.RPC.close()
