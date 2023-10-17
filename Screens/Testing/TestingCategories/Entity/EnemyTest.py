from ursina import *

import Game
from ...Test import Test

from Entity.Enemy.Enemy import Enemy
from Content.Enemies.TestEnemy import TestEnemy


class EnemyTest(Test):
    def __init__(self):
        super().__init__(Enemy)

        # create blank character tracker
        self.enemy = None
        self.enemy: TestEnemy

        self.test_follow_entity = None

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        def create_enemy():
            if not self.enemy:
                self.enemy = TestEnemy(parent=Test.screen)
                self.test_follow_entity = Entity()

        # tests
        # test spawn button
        self.make_button("Create Enemy", create_enemy)
        self.get_button(index=0).on_click()
        self.enemy.follow_entity(self.test_follow_entity)
        self.enemy.apply_effect(Game.content_manager.get_effect("Stun"))
        self.enemy.attack_switch(False)
        self.enemy.scale = (0.2, 0.2)

        self.make_button("Spawn Enemy", self.enemy.spawn)
        self.make_button("Kill Enemy", self.enemy.die)
        self.make_button("Damage Enemy", lambda: self.enemy.damage(100))
        self.make_button("Heal Enemy", lambda: self.enemy.heal(100))

    def _unload(self):
        destroy(self.enemy)
        destroy(self.test_follow_entity)
