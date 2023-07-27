from Entity.Artifact.ArtifactFamily import ArtifactFamily
from .OsuTablet.OsuTablet import OsuTablet
from .PepsiBottle.PepsiBottle import PepsiBottle
from .MdaokaChibiPlush.MadokaChibiPlush import MadokaChibiPlush

from .SetBuffs.twopiece import TwoPiece


class BraydenMesserschmidtFamily(ArtifactFamily):
    def __init__(self):
        super().__init__(
            [
                OsuTablet,
                PepsiBottle,
                MadokaChibiPlush
            ],
            TwoPiece()
        )

    @property
    def name(self) -> str:
        return "Brayden Messerschmidt"
