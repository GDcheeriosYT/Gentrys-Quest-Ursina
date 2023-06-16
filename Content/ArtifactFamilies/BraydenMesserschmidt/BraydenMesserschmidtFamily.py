from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .OsuTablet.OsuTablet import OsuTablet
from .PepsiBottle.PepsiBottle import PepsiBottle
from .MdaokaChibiPlush.MadokaChibiPlush import MadokaChibiPlush


class BraydenMesserschmidtFamily(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                OsuTablet,
                PepsiBottle,
                MadokaChibiPlush
            ]
        )