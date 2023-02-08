import pygame
from .RGB.RGB import RGB


class Screen:
    def __init__(self, width: int = 320, height: int = 240):
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((width, height))

    def set_resolution(self, width: int, height: int):
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((width, height))

    def set_width(self, width: int):
        self._width = width
        pygame.display.set_mode((self._width, self._height))

    def set_height(self, height: int):
        self._height = height
        pygame.display.set_mode((self._width, self._height))

    def set_color(self, rgb: RGB):
        self.screen.fill(rgb)

    def get_resolution(self):
        return self._width, self._height