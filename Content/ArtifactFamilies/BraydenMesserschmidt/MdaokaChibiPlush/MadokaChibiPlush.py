from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class MadokaChibiPlush(Artifact):
    def __init__(self, star_rating: int):
        super().__init__(
            star_rating=star_rating,
            texture="madoka.jpg",
            buff=Buff("CritRate", False)
        )

    @property
    def name(self) -> str:
        return "Madoka Chibi Plush"

    @property
    def family(self) -> str:
        return "Brayden Messerschmidt"
