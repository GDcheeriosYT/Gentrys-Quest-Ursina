import GameConfiguration
from Overlays.NotificationsManager import NotificationManager
from GameStates import GameStates
from Online.Presence.Presence import GamePresence
from GPSystem.GPmain import GPSystem
from Changelog import *

state = GameStates.intro
# presence = GamePresence()
presence = None
rating_program = GPSystem()
state_affected = False
version = "Super Dooper Beta"
user = None
intro_music = None
changelog = Changelog()
notification_manager = NotificationManager()


def change_state(new_state: GameStates):
    global state
    global state_affected
    if presence:
        presence.update_status(f"Currently in {new_state.name}")
    state = new_state
    state_affected = False


# changelog
shit = ChangeCategory("shit")
game = ChangeCategory("game")

shit.add_change(Change("made changelog :shrug:", "GDcheerios"))
shit.add_change(Change("A really really really really really really really really really really really really really really really really really really really really really really long change", "GDcheerios"))
game.add_change(Change("actually made the game lol", "GDcheerios"))

changelog.add_category(shit)
changelog.add_category(game)
