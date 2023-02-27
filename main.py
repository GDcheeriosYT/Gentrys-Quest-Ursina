# game packages
# graphics
from Graphics.TextStyles.VersionText import VersionText
from Graphics.TextStyles.TitleText import TitleText
from Graphics.Containers.Container import Container

# Entity
from Entity.Character.Character import Character
from BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt

# Screens
from Screens.MainMenu.MainMenu import MainMenu

# external packages
from ursina import *


# initialization
app = Ursina()
app.setBackgroundColor(177, 177, 177)

# window initialization
window.title = "Gentry's Quest"
window.borderless = False
window.exit_button.visible = False
window.exit_button.disable()
window.fps_counter.disable()

# variables
version = "Super Dooper Beta"

main_menu = MainMenu(version)

app.run()