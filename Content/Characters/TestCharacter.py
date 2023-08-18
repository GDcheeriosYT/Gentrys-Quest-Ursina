from Entity.Character.Character import Character


class TestCharacter(Character):
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def name(self) -> str:
        return "Test Character"

    @property
    def star_rating(self) -> int:
        return 1
