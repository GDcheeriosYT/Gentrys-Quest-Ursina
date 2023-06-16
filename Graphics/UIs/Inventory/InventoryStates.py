from enum import Enum


class InventoryStates(Enum):
    listing = 0
    entity_overview = 1
    selection = 2
    multiSelection = 3
