from ursina import *

import Game
from .ExperienceOverview import ExperienceOverview
from .InvButton import InvButton
from .EntityIcon import EntityIcon
from Graphics.Container import Container
from Graphics.TextStyles.StarRatingText import StarRatingText
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon
from Entity.Artifact.Artifact import Artifact
from .InventoryStates import InventoryStates
from Entity.Enemy.Enemy import Enemy
from utils.Event import Event
from .MoneyUpgradeUI import MoneyUpgradeUI


class Inventory(Entity):
    """
    An inventory class to handle all the methods for the user's inventory.

    :var state: The state of the inventory.
    """

    state = InventoryStates.listing
    state_affected = False

    def __init__(self):
        super().__init__(
            model=Quad(radius=0.06),
            scale=(1.2, 0.75),
            color=rgb(117, 117, 117, 200),
            position=(0, -0.1),
            parent=camera.ui
        )

        self.player = Game.user.user_data  # grab the user and set as variable
        self.selected_entity = None # tracker for character

        self.money = Text(
            "$",
            origin=(0.5, 0.5),
            position=(0.45, 0.48),
            scale=(1.2, 1.2),
            color=color.black,
            parent=self,
        )  # Text Entity for displaying money

        self.page = 0  # page counter

        self.selected_entities = []  # tracker for entity selections

        self.page_text = Text(
            str(self.page),
            position=(0, -0.4),
            parent=self
        )  # Text Entity to display the current page

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

        # Buttons to navigate up and down the pages

        self.current_page_listings = []  # keep track of the listings in the current page

        self.current_focused_entity = None  # keep track of the current entity

        self._characters_button = InvButton(
            "Characters",
            position=(-0.35, 0.65),
            parent=self
        )
        cevent = Event("cEvent", 0)
        cevent += lambda: self.set_state(InventoryStates.listing)
        cevent += lambda: self.show_entity_listing("characters", True)
        self._characters_button.on_click = cevent

        self._artifacts_button = InvButton(
            "Artifacts",
            position=(0, 0.65),
            parent=self
        )
        aevent = Event("aEvent", 0)
        aevent += lambda: self.set_state(InventoryStates.listing)
        aevent += lambda: self.show_entity_listing("artifacts", True)
        self._artifacts_button.on_click = aevent

        self._weapons_button = InvButton(
            "Weapons",
            position=(0.35, 0.65),
            parent=self
        )
        wevent = Event("wEvent", 0)
        self._weapons_button.on_click = lambda: self.show_entity_listing("weapons", True)

        # buttons for managing display of each entity types

        self.show_entity_listing("characters")  # show the default entity type




    def set_state(self, state: InventoryStates):  # noqa
        Inventory.state = state
        Inventory.state_affected = False




    def clear_listing(self):  # noqa
        """
        Clears the listings.
        """

        for entity in self.current_page_listings:
            destroy(entity)





    def show_entity_listing(self, entity_type, clear_page: bool = False):  # noqa
        """
        Lists entities in the inventory.
        :param entity_type: The type of entity needed to be listed.
        :param clear_page: Whether the page should be cleared or not.
        """

        def swap_weapon(entity: Character, weapon: Weapon):
            old_weapon = entity.swap_weapon(weapon)
            self.player.weapons.remove(weapon)
            if old_weapon:
                self.player.add_weapon(old_weapon)


        self.clear_listing()
        if clear_page:
            self.page = 0
            self.page_text.text = str(self.page)

        if self.current_focused_entity:
            destroy(self.current_focused_entity)

        tracker = 0  # column tracker
        y = 0.4
        category = None
        if entity_type == "characters":
            self._characters_button.color = color.gray
            self._weapons_button.color = color.black
            self._artifacts_button.color = color.black
            category = self.player.characters
        elif entity_type == "artifacts":
            self._characters_button.color = color.black
            self._weapons_button.color = color.black
            self._artifacts_button.color = color.gray
            category = self.player.artifacts
        elif entity_type == "weapons":
            self._characters_button.color = color.black
            self._weapons_button.color = color.gray
            self._artifacts_button.color = color.black
            category = self.player.weapons

        # determine the entity category to display

        for entity in self.get_entities(category, self.page):
            entity_icon = EntityIcon(
                entity,
                position=(-0.3 + (tracker * 0.3), y),
                color=color.clear,
                parent=self
            )
            if Inventory.state == InventoryStates.listing:
                entity_icon.on_click = lambda entity=entity: self.show_entity(entity)

            elif Inventory.state == InventoryStates.selection:
                if entity_type == "weapons":
                    click_event = Event("clickEvent", 0)
                    click_event += lambda entity=entity: swap_weapon(self.selected_entity, entity)
                    click_event += lambda: self.show_entity(self.selected_entity)
                    entity_icon.on_click = click_event

            self.current_page_listings.append(entity_icon)
            tracker += 1
            if tracker % 3 == 0:
                y -= 0.2
                tracker = 0

        # display entities in a grid fashion

        if self.page > 0:
            self.page_down_button.enable()
            self.page_down_button.on_click = lambda: self.page_down(entity_type)
        else:
            self.page_down_button.disable()

        print((self.page + 1) * 12, len(category), self.page * 12 < len(category))
        if (self.page + 1) * 12 < len(category):
            self.page_up_button.enable()
            self.page_up_button.on_click = lambda: self.page_up(entity_type)
        else:
            self.page_up_button.disable()

        # determine if the user can navigate up or down





    def page_up(self, type):  # noqa
        """
        Goes up a page.
        :param type: The type of entity listing.
        """

        self.page += 1
        self.page_text.text = str(self.page)
        self.show_entity_listing(type)

    def page_down(self, type):
        """
        Goes down a page.
        :param type: The type of entity listing.
        """

        self.page -= 1
        self.page_text.text = str(self.page)
        self.show_entity_listing(type)





    def get_entities(self, list: list, page):  # noqa
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





    def change_entity_focus(self, entity):  # noqa
        self.selected_entity = entity




    def show_entity(self, entity):  # noqa
        """
        Displays the given entity on the inventory overlay.
        :param entity: Entity to show
        """

        self.selected_entity = entity
        if self.current_focused_entity:
            destroy(self.current_focused_entity)

        self.set_state(InventoryStates.entity_overview)
        self.page = 0
        self.clear_listing()
        self.current_focused_entity = Container(parent=self)
        entity_picture = Entity(
            model=Quad(0.1),
            texture=entity.texture,
            position=(0.3, 0.3),
            scale=(0.3, 0.3),
            parent=self.current_focused_entity
        )

        entity_rating = StarRatingText(
            entity.star_rating,
            origin=(0.5, 0),
            position=(0.5, -0.6),
            scale=(6, 6),
            parent=entity_picture
        )

        entity_name = Text(
            entity.name,
            origin=(0.5, 0),
            position=(0.5, -0.7),
            scale=(6, 6),
            parent=entity_picture
        )

        entity_experience = ExperienceOverview(entity, parent=entity_picture)

        if isinstance(entity, Character):
            entity_description = Text(
                entity.description,
                origin=(0.5, 0.5),
                position=(0.5, -0.9),
                scale=(4, 4),
                parent=entity_picture
            )
            entity_description.wordwrap = 30

            entity_stats = Text(
                entity.stats,
                position=(-0.6, 0),
                origin=(0.5, 0),
                scale=(4, 4),
                parent=entity_picture
            )

            entity_equip_button = Button(
                "Equip",
                position=(0, -0.4),
                scale=(0.2, 0.1),
                parent=entity_picture
            )
            equip_on_click = Event('onClick', 0)
            equip_on_click += lambda: Game.user.equip_character(entity)
            equip_on_click += lambda: update_data(entity)
            equip_on_click += entity_equip_button.disable
            entity_equip_button.disable()
            entity_equip_button.on_click = equip_on_click

            if Game.user.get_equipped_character() != entity:
                entity_equip_button.enable()

            def update_data():
                entity_stats.text = entity.stats
                entity_experience.text = f"level {entity.experience.level}{f'/{entity.experience.limit}' if entity.experience.limit else ''} {int(entity.experience.xp)}/{entity.experience.get_xp_required(entity.star_rating)}xp"

            money_upgrade_ui = MoneyUpgradeUI(
                entity,
                update_data,
                position=(0, -2),
                parent=entity_picture
            )

            entity_weapon = EntityIcon(
                entity.weapon,
                origin=(0, 0),
                position=(-0.4, 0.3),
                parent=self.current_focused_entity
            )
            if entity.weapon:
                entity_weapon.on_click = lambda: self.show_entity(entity.weapon)
            else:
                _weapon_on_click = Event("weaponOnClick", 0)
                _weapon_on_click += lambda: self.set_state(InventoryStates.selection)
                _weapon_on_click += lambda: self.show_entity_listing("weapons")
                entity_weapon.on_click = _weapon_on_click

            weapon_text = Text(
                "Weapon",
                position=(0, 0.7),
                origin=(0, 0),
                scale=(8, 8),
                parent=entity_weapon
            )

        def weapon_manage_click():
            self.choose_item("weapon")

        if isinstance(entity, Weapon):
            def update_data():
                entity_experience.text = f"level {entity.experience.level}{f'/{entity.experience.limit}' if entity.experience.limit else ''} {int(entity.experience.xp)}/{entity.experience.get_xp_required(entity.star_rating)}xp"

            stats_text = f"base attack: {entity.base_attack} damage\n" \
                         f"attack speed: {entity.base_speed} seconds\n" \
                         f"range: {entity.range}\n"

            entity_stats = Text(
                stats_text,
                position=(-0.6, 0),
                origin=(0.5, 0),
                scale=(4, 4),
                parent=entity_picture
            )

            if entity.equipped_entity:
                self.swap_button = Button(
                    "swap",
                    scale=(0.1, 0.05),
                    position=(0, -0.45),
                    parent=self.current_focused_entity
                )
                swap_event = Event("swapEvent", 0)
                swap_event += lambda: self.change_entity_focus(entity.equipped_entity)
                swap_event += lambda: self.set_state(InventoryStates.selection)
                swap_event += lambda: self.show_entity_listing("weapons")
                self.swap_button.on_click = swap_event

            money_upgrade_ui = MoneyUpgradeUI(
                entity,
                update_data,
                position=(0, -2),
                parent=entity_picture
            )

        if isinstance(entity, Artifact):
            attribute_texts = ""
            for attribute in entity.attributes:
                attribute_texts += f"{attribute}\n"
            stats_text = f"main attribute: {entity.main_attribute}\n" \
                         f"{attribute_texts}"

            entity_stats = Text(
                stats_text,
                position=(-0.6, 0),
                origin=(0.5, 0),
                scale=(4, 4),
                parent=entity_picture
            )




    def choose_item(self, category: str):  # noqa
        """
        Choose an item from inventory to be returned.

        :param category: The category of item to choose.
        :return: Chosen Entity
        """

        Inventory.state = InventoryStates.selection
        self.show_entity_listing(category)






    def update(self):  # noqa
        """
        Every frame update the money display and display based on inventory state.
        """
        self.money.text = f"${format(int(Game.user.user_data.money), ',')}"
        if not Inventory.state_affected:
            if Inventory.state == InventoryStates.listing:
                pass

            if Inventory.state == InventoryStates.entity_overview:
                if self.current_focused_entity:
                    self.current_focused_entity.enable()

            if Inventory.state == InventoryStates.selection:
                self.current_focused_entity.disable()

        Inventory.state_affected = True
