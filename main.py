# game packages
import GameConfiguration
import Game
from GameStates import GameStates

# User
from User.User import User

# TestCharacter
from Content.Characters.TestCharacter import TestCharacter

# screens
from Screens.ScreenManager import ScreenManager

# online packages
from Online.ServerConnection import ServerConnection

# Languages
from Content.Languages.English import English

# external packages
from ursina import *
import argparse

# initialization
app = Ursina()
app.setBackgroundColor(0, 0, 0)
if os.path.isdir('Data'):
    pass
else:
    os.mkdir("Data")

parser = argparse.ArgumentParser(
    prog="Gentry's Quest",
    description="A game"
)

parser.add_argument("-s", "--server")
parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

camera.orthographic = True
camera.fov = 11

# window initialization
window.title = "Gentry's Quest"
window.borderless = False
window.exit_button.disable()
window.editor_ui.hide()

server_url = "http://localhost" if GameConfiguration.local_dev_branch else "http://gdcheerios.com"

if args.debug:
    Game.state = GameStates.testing
    Game.language = English()
    Game.user = User("Test User", True)
    test_character = TestCharacter()
    Game.user.add_character(test_character)
    Game.user.equip_character(test_character)
else:
    server = ServerConnection(server_url if args.server is None else args.server)
    if GameConfiguration.play_intro:
        Game.state = GameStates.intro
    else:
        Game.state = GameStates.mainMenu

# black_thing = Entity(model="quad", scale=(20, 20), color=color.black, position=(0, 0, -3), parent=camera.ui)
# destroy(black_thing, 3)
Game.app = app

Game.screen_manager = ScreenManager(app)

app.run()
