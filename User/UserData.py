from typing import List
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact


class UserData:
    def __init__(self):
        self._characters = []
        self._artifacts = []
        self._equipped_character = []
        self._weapons = []
        self._money = 0

    @property
    def characters(self) -> List[Character]:
        return self._characters

    @property
    def artifacts(self) -> List[Artifact]:
        pass

    #@property
    #def weapons
