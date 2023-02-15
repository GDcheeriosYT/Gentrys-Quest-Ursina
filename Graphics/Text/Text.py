# game packages
# graphics packages
from .FontStyles import FontStyles

# external packages
import pygame
pygame.init()


class Text:
    def __init__(self, text: str, position: tuple, font_size: int = 12, color: tuple = (0, 0, 0), font: FontStyles = FontStyles.MainFont):
        poopFont = pygame.font.Font(font.get_font_path(), font_size)
        self._text = poopFont.render(text, True, color)
        self._object = self._text.get_rect()
        self._object.x = position[0]
        self._object.y = position[1]

    def get_text(self):
        return self._text

    def get_rect(self):
        return self._object
