from Entity.Character.Skill.Skill import Skill


class TheSecondBoofHit(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += lambda: self.character.heal(self.character.stats.health.get_value() * 0.1)
        self.on_activate += self.deactivate

    @property
    def name(self) -> str:
        return "The Second Boof Hit"

    @property
    def description(self) -> str:
        return f'''
        Heals 10% Health
        cooldown {self.cooldown} seconds
        '''

    @property
    def cooldown(self) -> int:
        return 7

    @property
    def icon(self) -> str:
        return "Textures/booficon.png"
