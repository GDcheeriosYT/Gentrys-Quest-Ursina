import random

import Game
from Content.Enemies.TestEnemy import TestEnemy
from Content.ArtifactFamilies.TestFamily.TestFamily import TestFamily


class Map:
    def __init__(
            self,
            entities: list = None,
            enemies: list = None,
            difficulty: int = 0,
            difficulty_scales: bool = True,
            enemy_limit: int = 5,
            artifact_families: list = None
    ):
        if enemies:
            self.enemies = enemies
        else:
            self.enemies = [TestEnemy]

        if entities:
            self.entities = entities
        else:
            self.entities = []

        if artifact_families:
            self.artifact_families = artifact_families
        else:
            self.artifact_families = [TestFamily()]

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
        spawn_amount = random.randint(1, self.current_difficulty * 2)
        if len(self.enemy_tracker) + spawn_amount <= self.enemy_limit:
            for i in range(spawn_amount):
                enemy = random.choice(self.enemies)()
                enemy.experience.level = ((self.current_difficulty - 1) * 20) + ((Game.user.get_equipped_character().experience.level % 20) + random.randint(0, 3))
                enemy.follow_entity(Game.user.get_equipped_character())
                enemy.position = Game.user.get_equipped_character().position
                enemy.y += random.randint(-7, 7)
                enemy.x += random.randint(-7, 7)
                enemy.spawn()
                enemy.on_death += lambda: Game.user.user_data.add_artifact(self.generate_artifact())
                enemy.on_death += lambda: Game.user.get_equipped_character().manage_loot(enemy.get_loot())
                enemy.on_death += lambda: self.enemy_tracker.pop(0)
                self.enemy_tracker.append(enemy)

    def generate_artifact(self):
        random_num = random.randint(0, int(10000/self.current_difficulty))
        star_rating = 1
        if random_num <= 3500:
            star_rating = 2
        elif random_num <= 2000:
            star_rating = 3
        elif random_num <= 750:
            star_rating = 4
        elif random_num <= 300:
            star_rating = 5

        artifact = random.choice(self.artifact_families).get_random_artifact()()
        artifact.star_rating = star_rating
        print(artifact)
        return artifact

    def calculate_difficulty(self, player):
        if self.difficulty_scales:
            self.current_difficulty = self.difficulty + player.difficulty
        else:
            self.current_difficulty = self.difficulty
