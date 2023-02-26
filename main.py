# game packages
# graphics
from Graphics.TextStyles.VersionText import VersionText
from Graphics.TextStyles.TitleText import TitleText
from Graphics.Containers.Container import Container

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

title = TitleText("Gentry's Quest", hidden=True)
title.fade_in(1, 2)

def poop():
    BraydenMesserschmidt()

play = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
#play.on_click(poop)
#play.on_click = print("big boogas")
play.on_click = poop

poop_thing = Container((0.5, 0))

#poop_thing.

poop_thing2 = Container((-0.5, 0), background_color=color.rgba(0, 0, 0, 255))

poop_thing3 = Entity(model="quad", color=color.rgba(0, 0, 0, 255))
poop_thing3 = Entity(model="quad", color=color.rgba(0, 0, 0, 50), position=(0, -0.3))

poop_thing4 = Entity(model="quad", scale=(0.5, 0.3), position=(-0.5, 0), parent=camera.ui, color=color.black)
poop_container = Entity(model="quad", scale=(0.25, 0.5), origin=(0.5, 0.5), position=(0.5, 0.5), parent=poop_thing4)


#test_box = Entity(model="cube", scale=(0.2, 0.1, 0), position=(0.1, 0.1, 0), color=color.orange, parent=camera.ui)
#print(test_box.position)

app.run()