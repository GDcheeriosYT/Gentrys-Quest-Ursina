from ursina import *

from ..Container import Container


class ScrollableContainer(Container):
    def __init__(self, is_down: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_down = is_down
        self.distance = 0
        self.container_children = []
        self.moving_container = Container(parent=self)
        self.moving_container.add_script(Scrollable(axis="y" if self.is_down else "x", max=0.2, min=-0.2, target_value=-0.25))

    def add_to_container(self, entity: Entity):
        """
        Adds the entity to the container.

        :param entity: The entity to be added to the container.

        """

        entity.parent = self.moving_container
        entity.position = (
            self.distance * entity.world_scale[0] if not self.is_down else 0,  # x
            self.distance * entity.world_scale[1] if self.down else 0          # y
        )
        self.container_children.append(entity)
        self.calculate_distance()

    def calculate_distance(self):
        """
        Calculates the distance of the container.
        """

        self.distance = 0
        for child in self.container_children:
            self.distance += child.scale[0] if not self.down else child.scale[1]
