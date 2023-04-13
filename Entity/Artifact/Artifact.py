from ursina import *
from ..Stats import Stats
from ..Buff import Buff


class Artifact:
    def __init__(self, image: str):
        self._image = Texture(image)
        self._main_attribute = None
        self._attributes = None
        self._star_rating = None

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def main_attribute(self) -> Buff:
        return self._main_attribute

    @property
    def attributes(self) -> list:
        return self._attributes

    @property
    def star_rating(self) -> int:
        return self._star_rating
