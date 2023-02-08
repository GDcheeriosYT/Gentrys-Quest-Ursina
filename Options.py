# game packages
# graphics packages
from Graphics.Screen import Screen

# external packages
import pygame



class OptionsPanel:
    def __init__(self, screen: Screen):
        self._screen = screen
        resolution = self._screen.get_resolution()
        self._panel = pygame.Rect(-resolution[0], 0, resolution[0]/25, resolution[1])
        self._toggled = False

    def display(self):
        