from ursina import *
from ..Stats import Stats
from typing import List
from ..Buff import Buff
from ..Experience import Experience
from utils.Event import Event


class Artifact:
    def __init__(self, star_rating: int, texture: str, buff: Buff = None):
        self._texture = texture
        if not buff:
            self._main_attribute = Buff("Random")
        else:
            self._main_attribute = buff

        self._star_rating = star_rating

        self._attributes = []
        if star_rating - 2 > 0:
            for i in range(star_rating - 2):
                self.add_attribute()

        experience = Experience()
        experience.limit = star_rating * 4
        self._experience = experience
        self._main_attribute.handle_value(star_rating)

        self.on_add_xp = Event('onAddXp', 0)
        self.on_level_up = Event('onLevelUp', 0)
        self.on_level_up += self.new_attribute_check
        self.equipped_entity = None

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def main_attribute(self) -> Buff:
        return self._main_attribute

    def set_main_attribute(self, buff: Buff):
        self._main_attribute = buff
        self._main_attribute.level = self._experience.level
        self._main_attribute.handle_value(self._star_rating)

    def set_attributes(self, attributes: List[Buff]):
        self._attributes = attributes

    @property
    def attributes(self) -> List[Buff]:
        return self._attributes

    @property
    def star_rating(self) -> int:
        return self._star_rating

    def set_star_rating(self, star_rating: int):
        self._star_rating = star_rating
        self._main_attribute.handle_value(star_rating)
        for attribute in self._attributes:
            attribute.handle_value(star_rating)

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
        self._main_attribute.level_up()
        self._main_attribute.handle_value(self._star_rating)
        self.on_level_up()

    def check_attribute(self, attribute: Buff):
        if attribute.stat == self.main_attribute.stat and attribute.is_percent == self.main_attribute.is_percent:
            return True

        for other_attribute in self.attributes:
            if attribute.stat == other_attribute.stat and attribute.is_percent == other_attribute.is_percent:
                return True

        return False

    def add_attribute(self, buff: Buff = None):
        if buff:
            buff = buff
        else:
            buff = Buff()
            while self.check_attribute(buff):
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

    def jsonify(self):
        attributes = []
        for attribute in self.attributes:
            attributes.append(attribute.jsonify())

        return {
            "stats": {
                "attributes": attributes,
                "main attribute": self.main_attribute.jsonify()
            },
            "name": self.name,
            "experience": {
                "xp required": self.experience.get_xp_required(self.star_rating),
                "level": self.experience.level,
                "xp": self.experience.xp,
                "previous xp required": 0
            },
            "star rating": self.star_rating
        }
