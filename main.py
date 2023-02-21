# game packages
# graphics
from Graphics.TextStyles.VersionText import VersionText
from Graphics.TextStyles.TitleText import TitleText

# Entity
from Entity.Character.Character import Character
from BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt

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
VersionText(version)

TitleText("Gentry's Quest")

test_player = BraydenMesserschmidt()

#test_box = Entity(model="cube", scale=(0.2, 0.1, 0), position=(0.1, 0.1, 0), color=color.orange, parent=camera.ui)
#print(test_box.position)
#title2 = TitleText("Big boogas", test_box)
#print(title2.position)

app.run()