from ursina import *


class DamageText(Text):
    def __init__(self, damage_amount: int, is_crit: bool = None, text_color: color = rgb(255, 255, 255), *args, **kwargs):
        super().__init__(
            f"{damage_amount if damage_amount > 0 else 'miss'}",
            color=color.red if is_crit else text_color,
            position=(0, 0.5, -1),
            scale=(20, 20),
            origin=(0, 0),
            *args,
            **kwargs
        )

        self.animate_position((self.x + 0.1, self.y + 0.5), 1)
        self.fade_out(0, 1)
        destroy(self, 1.5)
