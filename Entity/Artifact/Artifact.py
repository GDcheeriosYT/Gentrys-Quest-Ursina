from ursina import *
from ..Stats import Stats
from ..Buff import Buff
from ..Experience import Experience


class Artifact:
    def __init__(self, texture: str):
        self._texture = Texture(texture)
        self._main_attribute = Buff("Random")
        self._star_rating = None
        self._attributes = None
        self._experience = None

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

    @star_rating.setter
    def star_rating(self, value):
        self._star_rating = value
        experience = Experience()
        experience.limit = value * 4
        self._experience = experience

    @property
    def texture(self):
        return self._texture

    @property
    def experience(self) -> Experience:
        return self._experience
