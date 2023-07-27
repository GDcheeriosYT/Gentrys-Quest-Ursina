from ursina import *

import Game
from .LocationButton import LocationButton
from .AreaInfoContainer import AreaInfoContainer
from .AreaButton import AreaButton
from utils.Event import Event


class TravelMenu(Entity):
    def __init__(self, parent):
        super().__init__(
            color=color.clear,
            parent=parent
        )

        self.locations = []
        self.areas = []
        self.selected_location = None
        self.location_info_updated = False

        self.list_locations()

        self.area_info_container = AreaInfoContainer(self)

        self.back_button = Button(
            "locations",
            position=(-0.5, -0.45),
            scale=(0.1, 0.1),
            parent=self
        )

        back_button_event = Event('BackEvent', 0)

        back_button_event += self.clear_areas
        back_button_event += lambda: invoke(self.list_locations, delay=0.32)

        self.back_button.on_click = back_button_event
        self.back_button.disable()

    def list_locations(self):
        position_y = 0.4

        def assign_click_event(button, location):
            button.on_click_event += lambda: self.set_location(location.name)

        for location in Game.content_manager.locations:
            location = location()
            location_button = LocationButton(location.name, self)
            assign_click_event(location_button, location)
            location_button.y = position_y
            self.locations.append(location_button)
            position_y -= 0.22

    def clear_locations(self):
        for location in self.locations:
            destroy(location)

    def clear_areas(self):
        self.selected_location = None
        self.location_info_updated = True
        Game.selected_area = None
        for area in self.areas:
            destroy(area)

    def list_areas(self, area_list: list):
        self.back_button.enable()
        position_y = 0.4

        def assign_click_event(button, area):
            button.on_click_event += lambda: self.set_area(area)

        for area in area_list:
            area_button = AreaButton(area.name, self)
            assign_click_event(area_button, area)
            area_button.y = position_y
            self.areas.append(area_button)
            position_y -= 0.22

        self.manage_area_color()

    def set_location(self, name: str):
        self.clear_locations()
        self.selected_location = Game.content_manager.get_location(name)
        Game.selected_area = self.selected_location.areas[0]
        self.area_info_container.update_area_info(Game.selected_area)
        self.list_areas(self.selected_location.areas)
        self.location_info_updated = True

    def set_area(self, area):
        Game.selected_area = area
        self.area_info_container.update_area_info(Game.selected_area)
        self.manage_area_color()

    def manage_area_color(self):
        for area_button in self.areas:
            if area_button.text == Game.selected_area.name:
                area_button.color = color.gray
            else:
                area_button.color = color.black

    def input(self, key):
        if key == "left mouse":
            self.manage_area_color()

    def update(self):
        if self.location_info_updated:
            if self.selected_location is None:
                self.area_info_container.animate_position((1, 0), 0.3)
            else:
                self.area_info_container.animate_position((0.2, 0), 0.3)

            self.location_info_updated = False
