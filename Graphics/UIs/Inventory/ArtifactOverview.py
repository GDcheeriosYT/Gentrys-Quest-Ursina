from ursina import *

import Game
from utils.StringMethods import *
from .MoneyUpgradeUI import MoneyUpgradeUI
from .ExperienceOverview import ExperienceOverview
from .EntityIcon import EntityIcon
from .ArtifactCollection import ArtifactCollection
from .BlankWeapon import BlankWeapon
from utils.Event import Event


class ArtifactOverview(Entity):
    def __init__(self, artifact, *args, **kwargs):
        super().__init__(
            model=Quad(0.1),
            scale=(1, 1),
            color=color.clear,
            *args,
            **kwargs
        )

        self._entity_picture = Entity(
            model=Quad(0.1),
            texture=artifact.texture,
            position=(0.3, 0.3),
            scale=(0.3, 0.3),
            parent=self
        )

        self._entity_rating = Text(
            repeat_string("*", artifact.star_rating),
            origin=(0.5, 0),
            color=color.gold,
            position=(0.5, -0.6),
            scale=(6, 6),
            parent=self._entity_picture
        )

        self._entity_name = Text(
            artifact.name,
            origin=(0.5, 0),
            position=(0.5, -0.7),
            scale=(6, 6),
            parent=self._entity_picture
        )

        # self._entity_description = Text(
        #     artifact.description,
        #     origin=(0.5, 0.5),
        #     position=(0.5, -0.9),
        #     scale=(4, 4),
        #     parent=self._entity_picture
        # )
        # self._entity_description.wordwrap = 30

        self._entity_experience = ExperienceOverview(artifact, parent=self._entity_picture)

    def update_data(self, artifact):
        self._entity_experience.text = f"level {artifact.experience.level}{f'/{artifact.experience.limit}' if artifact.experience.limit else ''} {int(artifact.experience.xp)}/{artifact.experience.get_xp_required(artifact.star_rating)}xp"
