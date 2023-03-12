from Entity.Character.Character import Character


class TestCharacter(Character):

    @property
    def name(self) -> str:
        return "Test Character"

    @property
    def star_rating(self) -> int:
        return 1