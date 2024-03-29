from Entity.Effect import Effect
from Graphics.TextStyles.DamageText import DamageText
from ursina import *


class Burn(Effect):
    def __init__(self, ticks: int = 0):
        super().__init__(ticks=ticks, delay=0.3)
        self.on_effect += self.handle_damage

    @property
    def name(self) -> str:
        return "Burn"

    def handle_damage(self):
        percent = 1
        damage = int(self._effector.stats.health.get_percent_of_stat(percent) * self._stack)
        self._effector.damage(damage, color=color.orange)

    @property
    def texture(self) -> str:
        return "fire.png"

    @property
    def description(self) -> str:
        return "burns the entity for 1% per 0.3 seconds or something ＼（〇_ｏ）／"
