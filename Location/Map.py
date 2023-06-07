from ursina import *
import random
import Game
import GameConfiguration
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
            artifact_families: list = None,
            music: list = None
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

        if music:
            self.music = music
        else:
            self.music = ["Audio/questfightvidgame.mp3", "Audio/1drill.mp3", "Audio/90ssound.mp3", "Audio/ooky.mp3", "Audio/gentrys_quest_jungle_1.mp3"]

        self.difficulty = difficulty
        self.difficulty_scales = difficulty_scales
        self.enemy_limit = enemy_limit
        self.current_difficulty = 0
        self.can_spawn = True

        self.enemy_tracker = []

    def load(self):
        self.calculate_difficulty(Game.user.get_equipped_character())
        self.manage_entities(True, True)
        self.music = Audio(random.choice(self.music), volume=GameConfiguration.volume, loop=True)

    def unload(self):
        self.manage_entities(True, False)

    def manage_entities(self, unloaded: bool = True, enable: bool = True):
        entity_list = self.entities if unloaded else self.enemy_tracker

        for entity in entity_list:
            entity.enable() if enable else entity.disable()

    def spawn_sequence(self):
        self.calculate_difficulty(Game.user.get_equipped_character())
        spawn_amount = random.randint(1, self.current_difficulty * 2)
        if len(self.enemy_tracker) + spawn_amount <= self.enemy_limit and self.can_spawn:
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
        return artifact

    def calculate_difficulty(self, player):
        if self.difficulty_scales:
            self.current_difficulty = self.difficulty + player.difficulty
        else:
            self.current_difficulty = self.difficulty
