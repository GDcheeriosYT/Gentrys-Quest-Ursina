from ursina import *

from ...Test import Test
from ...TestMethodButton import TestMethodButton

from Entity.Character.Character import Character
from Content.Characters.TestCharacter import TestCharacter
from utils.Event import Event


class CharacterTest(Test):
    def __init__(self):
        super().__init__(Character)

        # create blank character tracker
        self.character = None

        def create_character():
            if self.character:
                destroy(self.character)
                self.character = TestCharacter(parent=Test.screen)
            else:
                self.character = TestCharacter(parent=Test.screen)

        # tests
        # test spawn button
        event = Event('SpawnCharacterEvent')
        event += create_character  # add event to create character

        self.method_buttons.append(
            TestMethodButton("Spawn character", event)
        )
