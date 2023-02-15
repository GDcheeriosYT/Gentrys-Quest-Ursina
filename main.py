# game packages
# graphics packages

from Graphics.Screen import Screen
from Graphics.Text.TextStyles.MainText import MainText
from Graphics.Text.TextStyles.InfoText import InfoText

# built-in packages
import screeninfo
import os

# external packages
import pygame

# screen setup
screen = Screen(800, 640)
"""for monitor in screeninfo.get_monitors():
    if monitor.is_primary:
        screen.set_resolution(monitor.width, monitor.height)"""

# important variables
version_font_size = screen.get_font_size(2.5)
version = InfoText("Super Dooper Beta", (0, screen.get_height() - version_font_size - 10), version_font_size)


# initialization
running = True
pygame.init()

green_square = pygame.Rect(screen.get_center()[0], screen.get_center()[1], 50, 50)
screen.set_color((199, 199, 199))
screen.draw_rect((0, 255, 0), green_square)

screen.draw_text(version)
screen.draw_text(MainText("Gentry's Quest", (screen.get_horizontal_center(), screen.get_height() // 5), screen.get_font_size(5)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # quit game :)
            running = False


    #green_square.x += 1
    #green_square.update(green_square)
    #screen.draw_rect((0, 255, 0), green_square)
    screen.update()
