from Gacha.Gacha import Gacha

from Content.Characters.TestCharacter import TestCharacter
from Content.Weapons.Knife.Knife import Knife


class TestGacha(Gacha):
    def __init__(self):
        super().__init__(
            name="Test Gacha",
            characters=[TestCharacter],
            weapons=[Knife]
        )
