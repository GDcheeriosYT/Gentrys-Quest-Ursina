from ursina import *
from ..Stats import Stats
from ..Buff import Buff


class Artifact:
    def __init__(self, image: str):
        self._image = Texture(image)
        self._main_attribute = Buff("Random")
        self._attributes = None
        self.star_rating = None

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def main_attribute(self) -> Buff:
        return self._main_attribute

    @property
    def attributes(self) -> list:
        return self._attributes
