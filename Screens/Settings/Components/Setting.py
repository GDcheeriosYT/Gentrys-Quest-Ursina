from ursina import *

from Graphics.GameText import GameText


class Setting(Entity):
    def __init__(self, name: str, second_entity: Entity, *args, **kwargs):
        super().__init__(origin=(-1, 0), *args, **kwargs)
        self.setting_text = GameText(
            name,
            position=(-0.1, 0),
            origin=(0, 0),
            parent=self
        )
        self.second_entity = second_entity
        self.second_entity.position = (0.1, 0)
        self.second_entity.parent = self

    def get_setting(self):
        return self.second_entity