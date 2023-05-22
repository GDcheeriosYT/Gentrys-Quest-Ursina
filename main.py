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
window.borderless = GameConfiguration.borderless
window.fullscreen = GameConfiguration.fullscreen
window.exit_button.visible = False
window.exit_button.disable()
window.fps_counter.color = rgb(0, 0, 0)
if GameConfiguration.hide_fps: window.fps_counter.disable()

server_url = "http://localhost" if GameConfiguration.local_dev_branch else "https://gdcheerios.com"

server = ServerConnection(server_url if args.server is None else args.server)

Game.user = User("Gay Dude", True)

starter_character = StarterCharacter(Game.user.username)

Game.user.equip_character(starter_character)

Game.user.add_character(starter_character)
Game.user.add_character(BraydenMesserschmidt())
Game.user.add_character(PhilipMcClure())
Game.user.add_character(PeteMarks())


for i in range(15):
    artifact = TestArtifact()
    artifact.star_rating = 5
    Game.user.add_artifact(artifact)

Game.change_state(GameStates.gameplay)


# if GameConfiguration.play_intro:
#     Game.state = GameStates.intro
# else:
#     Game.state = GameStates.mainMenu

ScreenManager(app)

app.run()
