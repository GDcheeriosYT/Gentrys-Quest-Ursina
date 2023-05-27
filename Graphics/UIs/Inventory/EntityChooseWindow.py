from ursina import *

import Game
from .EntityIcon import EntityIcon


class EntityChooseWindow(Entity):
    def __init__(self, is_artifact: bool = False, single_selection: bool = True, *args, **kwargs):
        super().__init__(
            model=Quad(0.1),
            color=color.gray,
            *args,
            **kwargs
        )
        self.is_artifact = is_artifact
        self.single_selection = single_selection

        self.selections = []
        self.selection = None

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

        self.show_entity_listing(True)

    def clear_listing(self):
        for entity in self.current_page_listings:
            destroy(entity)

    def show_entity_listing(self, clear_page: bool = False):
        self.clear_listing()
        if clear_page:
            self.page = 0
            self.page_text.text = str(self.page)

        tracker = 0
        y = 0.4
        catagory = Game.user.get_artifacts() if self.is_artifact else Game.user.get_weapons()

        for entity in self.get_entities(catagory, self.page):
            entity_icon = EntityIcon(
                entity,
                position=(-0.3 + (tracker * 0.3), y),
                parent=self
            )
            entity_icon.color = color.green if entity in self.selections else color.clear
            entity_icon.on_click = lambda entity=entity: self.select(entity)
            self.current_page_listings.append(entity_icon)
            tracker += 1
            if tracker % 3 == 0:
                y -= 0.2
                tracker = 0

        if self.page > 0:
            self.page_down_button.enable()
            self.page_down_button.on_click = self.page_down
        else:
            self.page_down_button.disable()

        print((self.page + 1) * 12, len(catagory), self.page * 12 < len(catagory))
        if (self.page + 1) * 12 < len(catagory):
            self.page_up_button.enable()
            self.page_up_button.on_click = self.page_up
        else:
            self.page_up_button.disable()

    def select(self, entity):
        if self.single_selection:
            self.selections.append(
                Game.user.get_artifacts().index(entity) if self.is_artifact else Game.user.get_weapons().index(entity)
            )
        else:
            self.selection = Game.user.get_artifacts().index(entity) if self.is_artifact else Game.user.get_weapons().index(entity)

    def page_up(self):
        self.page += 1
        self.page_text.text = str(self.page)

    def page_down(self):
        self.page -= 1
        self.page_text.text = str(self.page)

    def get_entities(self, list: list, page):
        entity_list = []
        index_start = (page * 12)
        index_end = ((page + 1) * 12)
        current_index = index_start
        while current_index < index_end:
            try:
                entity_list.append(list[current_index])
            except IndexError:
                break
            current_index += 1

        return entity_list

    def submit(self):
        return self.selection
