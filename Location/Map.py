import random

import Game
from Content.Enemies.TestEnemy import TestEnemy


class Map:
    def __init__(
            self,
            entities: list = None,
            enemies: list = None,
            difficulty: int = 1,
            difficulty_scales: bool = True,
            enemy_limit: int = 5
    ):
        if enemies:
            self.enemies = enemies
        else:
            self.enemies = [TestEnemy]

        if entities:
            self.entities = entities
        else:
            self.entities = []

        self.difficulty = difficulty
        self.difficulty_scales = difficulty_scales
        self.enemy_limit = enemy_limit
        self.current_difficulty = 0

        self.enemy_tracker = []

    def load(self):
        self.calculate_difficulty(Game.user.get_equipped_character())
        for entity in self.entities:
            entity.enable()

    def unload(self):
        for entity in self.entities:
            entity.disable()

    def spawn_sequence(self):
        spawn_amount = random.randint(1, self.current_difficulty)
        if len(self.enemy_tracker) + spawn_amount < self.enemy_limit:
            for i in range(spawn_amount):
                enemy = random.choice(self.enemies)()
                enemy.experience.level = (self.current_difficulty * 20) + ((Game.user.get_equipped_character().experience.level % 20) + random.randint(-3, 3))
                enemy.follow_entity(Game.user.get_equipped_character())
                enemy.position = Game.user.get_equipped_character().position
                enemy.y += random.randint(-7, 7)
                enemy.x += random.randint(-7, 7)
                enemy.spawn()
                self.enemy_tracker.append(enemy)

    def calculate_difficulty(self, player):
        if self.difficulty_scales:
            self.current_difficulty = self.difficulty + player.difficulty
        else:
            self.current_difficulty = self.difficulty
