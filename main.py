# game packages
import GameConfiguration

# graphics

# Entity
from Content.Enemies.TestEnemy import TestEnemy
from Content.Characters.TestCharacter import TestCharacter
from Content.Characters.BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt
from Content.ArtifactFamilies.BraydenMesserschmidt.OsuPen.Artifact import OsuPen
from Overlays.NoficationsManager import NotificationManager
from Overlays.Notification import Notification

# screens
from Screens.MainMenu.MainMenu import MainMenu
from Screens.Play.Gameplay import GameplayScreen

# online packages
from Online.ServerConnection import ServerConnection

# external packages
from ursina import *
from ursina.curve import *
import argparse

# initialization
app = Ursina()
app.setBackgroundColor(0, 0, 0)

parser = argparse.ArgumentParser(
    prog="Gentry's Quest",
    description="A game"
)

parser.add_argument("-s", "--server")
args = parser.parse_args()

# window initialization
window.title = "Gentry's Quest"
window.borderless = GameConfiguration.borderless
window.fullscreen = GameConfiguration.fullscreen
window.exit_button.visible = False
window.exit_button.disable()
window.fps_counter.color = rgb(0, 0, 0)
if GameConfiguration.hide_fps: window.fps_counter.disable()

# intro
game_theme = Audio("Audio/GentrysTheme.mp3", loop=True, time=4, volume=0, autoplay=True)
game_theme.fade_in(GameConfiguration.volume, 4.5, delay=0.5, curve=in_sine)
if GameConfiguration.play_intro:
    engine_icon = Entity(model="quad", scale=(0.25, 0.25), texture="Graphics/Textures/ursina_chan_alpha.png", alpha=0, parent=camera.ui)
    engine_info_container = Entity(aplha=0, parent=camera.ui)
    engine_title = Text("ursina engine", alpha=0, origin=(0, 0), position=(0, -0.25), scale=(3, 3), parent=engine_info_container)
    engine_description = Text("open source game engine", origin=(0, 0), alpha=0, position=(0, -0.35), scale=(2, 2), parent=engine_info_container)
    fade_delay = 0.5
    fade_time = 1.5
    invoke(lambda: engine_icon.fade_in(1, fade_time), delay=fade_delay)
    invoke(lambda: engine_title.fade_in(1, fade_time), delay=fade_delay)
    invoke(lambda: engine_description.fade_in(1, fade_time), delay=fade_delay * 4)
    invoke(lambda: engine_icon.fade_in(0, fade_time * 4), delay=fade_delay * 10)
    invoke(lambda: engine_title.fade_in(0, fade_time * 4), delay=fade_delay * 10)
    invoke(lambda: engine_description.fade_in(0, fade_time * 4), delay=fade_delay * 12)

server = ServerConnection("https://gdcheerios.com" if args.server is None else args.server)

invoke(lambda: app.setBackgroundColor(177, 177, 177), delay=13 if GameConfiguration.play_intro else 0)
invoke(lambda: MainMenu(GameConfiguration.version, game_theme), delay=13 if GameConfiguration.play_intro else 0)

app.run()
