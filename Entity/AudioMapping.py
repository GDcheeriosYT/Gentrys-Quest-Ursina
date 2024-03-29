from ursina import *
import random


class AudioMapping:
    def __init__(self, spawn_sounds: list = None, levelup_sounds: list = None, damage_sounds: list = None, death_sounds: list = None):
        if not spawn_sounds:
            self._spawn_sounds = ["Entity/Audio/spawn.mp3"]
        else:
            self._spawn_sounds = spawn_sounds

        self._spawn_sounds = [Audio(file_path, autoplay=False) for file_path in self._spawn_sounds]

        if not levelup_sounds:
            self._levelup_sounds = ["Entity/Audio/levelup.mp3"]
        else:
            self._levelup_sounds = levelup_sounds

        self._levelup_sounds = [Audio(file_path, autoplay=False) for file_path in self._levelup_sounds]

        if not damage_sounds:
            self._damage_sounds = ["Entity/Audio/damage.mp3"]
        else:
            self._damage_sounds = damage_sounds

        self._damage_sounds = [Audio(file_path, autoplay=False) for file_path in self._damage_sounds]

        if not death_sounds:
            self._death_sounds = ["Entity/Audio/death.mp3"]
        else:
            self._death_sounds = death_sounds

        self._death_sounds = [Audio(file_path, autoplay=False) for file_path in self._death_sounds]

    def get_spawn_sound(self):
        return random.choice(self._spawn_sounds)

    def get_levelup_sound(self):
        return random.choice(self._levelup_sounds)

    def get_damage_sounds(self):
        return random.choice(self._damage_sounds)

    def get_death_sounds(self):
        return random.choice(self._death_sounds)
