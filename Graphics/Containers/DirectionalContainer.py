from ursina import *

from ..Container import Container


class DirectionalContainer(Container):
    def __init__(self, horizontal: bool, items: list, spacing: int = 3, child_origin: tuple = (0, 0), *args, **kwargs):
        """
        Create A DirectionalContainer.

        :param horizontal: Whether not the container is horizontal.
        :param items: The list of items in the container.
        :param spacing: The percentage of spacing between each item.
        :param child_origin: The origin of the children
        """

        super().__init__(
            *args,
            **kwargs
        )

        self.horizontal = horizontal
        self.items = items
        self.spacing = spacing
        self.child_origin = child_origin
        self.formula = 0
        self.child_scale = 1
        self.ratio = 1

        self.define_scale()
        self.position_tracker = -0.5 + self.formula / 2 if self.horizontal else 0.5 - self.formula / 2

        for item in self.items:
            item.parent = self
            item.scale = self.child_scale[0], self.child_scale[0] * self.ratio

            item.position = (
                self.position_tracker if self.horizontal else 0,     # x
                self.position_tracker if not self.horizontal else 0  # y
            )
            self.origin = self.child_origin
            self.position_tracker += self.formula if self.horizontal else -self.formula

    def define_scale(self):
        self.formula = (1 / len(self.items))
        self.ratio = self.scale[0] / self.scale[1]
        self.width = self.scale[1] * self.ratio
        self.height = self.scale[0] / self.ratio
        self.child_scale = (
            self.formula / self.spacing,  # x
            self.formula / self.spacing   # y
        )
