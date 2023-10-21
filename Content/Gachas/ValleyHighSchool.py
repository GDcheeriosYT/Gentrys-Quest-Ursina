from Gacha.Gacha import Gacha

from Content.Characters.BraydenMesserschmidt.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Characters.PhilipMcClure.PhilipMcClure import PhilipMcClure
from Content.Characters.PeteMarks.PeteMarks import PeteMarks

from Content.Weapons.BraydensOsuPen.BraydensOsuPen import BraydensOsuPen
from Content.Weapons.KingsGolfClub.KingsGolfClub import KingsGolfClub


class ValleyHighSchool(Gacha):
    def __init__(self):
        super().__init__(
            name="Valley High School",
            cost=1000,
            characters=[
                BraydenMesserschmidt,
                PhilipMcClure,
                PeteMarks
            ],
            weapons=[
                BraydensOsuPen,
                KingsGolfClub
            ]
        )
