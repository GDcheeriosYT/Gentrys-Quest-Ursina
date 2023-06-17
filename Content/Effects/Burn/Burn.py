from Entity.Effect import Effect
from Graphics.TextStyles.DamageText import DamageText
from ursina import *


class Burn(Effect):
    def __init__(self, ticks: int):
        super().__init__(ticks=ticks, delay=0.3)
        percent = 1.7
        self.on_effect += lambda: self._effector.damage(int(self._effector.stats.health.get_percent_of_stat(percent)), DamageText(int(self._effector.stats.health.get_percent_of_stat(percent)), text_color=rgb(249, 132, 69), parent=self._effector))

    @property
    def name(self) -> str:
        return "Burn"

    @property
    def texture(self) -> str:
        return "fire.png"

    @property
    def description(self) -> str:
        return "burns the entity or something ＼（〇_ｏ）／"
