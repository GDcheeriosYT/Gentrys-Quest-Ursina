from Entity.Artifact.Artifact import Artifact
from Entity.Buff import Buff


class TestArtifact(Artifact):
    def __init__(self):
        super().__init__(
            image="Entity/Textures/huh.png"
        )

    @property
    def name(self) -> str:
        return "Test Artifact"
