from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .ElHefe.ElHefe import ElHefe


class HyVee(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                ElHefe
            ]
        )

    @property
    def name(self) -> str:
        return "HyVee"
