from ursina import *


class DamageText(Text):
    def __init__(self):
        super().__init__(
            "",
            position=(0, 0.5, -1),
            scale=(20, 20),
            origin=(0, 0),
        )

    def display(self, damage, color: Vec4, parent: entity):
        try:
            self.text = str(damage)
            self.position = (0, 0)
            self.color = color
            self.parent = parent
            self.animate_position((self.x + 0.1, self.y + 0.5), 1)
            self.fade_out(0, 1)
            invoke(self.disable, delay=1)
        except AssertionError:
            self.disable()
