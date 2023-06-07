from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .TestArtifact import TestArtifact


class TestFamily(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                TestArtifact
            ]
        )
