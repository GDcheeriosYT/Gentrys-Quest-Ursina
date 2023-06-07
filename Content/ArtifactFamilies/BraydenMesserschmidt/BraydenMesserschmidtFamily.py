from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .OsuPen.Artifact import OsuPen


class BraydenMesserschmidtFamily(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                OsuPen
            ]
        )