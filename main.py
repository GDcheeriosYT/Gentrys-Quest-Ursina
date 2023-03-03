# game packages
# graphics
from Graphics.TextStyles.VersionText import VersionText
from Graphics.TextStyles.TitleText import TitleText
from Graphics.Containers.Container import Container

# Entity
from Entity.Character.Character import Character
from BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt

# screens
from Screens.Play.Gameplay import GameplayScreen

# external packages
from ursina import *
import argparse

# initialization
app = Ursina()
app.setBackgroundColor(177, 177, 177)

parser = argparse.ArgumentParser(
    prog="Gentry's Quest",
    description="A game"
)

parser.add_argument("-u", "--username")
parser.add_argument("-p", "--password")
parser.add_argument("-s", "--server")
parser.add_argument("-c", "--character")
args = parser.parse_args()

# window initialization
window.title = "Gentry's Quest"
window.borderless = False
window.exit_button.visible = False
window.exit_button.disable()
window.fps_counter.disable()

# variables
version = "Super Dooper Beta"

def gameplay_loader():
    character = BraydenMesserschmidt()
    gameplay_screen = GameplayScreen(character)


title = TitleText("Gentry's Quest", hidden=True)
title.fade_in(1, 2)
version = VersionText(version)
play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
play_button.on_click = gameplay_loader
settings_button = Button("Settings", position=(0, -0.2), scale=(0.2, 0.05))


app.run()