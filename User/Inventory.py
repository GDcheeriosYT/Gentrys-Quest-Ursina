from typing import List
from Entity.Character.Character import Character

class Inventory:

    @property
    def characters(self) -> List[Character]:
        characters = []
        return characters

    @characters.setter
    def characters(self, characters: List[Character]) -> None:
        self.characters = characters

    @property
    def weapons(self) -> List[]:
        pass
