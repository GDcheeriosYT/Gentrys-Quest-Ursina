from ursina import *

from typing import Union
import random

import Game

from Content.Enemies.TestEnemy import TestEnemy
from Content.ArtifactFamilies.TestFamily.TestFamily import TestFamily
from Entity.EntityPool import EntityPool


class Map:
    def __init__(
            self,
            name: str = "Map",
            description: str = "This is an area...",
            entities: list = None,
            enemies: list = None,
            difficulty: int = 0,
            difficulty_scales: bool = True,
            enemy_limit: int = 5,
            artifact_families: list = None,
            music: list = None,
            spawn_delay: Union[int, float] = 7
    ):
        self.name = name

        self.description = description

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

        self.music_player = None

        self.spawn_delay = spawn_delay

        self.difficulty = difficulty
        self.difficulty_scales = difficulty_scales
        self.enemy_limit = enemy_limit
        self.current_difficulty = 0
        self.enemy_pool = None
        self.can_spawn = True

        self.enemy_tracker = []

        # state
        self.loaded = False

    def load(self):
        start_time = time.time()
        Game.notification_manager.add_notification(Game.Notification(f"loading {self.name}", color.yellow))
        self.calculate_difficulty(Game.user.get_equipped_character())
        self.enemy_pool = EntityPool(self.enemy_limit, self.enemies, True)
        [entity.enable() for entity in self.entities]
        Game.audio_system.set_music(random.choice(self.music))
        Game.notification_manager.add_notification(Game.Notification(f"Finished in {round(time.time() - start_time, 2)} seconds", color.yellow))
        self.loaded = True

    def unload(self):
        self.enemy_pool.destroy()
        [entity.disable() for entity in self.entities]
        destroy(self.music_player)
        self.loaded = False

    def destroy_enemies(self):
        for enemy in self.enemy_tracker:
            destroy(enemy)

        self.enemy_tracker.clear()

    def toggle_enemies(self):
        for enemy in self.enemy_tracker:
            enemy.disable() if enemy.enabled else enemy.enable()

    def spawn(self):
        if self.can_spawn:
            enemy = self.enemy_pool.get_entity(False)
            if enemy:
                enemy.position = (Game.user.get_equipped_character().position[0]+random.randint(-6, 6), Game.user.get_equipped_character().position[1]+random.randint(-6, 6))
                enemy.spawn()
                invoke(lambda: enemy.follow_entity(Game.user.get_equipped_character()), delay=1)

    def artifact_check(self):
        if Game.score_manager.spend_points(2500):
            Game.user.add_artifact(self.generate_artifact())

    def kill_all_enemies(self):
        for enemy in self.enemy_pool.pool:
            if enemy.enabled:
                enemy.die()

    def spawn_sequence(self):
        number = self.generate_enemy_spawn_number()
        for i in range(number):
            self.spawn()

    def generate_enemy_spawn_number(self):
        return random.randint(1, self.current_difficulty) * random.randint(1, 2)

    def generate_artifact(self):
        random_num = random.randint(0, int(10000/self.current_difficulty))
        star_rating = 1
        if random_num <= 300:
            star_rating = 5
        elif random_num <= 750:
            star_rating = 4
        elif random_num <= 2000:
            star_rating = 3
        elif random_num <= 3500:
            star_rating = 2

        artifact = random.choice(self.artifact_families).get_random_artifact()(star_rating)
        return artifact

    def calculate_difficulty(self, player):
        if self.difficulty_scales:
            self.current_difficulty = self.difficulty + player.difficulty
        else:
            self.current_difficulty = self.difficulty

        if self.enemy_pool:
            del self.enemy_pool