from ursina import *

import GameConfiguration
from Rules import Rules
from Overlays.NotificationsManager import NotificationManager
from Overlays.Notification import Notification
from GameStates import GameStates
from Online.Presence.Presence import GamePresence
from Content.ContentManager import ContentManager
from GPSystem.GPmain import GPSystem
from Changelog import *
from Audio.AudioSystem import AudioSystem
from utils.ExceptionHandler import ExceptionHandler
from ScoreManager import ScoreManager
from Screens.ScreenManager import ScreenManager

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
rules = Rules()
score_manager = ScoreManager()
language = content_manager.get_language(GameConfiguration.language)
app = None
screen_manager = None


def change_state(new_state: GameStates):
    global state
    global state_affected
    if presence:
        presence.update_status(f"Currently in {new_state.name}")
    state = new_state
    state_affected = False


def reload_screen():
    global notification_manager
    global screen_manager

    notification_manager.add_notification(Notification(language.reloading_screen, color.yellow))
    screen_manager.kill()
    screen_manager = ScreenManager(app)
    invoke(lambda: change_state(GameStates.mainMenu), delay=GameConfiguration.fade_time)


# changelog
game = ChangeCategory("game")

game.add_change(Change("actually made the game lol", "GDcheerios"))

changelog.add_category(game)
