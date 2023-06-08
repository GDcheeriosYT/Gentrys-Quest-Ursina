from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .OsuTablet.OsuTablet import OsuTablet


class BraydenMesserschmidtFamily(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                OsuTablet
            ]
        )