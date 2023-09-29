from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .GatitosPuzzle.GatitosPuzzle import GatitosPuzzle
from .GatitosUnderwear.GatitosUnderwear import GatitosUnderwear
from .GatitosDeskMat.GatitosDeskMat import GatitosDeskMat


class Gatitos(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                GatitosPuzzle,
                GatitosUnderwear,
                GatitosDeskMat
            ]
        )