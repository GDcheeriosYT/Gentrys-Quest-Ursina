import ursina.scene
from ursina import *
from typing import Union
import random
import Game
import copy
import GameConfiguration
from Content.Enemies.TestEnemy import TestEnemy
from Content.ArtifactFamilies.TestFamily.TestFamily import TestFamily
from Entity.EntityPool import EntityPool
from Overlays.Notification import Notification
from .MapPreview import MapPreview


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
            weapon_list: list = None,
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

        if weapon_list:
            self.weapon_list = weapon_list
        else:
            self.weapon_list = [Game.content_manager.get_weapon("Knife")]

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

    def load(self):
        print("started loading")
        self.destroy_enemies()
        self.calculate_difficulty(Game.user.get_equipped_character())
        self.enemy_pool = EntityPool(self.enemy_limit, self.enemies)
        print(self.enemy_pool)
        self.manage_entities(True)
        Game.audio_system.set_music(random.choice(self.music))
        print("finished")

    def unload(self):
        self.manage_entities(False)
        self.destroy_enemies()
        self.enemy_pool.destroy()
        destroy(self.music_player)

    def destroy_enemies(self):
        for enemy in self.enemy_tracker:
            destroy(enemy)

        self.enemy_tracker.clear()

    def toggle_enemies(self):
        for enemy in self.enemy_tracker:
            enemy.disable() if enemy.enabled else enemy.enable()

    def manage_entities(self, enable: bool = True):
        for entity in self.entities:
            entity.enable() if enable else entity.disable()

    def spawn(self):
        if self.can_spawn:
            enemy = self.enemy_pool.get_entity()
            if enemy:
                enemy.follow_entity(Game.user.get_equipped_character())
                enemy.spawn()

    def spawn_sequence(self):
        for i in range(self.generate_enemy_spawn_number()):
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

    def generate_weapon(self):
        weapon = type(random.choice(self.weapon_list))
        return weapon()

    def calculate_difficulty(self, player):
        if self.difficulty_scales:
            self.current_difficulty = self.difficulty + player.difficulty
        else:
            self.current_difficulty = self.difficulty

        if self.enemy_pool:
            del self.enemy_pool

    def generate_preview(self):
        return MapPreview(self)

    def get_metadata(self) -> str:
        return f"""
{self.name}
{self.description}
{len(self.entities)} entities
difficulty: {self.difficulty} scales({self.difficulty_scales})
enemy_limit: {self.enemy_limit}
        """
