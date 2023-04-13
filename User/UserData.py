from typing import List
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact


class UserData:
    def __init__(self):
        self._characters = None
        self._artifacts = None
        self._equipped_character = None
        self._weapons = None

    @property
    def characters(self) -> List[Character]:
        return self._characters

    @property
    def artifacts(self) -> List[Artifact]:
        pass

    #@property
    #def weapons
