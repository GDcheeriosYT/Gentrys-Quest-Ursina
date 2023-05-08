from ursina import *


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
            if i != 4:
                shelf_entities.append(
                    Entity(
                        model='quad',
                        texture=random.choice(shelves),
                        scale=shelf_size,
                        position=(x, y, -1),
                        parent=self
                    )
                )
            x += 0.3
            if i == 2:
                y = -0.3
                x = -0.23
