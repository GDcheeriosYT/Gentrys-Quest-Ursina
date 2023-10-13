from ursina import *

import Game
from ...Test import Test
from Entity.EntityPool import EntityPool

from Graphics.TextStyles.DamageText import DamageText
from Content.Enemies.AngryPedestrian.AngryPedestrian import AngryPedestrian
from Content.Enemies.AngryChineseMan.AngryChineseMan import AngryChineseMan


class EntityPoolTest(Test):
    def __init__(self):
        super().__init__(EntityPool)

        self.enemy_pool = None
        self.enemy_pool: EntityPool

        self.object_pool = None
        self.object_pool: EntityPool

        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        def create_object_pool():
            if self.object_pool:
                self.object_pool.destroy()

            self.object_pool = EntityPool(10, DamageText)

        def create_enemy_pool():
            if self.enemy_pool:
                self.enemy_pool.destroy()

            self.enemy_pool = EntityPool(10, Game.content_manager.enemies)

        self.make_button("Create Object Pool", create_object_pool)
        self.make_button("Create Enemy Pool", create_enemy_pool)

    def _unload(self):
        self.object_pool.destroy()
        self.enemy_pool.destroy()
