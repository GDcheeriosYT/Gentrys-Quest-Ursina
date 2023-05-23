from ursina import *

import Game
from utils.StringMethods import *
from .MoneyUpgradeUI import MoneyUpgradeUI
from .ExperienceOverview import ExperienceOverview
from .EntityIcon import EntityIcon
from .ArtifactCollection import ArtifactCollection
from .BlankWeapon import BlankWeapon
from utils.Event import Event


class CharacterOverview(Entity):
    def __init__(self, character, *args, **kwargs):
        super().__init__(
            model=Quad(0.1),
            scale=(1, 1),
            color=color.clear,
            *args,
            **kwargs
        )

        self._entity_picture = Entity(
            model=Quad(0.1),
            texture=character.texture,
            position=(0.3, 0.3),
            scale=(0.3, 0.3),
            parent=self
        )

        self._entity_rating = Text(
            repeat_string("*", character.star_rating),
            origin=(0.5, 0),
            color=color.gold,
            position=(0.5, -0.6),
            scale=(6, 6),
            parent=self._entity_picture
        )

        self._entity_name = Text(
            character.name,
            origin=(0.5, 0),
            position=(0.5, -0.7),
            scale=(6, 6),
            parent=self._entity_picture
        )

        self._entity_description = Text(
            character.description,
            origin=(0.5, 0.5),
            position=(0.5, -0.9),
            scale=(4, 4),
            parent=self._entity_picture
        )
        self._entity_description.wordwrap = 30

        self._entity_experience = ExperienceOverview(character, parent=self._entity_picture)
        self._entity_stats = Text(
            character.stats,
            position=(-0.6, 0),
            origin=(0.5, 0),
            scale=(4, 4),
            parent=self._entity_picture
        )

        self._entity_equip_button = Button(
                "Equip",
                position=(0, -0.4),
                scale=(0.2, 0.1),
                parent=self
            )
        equip_on_click = Event('onClick', 0)
        equip_on_click += lambda: Game.user.equip_character(character)
        equip_on_click += lambda: self.update_data(character)
        equip_on_click += self._entity_equip_button.disable
        self._entity_equip_button.disable()
        self._entity_equip_button.on_click = equip_on_click

        if Game.user.get_equipped_character() != character:
            self._entity_equip_button.enable()

        self.money_upgrade_ui = MoneyUpgradeUI(
            character,
            self.update_data,
            position=(0, -2),
            parent=self._entity_picture
        )

        if character.weapon:
            self._entity_weapon = EntityIcon(
                character.weapon,
                origin=(-0.5, 0),
                position=(-0.4, 0.4),
                parent=self
            )
            self.weapon_text = Text(
                "Weapon",
                position=(0.6, 0),
                origin=(-0.5, 0),
                scale=(8, 8),
                parent=self._entity_weapon
            )
        else:
            self._entity_weapon = BlankWeapon(
                origin=(0, 0),
                position=(-0.4, 0.4),
                parent=self
            )
            self.weapon_text = Text(
                "Weapon",
                position=(0.6, 0),
                origin=(-0.5, 0),
                scale=(8, 8),
                parent=self._entity_weapon
            )

        self._artifact_collection = ArtifactCollection(
            character,
            origin=(-0.5, 0),
            position=(-0.4, 0.3),
            parent=self
        )

    def update_data(self, character):
        self._entity_stats.text = character.stats
        self._entity_experience.text = f"level {character.experience.level}{f'/{character.experience.limit}' if character.experience.limit else ''} {int(character.experience.xp)}/{character.experience.get_xp_required(character.star_rating)}xp"
