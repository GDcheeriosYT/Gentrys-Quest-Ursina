import GameConfiguration
from Overlays.NotificationsManager import NotificationManager
from GameStates import GameStates
from Online.Presence.Presence import GamePresence


state = GameStates.intro
# presence = GamePresence()
presence = None
state_affected = False
version = "Super Dooper Beta"
user = None
intro_music = None
notification_manager = NotificationManager()


def change_state(new_state: GameStates):
    global state
    global state_affected
    if presence:
        presence.update_status(f"Currently in {new_state.name}")
    state = new_state
    state_affected = False
