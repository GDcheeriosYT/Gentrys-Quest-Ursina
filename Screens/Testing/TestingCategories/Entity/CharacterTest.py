from ursina import *

from ...Test import Test

from Entity.Character.Character import Character
from Content.Characters.TestCharacter import TestCharacter
from utils.Event import Event


class CharacterTest(Test):
    def __init__(self):
        super().__init__(Character)

        # create blank character tracker
        self.character = None
        self.character: TestCharacter

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        def create_character():
            if not self.character:
                self.character = TestCharacter(parent=Test.screen)

        # tests
        # test spawn button
        self.make_button("Create Character", create_character)
        self.get_button(index=0).on_click()
        self.character.can_move = False
        self.character.disable_skills()
        self.character.scale = (0.2, 0.2)

        self.make_button("Spawn Character", self.character.spawn)
        self.make_button("Kill Character", self.character.die)
        self.make_button("Damage Character", lambda: self.character.damage(100))
        self.make_button("Heal Character", lambda: self.character.heal(100))

    def _unload(self):
        destroy(self.character)