from ursina import *
import random


class AudioMapping:
    def __init__(self, spawn_sounds: list = None, levelup_sounds: list = None):
        if not spawn_sounds:
            self._spawn_sounds = ["audio/spawn.mp3"]
        else:
            self._spawn_sounds = spawn_sounds

        if not levelup_sounds:
            self._levelup_sounds = ["audio/levelup.mp3"]
        else:
            self._levelup_sounds = levelup_sounds

    def get_spawn_sound(self):
        return random.choice(self._spawn_sounds)

    def get_levelup_sound(self):
        return random.choice(self._levelup_sounds)
