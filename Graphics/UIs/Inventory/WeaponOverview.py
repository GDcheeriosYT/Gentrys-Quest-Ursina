from ursina import *

import Game
from utils.StringMethods import *
from .MoneyUpgradeUI import MoneyUpgradeUI
from .ExperienceOverview import ExperienceOverview
from .EntityIcon import EntityIcon
from .ArtifactCollection import ArtifactCollection
from .BlankWeapon import BlankWeapon
from utils.Event import Event


class WeaponOverview(Entity):
    def __init__(self, weapon, *args, **kwargs):
        super().__init__(
            model=Quad(0.1),
            scale=(1, 1),
            color=color.clear,
            *args,
            **kwargs
        )

        self._entity_picture = Entity(
            model=Quad(0.1),
            texture=weapon.texture,
            position=(0.3, 0.3),
            scale=(0.3, 0.3),
            parent=self
        )

        self._entity_rating = Text(
            repeat_string("*", weapon.star_rating),
            origin=(0.5, 0),
            color=color.gold,
            position=(0.5, -0.6),
            scale=(6, 6),
            parent=self._entity_picture
        )

        self._entity_name = Text(
            weapon.name,
            origin=(0.5, 0),
            position=(0.5, -0.7),
            scale=(6, 6),
            parent=self._entity_picture
        )

        # self._entity_description = Text(
        #     weapon.description,
        #     origin=(0.5, 0.5),
        #     position=(0.5, -0.9),
        #     scale=(4, 4),
        #     parent=self._entity_picture
        # )
        # self._entity_description.wordwrap = 30

        self._entity_experience = ExperienceOverview(weapon, parent=self._entity_picture)
        self._entity_stats = Text(
            weapon.stats,
            position=(-0.6, 0),
            origin=(0.5, 0),
            scale=(4, 4),
            parent=self._entity_picture
        )

        self.money_upgrade_ui = MoneyUpgradeUI(
            weapon,
            self.update_data,
            position=(0, -2),
            parent=self._entity_picture
        )

    def update_data(self, weapon):
        self._entity_experience.text = f"level {weapon.experience.level}{f'/{weapon.experience.limit}' if weapon.experience.limit else ''} {int(weapon.experience.xp)}/{weapon.experience.get_xp_required(weapon.star_rating)}xp"
