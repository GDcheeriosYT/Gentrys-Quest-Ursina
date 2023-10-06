import GameConfiguration
from Overlays.NotificationsManager import NotificationManager
from GameStates import GameStates
from Online.Presence.Presence import GamePresence
from Content.ContentManager import ContentManager
from GPSystem.GPmain import GPSystem
from Changelog import *
from Audio.AudioSystem import AudioSystem
from utils.ExceptionHandler import ExceptionHandler

GameConfiguration.apply_settings()

state = GameStates.intro
presence = GamePresence() if not GameConfiguration.local_dev_branch else None
rating_program = GPSystem()
state_affected = False
version = "Super Dooper Beta"
user = None
changelog = Changelog()
content_manager = ContentManager()
notification_manager = NotificationManager()
audio_system = AudioSystem(GameConfiguration.music_volume, GameConfiguration.sound_volume)
selected_area = None
testing_screen = None
exception_handler = ExceptionHandler(notification_manager)
language = content_manager.get_language(GameConfiguration.language)


def change_state(new_state: GameStates):
    global state
    global state_affected
    if presence:
        presence.update_status(f"Currently in {new_state.name}")
    state = new_state
    state_affected = False


# changelog
game = ChangeCategory("game")

game.add_change(Change("actually made the game lol", "GDcheerios"))

changelog.add_category(game)
