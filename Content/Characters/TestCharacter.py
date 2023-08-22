from Entity.Character.Character import Character

from .TestSkill import TestSkill


class TestCharacter(Character):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.secondary = TestSkill()
        self.utility = TestSkill()
        self.ultimate = TestSkill()

    @property
    def name(self) -> str:
        return "Test Character"

    @property
    def star_rating(self) -> int:
        return 1
