from ursina import *

import Game

from ...Test import Test
from ...TestTypes import TestTypes

from Overlays.Notification import Notification
from Content.Enemies.TestEnemy import TestEnemy
from Content.Characters.TestCharacter import TestCharacter
from Content.Weapons.Knife.Knife import Knife


class Fight():  # just a name class
    pass


class FightTest(Test):
    def __init__(self):
        super().__init__(Fight, TestTypes.NotScreenTest)
        self.on_load += self._load
        self.on_unload += self._unload

        self._player = None
        self._player: TestCharacter
        self._enemy = None
        self._enemy: TestEnemy

    def _load(self):
        def set_scene():
            self._player = TestCharacter(position=(0, -2.5))
            self._player.apply_effect(Game.content_manager.get_effect("Stun"))
            self._player.scale = (1.5, 1.5)
            self._player.swap_weapon(Knife())

            self._enemy = TestEnemy(position=(0, 0))
            self._enemy.apply_effect(Game.content_manager.get_effect("Stun"))
            self._enemy.scale = (1.5, 1.5)

            self._player.spawn(), self._enemy.spawn()

        def player_attack():
            if self._player:
                self._player.attack((0, 1))

        def enemy_attack():
            if self._enemy:
                self._enemy.attack((0, -1))

        def randomize_weapons():
            random_weapon = random.choice(Game.content_manager.weapons)().name
            Game.notification_manager.add_notification(Notification(f"Got {random_weapon}", color=color.blue))
            self._player.swap_weapon(Game.content_manager.get_weapon(random_weapon))
            self._enemy.swap_weapon(Game.content_manager.get_weapon(random_weapon))

        self.make_button("Set Scene", set_scene)
        self.get_button(index=0).on_click()
        self.make_button("Player Attack", player_attack)
        self.make_button("Enemy Attack", enemy_attack)
        self.make_button("Random Weapon", randomize_weapons)

    def _unload(self):
        destroy(self._player)
        destroy(self._enemy)
