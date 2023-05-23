from ..GameEntityBase import GameEntityBase
from ursina import *
from utils.Event import Event
from typing import Union


class Weapon(GameEntityBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_attack = Event('onAttack', 0)
        self.on_equip = Event('onEquip', 0)
        self.on_de_equip = Event('onDeEquip', 0)
        self._equipped_entity = None
        self._instance = None
        self._attacking = False
        self.texture = None
        self.model = None
        self.enable()

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
    def weapon_texture(self) -> str:
        raise NotImplementedError

    @property
    def star_rating(self) -> int:
        raise NotImplementedError

    @property
    def range(self) -> int:
        raise NotImplementedError

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
