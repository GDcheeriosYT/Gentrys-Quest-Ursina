# game packages
import GameConfiguration
import Game
from GameStates import GameStates


# User
from User.User import User

# graphics

# Entity
from Content.Characters.StarterCharacter.StarterCharacter import StarterCharacter
from Content.Characters.BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen
from Content.Weapons.Knife.Knife import Knife
from Content.Characters.PhilipMcClure.PhilipMcClure import PhilipMcClure
from Content.Characters.PeteMarks.PeteMarks import PeteMarks
from Content.Characters.StarterCharacter.StarterCharacter import StarterCharacter
from Content.ArtifactFamilies.TestFamily.TestArtifact import TestArtifact

# screens
from Screens.ScreenManager import ScreenManager

# online packages
from Online.ServerConnection import ServerConnection

# built-in packages
import os

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
args = parser.parse_args()

camera.orthographic = True
camera.fov = 11

# window initialization
window.title = "Gentry's Quest"
window.fullscreen = GameConfiguration.fullscreen
window.borderless = False
window.exit_button.visible = False
window.aspect_ratio = 1
window.exit_button.disable()
window.fps_counter.color = rgb(0, 0, 0)
window.fps_counter.disable()

server_url = "http://localhost" if GameConfiguration.local_dev_branch else "https://gdcheerios.com"

server = ServerConnection(server_url if args.server is None else args.server)

Game.user = User("Cool Guy", True)

Game.user.add_money(100000)
Game.user.add_weapon(BraydensOsuPen())
Game.user.add_weapon(Knife())

starter_character = StarterCharacter("Guy")

Game.user.add_character(BraydenMesserschmidt())

Game.user.equip_character(starter_character)

Game.user.add_character(starter_character)

Game.change_state(GameStates.gameplay)

# if GameConfiguration.play_intro:
#     Game.state = GameStates.intro
# else:
#     Game.state = GameStates.mainMenu

ScreenManager(app)

app.run()
