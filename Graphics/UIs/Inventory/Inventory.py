from ursina import *

import Game
from .InvButton import InvButton
from .EntityIcon import EntityIcon
from .CharacterOverview import CharacterOverview
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon
from Entity.Enemy.Enemy import Enemy
from utils.Event import Event


class Inventory(Entity):
    def __init__(self):
        super().__init__(
            model=Quad(radius=0.06),
            scale=(1.2, 0.75),
            color=rgb(117, 117, 117, 200),
            position=(0, -0.1),
            parent=camera.ui
        )
        self.player = Game.user.user_data

        self.money = Text(
            "$",
            origin=(0.5, 0.5),
            position=(0.45, 0.48),
            scale=(1.2, 1.2),
            color=color.black,
            parent=self,
        )

        self.page = 0

        self.page_text = Text(
            str(self.page),
            position=(0, -0.4),
            parent=self
        )

        self.page_down_button = Button(
            "back",
            scale=(0.06, 0.06),
            position=(-0.2, -0.4),
            parent=self
        )
        self.page_down_button.disable()
        self.page_up_button = Button(
            "next",
            scale=(0.06, 0.06),
            position=(0.2, -0.4),
            parent=self
        )
        self.page_up_button.disable()

        self.current_page_listings = []

        self.current_focused_entity = None

        self._characters_button = InvButton(
            "Characters",
            position=(-0.35, 0.65),
            parent=self
        )
        self._characters_button.on_click = lambda: self.show_entity_listing("characters", True)

        self._artifacts_button = InvButton(
            "Artifacts",
            position=(0, 0.65),
            parent=self
        )
        self._artifacts_button.on_click = lambda: self.show_entity_listing("artifacts", True)

        self._weapons_button = InvButton(
            "Weapons",
            position=(0.35, 0.65),
            parent=self
        )
        self._weapons_button.on_click = lambda: self.show_entity_listing("weapons", True)

        self.show_entity_listing("characters")

    def clear_listing(self):
        for entity in self.current_page_listings:
            destroy(entity)

    def show_entity_listing(self, entity_type, clear_page: bool = False):
        self.clear_listing()
        if clear_page:
            self.page = 0
            self.page_text.text = str(self.page)

        if self.current_focused_entity:
            destroy(self.current_focused_entity)

        tracker = 0
        y = 0.4
        catagory = None
        if entity_type == "characters":
            self._characters_button.color = color.gray
            self._weapons_button.color = color.black
            self._artifacts_button.color = color.black
            catagory = self.player.characters
        elif entity_type == "artifacts":
            self._characters_button.color = color.black
            self._weapons_button.color = color.black
            self._artifacts_button.color = color.gray
            catagory = self.player.artifacts
        elif entity_type == "weapons":
            self._characters_button.color = color.black
            self._weapons_button.color = color.gray
            self._artifacts_button.color = color.black
            catagory = self.player.weapons

        for entity in self.get_entities(catagory, self.page):
            entity_icon = EntityIcon(
                entity,
                position=(-0.3 + (tracker * 0.3), y),
                parent=self
            )
            entity_icon.on_click = lambda entity=entity: self.show_entity(entity)
            self.current_page_listings.append(entity_icon)
            tracker += 1
            if tracker % 3 == 0:
                y -= 0.2
                tracker = 0

        if self.page > 0:
            self.page_down_button.enable()
            self.page_down_button.on_click = lambda: self.page_down(entity_type)
        else:
            self.page_down_button.disable()

        print((self.page + 1) * 12, len(catagory), self.page * 12 < len(catagory))
        if (self.page + 1) * 12 < len(catagory):
            self.page_up_button.enable()
            self.page_up_button.on_click = lambda: self.page_up(entity_type)
        else:
            self.page_up_button.disable()

    def page_up(self, type):
        self.page += 1
        self.page_text.text = str(self.page)
        self.show_entity_listing(type)

    def page_down(self, type):
        self.page -= 1
        self.page_text.text = str(self.page)
        self.show_entity_listing(type)

    def get_entities(self, list: list, page):
        entity_list = []
        index_start = (page * 12)
        index_end = ((page + 1) * 12)
        current_index = index_start
        print(self.page)
        print(index_start)
        print(index_end)
        print(current_index)
        while current_index < index_end:
            try:
                entity_list.append(list[current_index])
            except IndexError:
                break
            current_index += 1

        return entity_list

    def show_entity(self, entity):
        self.page = 0
        self.clear_listing()
        if isinstance(entity, Character):
            self.current_focused_entity = CharacterOverview(entity, parent=self)

    def update(self):
        self.money.text = f"${format(int(Game.user.user_data.money), ',')}"
