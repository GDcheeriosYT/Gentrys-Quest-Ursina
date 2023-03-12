from ..GameEntityBase import GameEntityBase


class Weapon(GameEntityBase):

    @property
    def name(self) -> str:
        raise NotImplementedError