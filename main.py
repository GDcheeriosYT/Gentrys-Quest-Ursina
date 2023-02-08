# imports
from Game import Game
from Graphics.Screen import Screen
import screeninfo

# screen setup
screen = Screen()
for monitor in screeninfo.get_monitors():
    if monitor.is_primary:
        screen.set_resolution(monitor.width, monitor.height)

# important variables

# initialization
game = Game(screen)
game.start()