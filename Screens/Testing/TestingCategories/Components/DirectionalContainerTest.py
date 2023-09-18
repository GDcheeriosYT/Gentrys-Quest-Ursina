from ursina import *

from ...Test import Test

from Graphics.Containers.DirectionalContainer import DirectionalContainer


class DirectionalContainerTest(Test):
    def __init__(self):
        super().__init__(DirectionalContainer)
        self.directional_container_horizontal = None
        self.directional_container_horizontal: DirectionalContainer

        self.directional_container_vertical = None
        self.directional_container_vertical: DirectionalContainer

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        amount = 3
        spacing = 3

        def create_horizontal_container():
            if not self.directional_container_horizontal:
                self.directional_container_horizontal = DirectionalContainer(
                    horizontal=True,
                    items=[
                        Entity(model="quad", color=color.black) for i in range(amount)
                    ],
                    spacing=spacing,
                    color=color.white,
                    parent=Test.screen,
                    scale=(0.45, 0.45),
                    position=(-0.25, 0)
                )

        def create_vertical_container():
            if not self.directional_container_vertical:
                self.directional_container_vertical = DirectionalContainer(
                    horizontal=False,
                    items=[
                        Entity(model="quad", color=color.black) for i in range(amount)
                    ],
                    spacing=spacing,
                    color=color.white,
                    parent=Test.screen,
                    scale=(0.45, 0.45),
                    position=(0.25, 0)
                )

        # tests
        # test spawn button
        self.make_button("Create Horizontal Container", create_horizontal_container)
        self.make_button("Create Vertical Container", create_vertical_container)
        self.get_button(index=0).on_click()
        self.get_button(index=1).on_click()

    def _unload(self):
        destroy(self.directional_container_horizontal)
        destroy(self.directional_container_vertical)
