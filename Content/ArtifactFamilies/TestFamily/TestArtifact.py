import random

from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class TestArtifact(Artifact):
    def __init__(self):
        star_rating = random.randint(1, 5)
        super().__init__(
            star_rating=star_rating,
            texture="Entity/Textures/huh.png"
        )

    @property
    def name(self) -> str:
        return "Test Artifact"
