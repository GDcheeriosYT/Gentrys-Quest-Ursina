from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class GatitosDeskMat(Artifact):
    def __init__(self, star_rating: int):
        super().__init__(
            star_rating=star_rating,
            texture="deskmat.png"
        )

    @property
    def name(self) -> str:
        return "Gatitos Desk Mat"
