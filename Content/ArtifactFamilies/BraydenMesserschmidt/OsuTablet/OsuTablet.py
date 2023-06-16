from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class OsuTablet(Artifact):
    def __init__(self, star_rating: int):
        super().__init__(
            star_rating=star_rating,
            texture="Artifact.png",
            buff=Buff("CritRate", False)
        )

    @property
    def name(self) -> str:
        return "Osu Tablet"
