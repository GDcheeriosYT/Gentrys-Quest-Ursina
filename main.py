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
from Screens.MainMenu.MainMenu import MainMenu

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

MainMenu()


app.run()