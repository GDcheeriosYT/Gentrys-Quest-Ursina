from ursina import *

from Entity.Enemy.Enemy import Enemy


class TestEnemy(Enemy):
    def __init__(self):
        super().__init__()
    
    @property
    def name(self) -> str:
        return "Test Enemy"

    def update(self):
        if held_keys['/']:
            self.damage(5)

        if held_keys['=']:
            self.level_up()
        if held_keys["-"]:
            if self.experience.level > 1:
                self.experience.level -= 1
                self.on_level_up()
                self.update_stats()
