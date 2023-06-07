from ursina import *
from .Register import Register


class GasStation(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            texture='Textures/tiles.png',
            scale=(15, 8),
            position=(0, 0, 1),
            parent=self
        )

        shelves = [
            'Textures/shelf.png',
            'Textures/shelf1.png'
        ]

        shelf_size = (0.2, 0.15)

        shelf_entities = []

        x = -0.23
        y = 0.25

        for i in range(6):
            if i != 3 and i != 4:
                shelf_entities.append(
                    Entity(
                        model='quad',
                        texture=random.choice(shelves),
                        scale=shelf_size,
                        position=(x, y, -1),
                        collider='box',
                        parent=self
                    )
                )
            x += 0.3
            if i == 2:
                y = -0.3
                x = -0.23

        wall = Entity(
            model='quad',
            color=color.gray,
            collider='box',
            parent=self
        )
        wall.disable()

        register = Register(self)

        tender = Entity(
            model='quad',
            texture='Textures/philip.png',
            position=(-0.4, -0.2, -1),
            scale=(0.15, 0.15),
            collider='box',
            parent=self
        )

        duplicate(wall, position=(0, 0.5, -1), scale=(1, 0.1))
        duplicate(wall, position=(0.3, -0.5, -1), scale=(0.35, 0.1))
        duplicate(wall, position=(-0.3, -0.5, -1), scale=(0.35, 0.1))
        duplicate(wall, position=(-0.5, 0, -1), scale=(0.05, 1.1))
        duplicate(wall, position=(0.5, 0, -1), scale=(0.05, 1.1))
