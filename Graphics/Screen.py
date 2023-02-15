import pygame
from .RGB.RGB import RGB
from .Text import Text


class Screen:
    def __init__(self, width: int = 320, height: int = 240):
        self._width = width
        self._height = height
        self._old_width = width
        self._old_height = height
        self._elements = []
        self._screen = pygame.display.set_mode((width, height))

    def update_elements(self):
        width_change = self._width / self._old_width
        height_change = self._width / self._old_height
        for element in self._elements:
            if isinstance(element, pygame.Surface):
                element = pygame.transform.scale(element, (int(element.get_width() * width_change), int(element.get_height() * height_change)))
            elif isinstance(element, pygame.Rect):
                element.width = int(element.width * width_change)
                element.height = int(element.height * height_change)
            elif isinstance(element, pygame.font.Font):
                element.size = int(element.size * height_change)

    def set_resolution(self, width: int, height: int):
        self._old_width = self._width
        self._old_height = self._height
        self._width = width
        self._height = height
        self._screen = pygame.display.set_mode((width, height))
        self.update_elements()

    def set_width(self, width: int):
        self._old_width = self._width
        self._width = width
        self._screen = pygame.display.set_mode((self._width, self._height))
        self.update_elements()

    def set_height(self, height: int):
        self._old_height = self._height
        self._height = height
        self._screen = pygame.display.set_mode((self._width, self._height))
        self.update_elements()

    def get_resolution(self):
        return self._width, self._height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_old_resolution(self):
        return self._old_width, self._old_height

    def get_center(self):
        return self._width // 2, self._height // 2

    def get_horizontal_center(self):
        return self._height // 2

    def get_vertical_center(self):
        return self._width // 2

    def get_font_size(self, coefficient = 1):
        return int((min(self._width, self._height) // 30) * coefficient)

    @staticmethod
    def update():
        pygame.display.update()

    def set_color(self, color: tuple):
        self._screen.fill(color)

    def draw_rect(self, color: tuple, rect: pygame.Rect):
        pygame.draw.rect(self._screen, color, rect)
        self._elements.append(rect)

    def replace_rect(self, rect: pygame.Rect):
        self._elements.remove(rect)
        pygame.display.update(rect)
        self._elements.append(rect)

    def draw_text(self, text: Text):
        self._screen.blit(text.get_text(), text.get_rect())
        self._elements.append(text.get_text())
