from ..GameEntityBase import GameEntityBase
from ursina import *


class Weapon(GameEntityBase):
    def __init__(self):
        super().__init__()

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def base_attack(self) -> int:
        raise NotImplementedError

    @property
    def weapon_type(self) -> str:
        raise NotImplementedError

    @property
    def weapon_sprite(self) -> Texture:
        raise NotImplementedError
