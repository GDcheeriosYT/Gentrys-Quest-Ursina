from ursina import *


class ParkingLot(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            color=rgb(36, 36, 36),
            position=(0, -6, 1),
            texture_scale=(6, 6),
            origin=(0, 0.5),
            scale=(20, 12),
            parent=self
        )

        self.sidewalk = Entity(
            model='quad',
            scale=(2, 0.2, 0),
            color=rgb(117, 117, 117),
            texture_scale=(16, 1),
            origin=(0, -0.5),
            position=(0, 0),
            parent=self
        )

        side_walk_cracks = Entity(
            model='quad',
            position=(0, 0.5, -2),
            color=rgb(6, 6, 6, 100),
            scale=(0.001, 1),
            parent=self.sidewalk
        )
        side_walk_cracks.disable()

        for i in range(16):
            duplicate(side_walk_cracks, position=((8 - i) * 0.06, 0.5, -2), scale=(0.0015, 1)).combine(self.sidewalk)

        sidewalk_siding = Entity(
            model='quad',
            scale=(1, 0.1, 9),
            color=color.white,
            origin=(0, 0),
            position=(0, 0, -1),
            collider='box',
            parent=self.sidewalk
        )

        Entity(
            model='quad',
            collider='box',
            color=color.clear,
            position=(-0.3, -0.5, -1),
            scale=(0.1, 2),
            parent=self,
        )

        street_lines = Entity(
            model='quad',
            scale=(0.007, 0.25),
            color=color.white,
            origin=(0, 0.5),
            position=(0, 0, -1),
            parent=self
        )
        street_lines.disable()

        amount = 7
        for i in range(amount):
            duplicate(street_lines, position=(-0.5 + i * (1 / amount), 0, -1)).combine(self)
