from Graphics.Container import Container
from ursina import *


class EffectsContainer(Container):
    def __init__(self):
        super().__init__(
            position=(0.2, 1),
            scale=(1, 1.5)
        )

        self._effects = []

    def update_data(self, effects):
        for effect in self._effects:
            destroy(effect)

        self._effects.clear()

        x = 0
        for effect in effects:
            effect_picture = Entity(
                model="quad",
                texture=effect.texture,
                position=(x, 0),
                scale=(0.15, 0.15),
                parent=self
            )
            Text(
                f"{effect.name} {f'{effect.get_stack()}x' if effect.get_stack() > 1 else ''}",
                color=color.black,
                scale=(9, 18),
                position=(0, -0.7),
                origin=(0, -0.5),
                parent=effect_picture
            )

            self._effects.append(effect_picture)

            x += 0.2
