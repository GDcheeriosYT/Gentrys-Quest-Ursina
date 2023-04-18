from ursina import *
import random


class AudioMapping:
    def __init__(self, spawn_sounds: list = None, levelup_sounds: list = None, damage_sounds: list = None, death_sounds: list = None):
        if not spawn_sounds:
            self._spawn_sounds = ["audio/spawn.mp3"]
        else:
            self._spawn_sounds = spawn_sounds

        if not levelup_sounds:
            self._levelup_sounds = ["audio/levelup.mp3"]
        else:
            self._levelup_sounds = levelup_sounds

        if not damage_sounds:
            self._damage_sounds = ["audio/damage.mp3"]
        else:
            self._damage_sounds = damage_sounds

        if not death_sounds:
            self._death_sounds = ["audio/death.mp3"]
        else:
            self._death_sounds = death_sounds

    def get_spawn_sound(self):
        return random.choice(self._spawn_sounds)

    def get_levelup_sound(self):
        return random.choice(self._levelup_sounds)

    def get_damage_sounds(self):
        return random.choice(self._damage_sounds)

    def get_death_sounds(self):
        return random.choice(self._death_sounds)
