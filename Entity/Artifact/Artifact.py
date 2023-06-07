from ursina import *
from ..Stats import Stats
from typing import List
from ..Buff import Buff
from ..Experience import Experience
from utils.Event import Event


class Artifact:
    def __init__(self, star_rating: int, texture: str, buff: Buff = None):
        self._texture = Texture(texture)
        if not buff:
            self._main_attribute = Buff("Random")
        else:
            self._main_attribute = buff

        self._star_rating = star_rating
        self._attributes = []
        experience = Experience()
        experience.limit = star_rating * 4
        self._experience = experience
        self._main_attribute.handle_value(star_rating)
        if star_rating - 2 > 0:
            for i in range(star_rating - 2):
                self.add_attribute()

        self.on_add_xp = Event('onAddXp', 0)
        self.on_level_up = Event('onLevelUp', 0)
        self.on_level_up += self.new_attribute_check

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def main_attribute(self) -> Buff:
        return self._main_attribute

    @property
    def attributes(self) -> List[Buff]:
        return self._attributes

    @property
    def star_rating(self) -> int:
        return self._star_rating

    @property
    def texture(self):
        return self._texture

    @property
    def experience(self) -> Experience:
        return self._experience

    def new_attribute_check(self):
        if self._experience.level % 4 == 0:
            self.add_attribute()

    def add_xp(self, amount):
        while amount > 0:
            difference = self.experience.get_xp_required(self.star_rating) - self.experience.xp
            if difference > amount:
                self.experience.xp += amount
                amount = 0
            else:
                self.level_up()
                amount -= difference

        self.on_add_xp()

    def level_up(self):
        self.experience.level += 1
        self.experience.xp = 0
        self.on_level_up()

    def add_attribute(self, buff: Buff = None):
        if buff:
            buff = buff
        else:
            buff = Buff()
            buff.handle_value(self.star_rating)

        exists = False
        for attribute in self.attributes:
            if attribute.stat == buff.stat:
                attribute.level_up()
                attribute.handle_value(self.star_rating)
                exists = True

        if not exists:
            self._attributes.append(buff)
