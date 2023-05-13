from Entity.Character.Skill.Skill import Skill
from ursina import *


class BrutalOverdose(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate

    @property
    def name(self) -> str:
        return "Brutal Overdose"

    def _on_activate(self):
        times = 10

        def hit_check(instance: Entity):
            nonlocal times
            entity = instance.intersects().entity
            try:
                if entity is not self.character:
                    entity.damage(self.character.stats.health.get_percent_of_stat(25))
            except AttributeError:
                pass

            times -= 1

        self._instance = Entity(
            model='circle',
            scale=(5, 5),
            collider='sphere',
            color=rgb(200, 0, 0, 200),
            position=self.character.position
        )

        invoke(lambda: hit_check(self._instance), delay=1)
        destroy(self._instance, 10)
        self.deactivate()

    @property
    def icon(self):
        return "Textures/odicon.jpg"

    @property
    def description(self) -> str:
        return '''
        Damage and stun enemies in radius
        cooldown 90 seconds
        '''

    @property
    def cooldown(self) -> int:
        return 90
