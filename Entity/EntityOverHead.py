from ursina import *
from ursina.prefabs.health_bar import HealthBar


class EntityOverhead(Entity):
    def __init__(self, entity: Entity):
        self._entity = entity
        super().__init__(
            model="quad",
            parent=entity,
            origin=(0, 0),
            scale=(2, 2),
            position=(0, 0.6),
            color=rgb(0, 0, 0, 0)
        )

        try:
            name = entity.name
        except AttributeError:
            name = None

        self.entity_name = Text(f"{name}", parent=self, color=rgb(0, 0, 0, 255), scale=(5, 5), origin=(0, 0), position=(0, 0.2))
        self.health_bar = HealthBar(max_value=entity.stats.health.get_value(), parent=self, position=(-0.25, 0.1), show_text=False)
        self.health_bar.collider = None

    def update_data(self):
        self.health_bar.max_value = self._entity.stats.health.get_value()
        self.health_bar.value = self._entity.stats.health.current_value
        self.entity_name.text = f"{self._entity.name}\nlevel {self._entity.experience.level}"

    def change_name(self, name):
        self.entity_name.text = name
