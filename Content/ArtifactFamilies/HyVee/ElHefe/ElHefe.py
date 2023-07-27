from Entity.Artifact.Artifact import Artifact


class ElHefe(Artifact):
    def __init__(self, star_rating: int):
        super().__init__(
            star_rating=star_rating,
            texture="elhefe.png"
        )

    @property
    def name(self) -> str:
        return "El Hefe"

    @property
    def family(self) -> str:
        return "HyVee"

