from ursina import *

from Entity.Character.Skill.Skill import Skill


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
            intersection = instance.intersects()
            print(intersection.entities)
            entities = intersection.entities
            try:
                for entity in entities:
                    if entity != self.character:
                        entity.damage(self.character.stats.attack.get_percent_of_stat(105))
            except AttributeError:
                pass

            if times > 0:
                invoke(lambda: hit_check(self._instance), delay=1)

            times -= 1

        self._instance = Entity(
            model='circle',
            scale=(5, 5),
            collider='sphere',
            color=rgb(200, 0, 0, 200),
            position=self.character.position
        )

        self.character.animate_position((self.character.position[0] + 5, self.character.position[1] + 5))

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
