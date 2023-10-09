from ursina import *

import Game
from .ExperienceOverview import ExperienceOverview
from .InvButton import InvButton
from .EntityIcon import EntityIcon
from Graphics.Container import Container
from Graphics.TextStyles.StarRatingText import StarRatingText
from Graphics.GameButton import GameButton
from Graphics.GameText import GameText
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon
from Entity.Artifact.Artifact import Artifact
from .InventoryStates import InventoryStates
from utils.Event import Event
from .MoneyUpgradeUI import MoneyUpgradeUI
from typing import Union
from User.User import User


class Inventory(Entity):
    """
    An inventory class to handle all the methods for the user's inventory.

    :var state: The state of the inventory.
    """

    state = InventoryStates.listing
    state_affected = False

    def __init__(self, character_swapping: bool = False, parent: Entity = None):
        super().__init__(
            model=Quad(radius=0.06),
            scale=(1, 0.75),
            color=rgb(117, 117, 117, 255),
            position=(0, -0.1),
            parent=camera.ui if parent is None else parent
        )

        self.player = User("No user", True).user_data  # grab the user and set as variable
        self.selected_entity = None  # tracker for character
        self.selected_index = None  # tracker for artifact index
        self.character_swapping = character_swapping

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

        self.page_down_button = GameButton(
            "back",
            scale=(0.06, 0.06),
            position=(-0.2, -0.4),
            parent=self
        )
        self.page_down_button.disable()
        self.page_up_button = GameButton(
            "next",
            scale=(0.06, 0.06),
            position=(0.2, -0.4),
            parent=self
        )
        self.page_up_button.disable()

        # Buttons to navigate up and down the pages

        self.done_button = GameButton(
            "done",
            scale=(0.15, 0.1),
            position=(0.4, -0.4, -1),
            parent=self
        )
        self.done_button.disable()

        self.current_page_listings = []  # keep track of the listings in the current page

        self.current_focused_entity = None  # keep track of the current entity

        self._characters_button = InvButton(
            Game.language.characters if self.character_swapping else Game.language.character,
            position=(-0.35, 0.65),
            parent=self
        )
        character_event = Event("cEvent", 0)
        if self.character_swapping:
            character_event += lambda: self.set_state(InventoryStates.listing)
            character_event += lambda: self.show_entity_listing("characters", True)
        else:
            character_event += lambda:  self.show_entity(Game.user.get_equipped_character())

        self._characters_button.on_click = character_event

        self._artifacts_button = InvButton(
            Game.language.artifacts,
            position=(0, 0.65),
            parent=self
        )
        artifact_event = Event("aEvent", 0)
        artifact_event += lambda: self.set_state(InventoryStates.listing)
        artifact_event += lambda: self.show_entity_listing("artifacts", True)
        self._artifacts_button.on_click = artifact_event

        self._weapons_button = InvButton(
            Game.language.weapons,
            position=(0.35, 0.65),
            parent=self
        )
        weapon_event = Event("wEvent", 0)
        weapon_event += lambda: self.set_state(InventoryStates.listing)
        weapon_event += lambda: self.show_entity_listing("weapons", True)
        self._weapons_button.on_click = weapon_event

        # buttons for managing display of each entity types

        if self.character_swapping:
            self.show_entity_listing("characters")  # show the default entity type
        else:
            self.show_entity(Game.user.get_equipped_character())



    def update_player(self):  # noqa
        self.player = Game.user.user_data




    def set_state(self, state: InventoryStates):  # noqa
        Inventory.state = state
        Inventory.state_affected = False




    def clear_listing(self):  # noqa
        """
        Clears the listings.
        """

        for entity in self.current_page_listings:
            destroy(entity)

        self.current_page_listings.clear()





    def show_entity_listing(self, entity_type, clear_page: bool = False):  # noqa
        """
        Lists entities in the inventory.
        :param entity_type: The type of entity needed to be listed.
        :param clear_page: Whether the page tracker should be reset or not.
        """

        if self.current_focused_entity:
            destroy(self.current_focused_entity)

        def swap_weapon(entity: Character, weapon: Weapon):
            old_weapon = entity.swap_weapon(weapon)
            self.player.weapons.remove(weapon)
            if old_weapon:
                self.player.add_weapon(old_weapon)

        def swap_artifact(entity: Character, artifact: Artifact, index: int):
            old_artifact = entity.artifacts[index]
            self.player.artifacts.remove(artifact)
            entity.set_artifact(artifact, index)
            if old_artifact:
                self.player.add_artifact(old_artifact)

        self.clear_listing()
        if clear_page:
            self.page = 0
            self.page_text.text = str(self.page)

        tracker = 0  # column tracker
        y = 0.38
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

        if Inventory.state == InventoryStates.multiSelection:
            self.done_button.enable()

            def upgrade_item():
                def determine_xp(item: Union[Weapon, Artifact]):
                    if isinstance(item, Weapon):
                        self.player.weapons.remove(item)
                        return int((item.experience.level * item.star_rating) * 100)

                    else:
                        self.player.artifacts.remove(item)
                        return int((item.experience.level * item.star_rating) * 100)

                for item in self.selected_entities:
                    self.selected_entity.add_xp(determine_xp(item))

                if isinstance(self.selected_entity, Artifact):
                    if self.selected_entity not in self.player.artifacts and not self.selected_entity.equipped_entity:
                        self.player.add_artifact(self.selected_entity)

                else:
                    if self.selected_entity not in self.player.weapons and not self.selected_entity.equipped_entity:
                        self.player.add_weapon(self.selected_entity)

                self.selected_entities.clear()
                self.show_entity(self.selected_entity)

            self.done_button.on_click = upgrade_item

        for entity in self.get_entities(category, self.page):
            entity_icon = EntityIcon(
                entity,
                position=(-0.3 + (tracker * 0.3), y, -1),
                parent=self
            )

            self.current_page_listings.append(entity_icon)  # add entity icon to listings

            if Inventory.state == InventoryStates.listing:
                entity_icon.on_click = lambda entity=entity: self.show_entity(entity)

            elif Inventory.state == InventoryStates.selection:
                if entity_type == "weapons":
                    click_event = Event("clickEvent", 0)
                    click_event += lambda entity=entity: swap_weapon(self.selected_entity, entity)
                    click_event += lambda: self.show_entity(self.selected_entity)
                    entity_icon.on_click = click_event

                if entity_type == "artifacts":
                    click_event = Event("clickEvent", 0)
                    click_event += lambda entity=entity: swap_artifact(self.selected_entity, entity, self.selected_index)
                    click_event += lambda: self.show_entity(self.selected_entity)
                    entity_icon.on_click = click_event

            elif Inventory.state == InventoryStates.multiSelection:
                def color_icon(entity: Union[Artifact, Weapon], icon: GameButton):
                    if entity in self.selected_entities:
                        icon.color = rgb(0, 255, 0, 150)
                    else:
                        icon.color = color.clear

                def assign_click(entity: Union[Artifact, Weapon], icon: GameButton):
                    def click_handler():
                        if entity not in self.selected_entities:
                            self.selected_entities.append(entity)
                            icon.color = rgb(0, 200, 0, 150)
                        else:
                            icon.color = color.clear
                            self.selected_entities.remove(entity)

                    icon.on_click = click_handler

                color_icon(entity, entity_icon)
                assign_click(entity, entity_icon)

            tracker += 1
            if tracker % 3 == 0:
                y -= 0.2
                tracker = 0

        # display entities in a grid fashion
        # also determine what click style it'll be

        if self.page > 0:
            self.page_down_button.enable()
            self.page_down_button.on_click = lambda: self.page_down(entity_type)
        else:
            self.page_down_button.disable()

        # print((self.page + 1) * 12, len(category), self.page * 12 < len(category))
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

        self.selected_entity = entity  # set the selected entity for reference

        if self.current_focused_entity:
            destroy(self.current_focused_entity)

        self.set_state(InventoryStates.entity_overview)
        self.clear_listing()
        self.current_focused_entity = Container(parent=self)
        entity_picture = Entity(
            model=Quad(0.1),
            texture=entity.texture,
            position=(0.3, 0.3, -1),
            scale=(0.3, 0.3),
            parent=self.current_focused_entity
        )

        entity_rating = StarRatingText(
            entity.star_rating,
            origin=(0.5, 0),
            position=(0.5, -0.6, -1),
            scale=(6, 6),
            parent=entity_picture
        )

        entity_name = Text(
            entity.name,
            origin=(0.5, 0),
            position=(0.5, -0.7, -1),
            scale=(6, 6),
            parent=entity_picture
        )

        entity_experience = ExperienceOverview(entity, parent=entity_picture)

        if isinstance(entity, Character):
            entity_description = GameText(
                entity.description,
                origin=(0.5, 0.5),
                position=(0.5, -0.9, -1),
                scale=(4, 4),
                parent=entity_picture
            )
            entity_description.wordwrap = 30

            entity_stats = GameText(
                entity.stats,
                position=(-0.6, 0, -1),
                origin=(0.5, 0),
                scale=(2.5, 2.5),
                parent=entity_picture
            )

            entity_equip_button = GameButton(
                Game.language.equip,
                position=(0, -0.4, -1),
                scale=(0.2, 0.1),
                parent=self.current_focused_entity
            )
            equip_on_click = Event('onClick', 0)
            equip_on_click += lambda: Game.user.equip_character(entity)
            equip_on_click += entity_equip_button.disable
            if Game.user.get_equipped_character() == entity:
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
                position=(0, -2, -1),
                parent=entity_picture
            )

            entity_weapon = EntityIcon(
                entity.weapon,
                origin=(0, 0),
                position=(-0.4, 0.3, -1),
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
                position=(0, 0.7, -1),
                origin=(0, 0),
                scale=(8, 8),
                parent=entity_weapon
            )

            artifact_icon_scale = (0.12, 0.12)
            artifact_icon_y = 0.15
            artifact_icon_change = -0.14

            def create_on_click(icon: GameButton, artifact_index: int):
                if not entity.artifacts[artifact_index]:
                    def on_click_handler():
                        self.selected_index = artifact_index
                        self.set_state(InventoryStates.selection)
                        self.show_entity_listing("artifacts")

                else:
                    def on_click_handler():
                        self.selected_index = artifact_index
                        self.show_entity(entity.artifacts[artifact_index])

                icon.on_click = on_click_handler

            artifact_1_icon = EntityIcon(
                entity.artifacts[0],
                origin=(0, 0),
                scale=artifact_icon_scale,
                position=(-0.4, artifact_icon_y, -1),
                parent=self.current_focused_entity
            )
            create_on_click(icon=artifact_1_icon, artifact_index=0)
            artifact_icon_y += artifact_icon_change
            artifact_2_icon = EntityIcon(
                entity.artifacts[1],
                origin=(0, 0),
                scale=artifact_icon_scale,
                position=(-0.4, artifact_icon_y, -1),
                parent=self.current_focused_entity
            )
            create_on_click(icon=artifact_2_icon, artifact_index=1)
            artifact_icon_y += artifact_icon_change
            artifact_3_icon = EntityIcon(
                entity.artifacts[2],
                origin=(0, 0),
                scale=artifact_icon_scale,
                position=(-0.4, artifact_icon_y, -1),
                parent=self.current_focused_entity
            )
            create_on_click(icon=artifact_3_icon, artifact_index=2)
            artifact_icon_y += artifact_icon_change
            artifact_4_icon = EntityIcon(
                entity.artifacts[3],
                origin=(0, 0),
                scale=artifact_icon_scale,
                position=(-0.4, artifact_icon_y, -1),
                parent=self.current_focused_entity
            )
            create_on_click(icon=artifact_4_icon, artifact_index=3)
            artifact_icon_y += artifact_icon_change
            artifact_5_icon = EntityIcon(
                entity.artifacts[4],
                origin=(0, 0),
                scale=artifact_icon_scale,
                position=(-0.4, artifact_icon_y, -1),
                parent=self.current_focused_entity
            )
            create_on_click(icon=artifact_5_icon, artifact_index=4)

        if isinstance(entity, Weapon):
            stats_text = f"{Game.language.get_localized_text(Game.language.damage, entity.damage)}\n" \
                         f"{Game.language.get_localized_text(Game.language.buff, entity.buff)}\n" \
                         f"{Game.language.get_localized_text(Game.language.attack_speed, entity.base_speed)} {Game.language.seconds}\n" \
                         f"{Game.language.get_localized_text(Game.language.range, entity.range)}\n"

            def update_data():
                entity_experience.text = f"level {entity.experience.level}{f'/{entity.experience.limit}' if entity.experience.limit else ''} {int(entity.experience.xp)}/{entity.experience.get_xp_required(entity.star_rating)}xp"
                entity_stats.text = f"{Game.language.get_localized_text(Game.language.damage, entity.damage)}\n" \
                                    f"{Game.language.get_localized_text(Game.language.buff, entity.buff)}\n" \
                                    f"{Game.language.get_localized_text(Game.language.attack_speed, entity.speed)} {Game.language.seconds}\n" \
                                    f"{Game.language.get_localized_text(Game.language.range, entity.range)}\n"

            entity_stats = GameText(
                stats_text,
                position=(-0.6, 0, -1),
                origin=(0.5, 0),
                scale=(4, 4),
                parent=entity_picture
            )

            if entity.equipped_entity:
                swap_button = GameButton(
                    "swap",
                    scale=(0.1, 0.05),
                    position=(0, -0.45, -1),
                    parent=self.current_focused_entity
                )
                swap_event = Event("swapEvent", 0)
                swap_event += lambda: self.change_entity_focus(entity.equipped_entity)
                swap_event += lambda: self.set_state(InventoryStates.selection)
                swap_event += lambda: self.show_entity_listing("weapons")
                swap_button.on_click = swap_event

                remove_button = GameButton(
                    "remove",
                    scale=(0.1, 0.05),
                    position=(-0.2, -0.45, -1),
                    parent=self.current_focused_entity
                )
                remove_event = Event("removeEvent", 0)
                referenced_entity = entity.equipped_entity
                remove_event += entity.equipped_entity.remove_weapon
                remove_event += lambda: self.show_entity(referenced_entity)
                remove_event += lambda: self.player.add_weapon(entity)
                remove_button.on_click = remove_event

            money_upgrade_ui = MoneyUpgradeUI(
                entity,
                update_data,
                position=(0, -2),
                parent=entity_picture
            )

            upgrade_with_weapon_button = GameButton(
                Game.language.upgrade_with_weapons,
                position=(-0.25, -0.25),
                scale=(0.35, 0.17),
                parent=self.current_focused_entity
            )

            def upgrade_weapon_button_click():
                if not entity.equipped_entity:
                    self.player.weapons.remove(entity)
                self.set_state(InventoryStates.multiSelection)
                self.show_entity_listing("weapons")

            upgrade_with_weapon_button.on_click = upgrade_weapon_button_click

        if isinstance(entity, Artifact):
            attribute_texts = ""
            for attribute in entity.attributes:
                attribute_texts += f"{attribute}\n"
            stats_text = f"main attribute: {entity.main_attribute}\n" \
                         f"{attribute_texts}"

            if entity.equipped_entity:
                swap_button = GameButton(
                    "swap",
                    scale=(0.1, 0.05),
                    position=(0, -0.45, -1),
                    parent=self.current_focused_entity
                )
                swap_event = Event("swapEvent", 0)
                swap_event += lambda: self.change_entity_focus(entity.equipped_entity)
                swap_event += lambda: self.set_state(InventoryStates.selection)
                swap_event += lambda: self.show_entity_listing("artifacts")
                swap_button.on_click = swap_event

                remove_button = GameButton(
                    "remove",
                    scale=(0.1, 0.05),
                    position=(-0.2, -0.45, -1),
                    parent=self.current_focused_entity
                )
                remove_event = Event("removeEvent", 0)
                referenced_entity = entity.equipped_entity
                remove_event += lambda: entity.equipped_entity.remove_artifact(self.selected_index)
                remove_event += lambda: self.show_entity(referenced_entity)
                remove_event += lambda: self.player.add_artifact(entity)
                remove_button.on_click = remove_event

            entity_stats = Text(
                stats_text,
                position=(-0.6, 0, -1),
                origin=(0.5, 0),
                scale=(4, 4),
                parent=entity_picture
            )

            upgrade_button = GameButton(
                "upgrade",
                scale=(1, 0.5),
                position=(0, -2, -1),
                parent=entity_picture
            )

            def upgrade_artifact_button_click():
                if not entity.equipped_entity:
                    self.player.artifacts.remove(entity)
                self.set_state(InventoryStates.multiSelection)
                self.show_entity_listing("artifacts")

            upgrade_button.on_click = upgrade_artifact_button_click






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
                self.page_text.enable()

            if Inventory.state == InventoryStates.entity_overview:
                self.page_up_button.disable()
                self.page_down_button.disable()
                self.page = 0
                self.page_text.disable()
                self.done_button.disable()

            if Inventory.state == InventoryStates.selection:
                self.page_text.enable()
                self.done_button.disable()

            if Inventory.state == InventoryStates.multiSelection:
                self.page_text.enable()

        Inventory.state_affected = True
