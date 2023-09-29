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

        self.scale_text = None
        self.ratio_text = None

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        def create_horizontal_container():
            if self.directional_container_horizontal:
                destroy(self.directional_container_horizontal)

            self.directional_container_horizontal = DirectionalContainer(
                horizontal=True,
                items=[
                    Entity(model="quad", color=color.black) for i in range(int(self.get_variable("Amount")))
                ],
                spacing=self.get_variable("Spacing"),
                color=color.white,
                parent=Test.screen,
                scale=(self.get_variable("X Scale"), self.get_variable("Y Scale")),
                position=(-0.25, 0)
            )
            self.update_text(self.directional_container_horizontal)

        def create_vertical_container():
            if self.directional_container_vertical:
                destroy(self.directional_container_vertical)

            self.directional_container_vertical = DirectionalContainer(
                horizontal=False,
                items=[
                    Entity(model="quad", color=color.black) for i in range(int(self.get_variable("Amount")))
                ],
                spacing=self.get_variable("Spacing"),
                color=color.white,
                parent=Test.screen,
                scale=(self.get_variable("X Scale"), self.get_variable("Y Scale")),
                position=(0.25, 0)
            )
            self.update_text(self.directional_container_vertical)

        # tests
        # test spawn button
        self.make_button("Create Horizontal Container", create_horizontal_container)
        self.make_button("Create Vertical Container", create_vertical_container)
        self.make_slider("X Scale", 0.01, 0.45, 0.45)
        self.make_slider("Y Scale", 0.01, 0.45, 0.45)
        self.make_slider("Spacing", 1, 5, 3)
        self.make_slider("Amount", 1, 100, 3, 1)
        self.get_button(index=0).on_click()
        self.get_button(index=1).on_click()

    def update_text(self, container):
        if self.scale_text:
            destroy(self.scale_text)

        if self.ratio_text:
            destroy(self.ratio_text)

        self.scale_text = Text(f"scale: {round(container.formula / container.spacing, 2)}", origin=(0.5, 0.5), position=(0.5, 0.5), parent=Test.screen)
        self.ratio_text = Text(f"ratio: {round(container.ratio, 2)}({round(container.width, 2)}:{round(container.height, 2)})", origin=(0.5, 0.5), position=(0.5, 0.46), parent=Test.screen)

    def _unload(self):
        destroy(self.directional_container_horizontal)
        destroy(self.directional_container_vertical)
        destroy(self.scale_text)
        destroy(self.ratio_text)
