from Entity.Character.Skill.Skill import Skill
from ursina import *


class Pete(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate

    @property
    def name(self) -> str:
        return "Pete"

    @property
    def description(self) -> str:
        return '''
        Increases CritRate by 20%
        Cooldown 35 seconds
        '''

    @property
    def cooldown(self) -> int:
        return 35

    def _on_activate(self):
        self.character.stats.crit_rate.add_value(20)
        invoke(lambda: self.character.stats.crit_rate.remove_value(20), delay=10)
        self.deactivate()
