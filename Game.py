# game packages
# graphics packages
from Graphics.Screen import Screen
from Graphics.RGB.ColorChannel import ColorChannel
from Graphics.RGB.RGB import RGB
from Graphics.Screen import Screen

# built-in packages
import sys

# external packages
import pygame

class Game:
    def __init__(self, screen: Screen):
        self.screen = screen

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()