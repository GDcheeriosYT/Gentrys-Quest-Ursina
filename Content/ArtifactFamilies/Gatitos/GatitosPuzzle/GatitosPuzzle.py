from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class GatitosPuzzle(Artifact):
    def __init__(self, star_rating: int):
        super().__init__(
            star_rating=star_rating,
            texture="puzzle.png"
        )

    @property
    def name(self) -> str:
        return "Gatitos Puzzle"
