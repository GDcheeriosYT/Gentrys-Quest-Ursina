from Overlays.NoficationsManager import NotificationManager
from GameStates import GameStates

state = GameStates.intro
state_affected = False
user = None
intro_music = None
notification_manager = NotificationManager


def change_state(new_state: GameStates):
    global state
    global state_affected
    state = new_state
    state_affected = False
