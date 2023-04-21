from typing import List
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon
from Entity.Artifact.Artifact import Artifact


class Inventory:
    def ___init__(self):
        self._characters = []
        self._weapons = []
        self._artifacts = []
        self._money = 0

    @property
    def characters(self) -> List[Character]:
        return self._characters

    @property
    def weapons(self) -> List[Weapon]:
        return self._weapons

    @property
    def artifacts(self) -> List[Artifact]:
        return self._artifacts
