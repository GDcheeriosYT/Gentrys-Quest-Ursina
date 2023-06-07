from Entity.Character.Character import Character
from .Skills.Pete import Pete
from .Skills.FourEightFourOneFour import FourEightFourOneFour


class PeteMarks(Character):
    def __init__(self):
        super().__init__()

        # stats
        self._stats.crit_rate.points = 3

        # skills
        self.secondary = Pete()
        self.utility = FourEightFourOneFour()
        self.ultimate = Pete()

    @property
    def name(self) -> str:
        return "Pete Marks"

    @property
    def star_rating(self) -> int:
        return 4