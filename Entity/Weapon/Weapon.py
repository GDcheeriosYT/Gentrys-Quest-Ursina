from ..GameEntityBase import GameEntityBase
from ursina import *
from utils.Event import Event
from typing import Union
from Entity.Buff import Buff


class Weapon(GameEntityBase):
    def __init__(self, buff: Buff = Buff(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_attack = Event('onAttack', 0)
        self.on_equip = Event('onEquip', 0)
        self.on_de_equip = Event('onDeEquip', 0)
        self._equipped_entity = None
        self.buff = buff
        self.buff.handle_value(self.star_rating)
        self._instance = None
        self._attacking = False
        self.texture = None
        self.damage = 0
        self.model = None
        self.enable()
        self.update_stats()

        self.on_level_up += self.update_stats

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def base_attack(self) -> int:
        raise NotImplementedError

    @property
    def base_speed(self) -> int:
        raise NotImplementedError

    @property
    def weapon_type(self) -> str:
        raise NotImplementedError

    @property
    def texture(self) -> str:
        raise NotImplementedError

    @property
    def star_rating(self) -> int:
        raise NotImplementedError

    @property
    def range(self) -> int:
        raise NotImplementedError

    @property
    def equipped_entity(self):
        return self._equipped_entity

    def update_stats(self):
        self.damage = int(self.base_attack + (self.experience.level * 1.2) + (self.star_rating * self.experience.level))
        self.buff.level = self.experience.level
        self.buff.handle_value(self.star_rating)
        self.try_update_equipped_stats()

    def try_update_equipped_stats(self):
        try:
            self._equipped_entity.update_stats
        except AttributeError:
            pass

    def equip(self, entity):
        self._equipped_entity = entity
        self.on_equip()

    def de_equip(self):
        self._equipped_entity = None
        self.on_de_equip()

    def is_ready(self) -> bool:
        return not self._attacking

    def attack(self, direction):
        self._attacking = True
        self.on_attack()
        return self.attack_process(direction)

    def destroy_instance(self):
        destroy(self._instance)
        self._instance = None
        self._attacking = False

    def attack_process(self, direction):
        pass

    def jsonify(self):
        return {
            "buff": self.buff.jsonify(),
            "name": self.name,
            "description": self.description,
            "star rating": self.star_rating,
            "experience": {
                "xp required": self.experience.get_xp_required(self.star_rating),
                "level": self.experience.level,
                "xp": self.experience.xp,
                "previous xp required": 0
            }
        }
