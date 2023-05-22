from ursina import *

import Game
from .InvButton import InvButton
from .EntityIcon import EntityIcon


class Inventory(Entity):
    def __init__(self):
        super().__init__(
            model=Quad(radius=0.1),
            scale=(1.2, 0.75),
            color=rgb(117, 117, 117),
            parent=camera.ui
        )
        self.player = Game.user.user_data

        self.current_page_listings = []

        self._characters_button = InvButton(
            "Characters",
            position=(-0.35, 0.6),
            parent=self
        )
        self._characters_button.on_click = lambda: self.show_entity("characters")

        self._artifacts_button = InvButton(
            "Artifacts",
            position=(0, 0.6),
            parent=self
        )
        self._artifacts_button.on_click = lambda: self.show_entity("artifacts")

        self._weapons_button = InvButton(
            "Weapons",
            position=(0.35, 0.6),
            parent=self
        )
        self._weapons_button.on_click = lambda: self.show_entity("weapons")

    def show_entity(self, entity_type):
        for entity in self.current_page_listings:
            destroy(entity)

        tracker = 0
        y = 0.4
        if entity_type == "characters":
            catagory = self.player.characters
        elif entity_type == "artifacts":
            catagory = self.player.artifacts
        elif entity_type == "weapons":
            catagory = self.player.weapons

        for entity in catagory:
            self.current_page_listings.append(EntityIcon(
                entity,
                position=(-0.3 + (tracker * 0.3), y),
                parent=self
            ))
            tracker += 1
            if tracker % 3 == 0:
                y -= 0.2
                tracker = 0
