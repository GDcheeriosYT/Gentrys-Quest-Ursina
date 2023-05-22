from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class OsuPen(Artifact):
    def __init__(self, star_rating: int):
        super().__init__(
            "Artifact.png",
        )
        self._main_attribute = Buff("CritRate")
        self._star_rating = star_rating

    @property
    def name(self) -> str:
        return "Osu Pen"
