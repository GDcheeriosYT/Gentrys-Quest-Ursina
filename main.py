# game packages
import GameConfiguration
import Game
from GameStates import GameStates


# User
from User.User import User

# screens
from Screens.ScreenManager import ScreenManager

# online packages
from Online.ServerConnection import ServerConnection

# built-in packages
import os

# external packages
from ursina import *
import argparse
import json

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
window.fullscreen = GameConfiguration.fullscreen
window.borderless = False
window.exit_button.visible = False
window.vsync = False
window.exit_button.disable()
window.fps_counter.color = rgb(0, 0, 0)
window.editor_ui.hide()


server_url = "http://localhost" if GameConfiguration.local_dev_branch else "http://gdcheerios.com"

server = ServerConnection(server_url if args.server is None else args.server)

if args.debug:
    Game.state = GameStates.testing
else:
    if GameConfiguration.play_intro:
        Game.state = GameStates.intro
    else:
        Game.state = GameStates.mainMenu

black_thing = Entity(model="quad", scale=(20, 20), color=color.black, position=(0, 0, -3), parent=camera.ui)
destroy(black_thing, 3)

ScreenManager(app)

app.run()
