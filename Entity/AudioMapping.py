from ursina import *
import random


class AudioMapping:
    def __init__(self, spawn_sounds: list = None):
        if not spawn_sounds:
            self._spawn_sounds = ["audio/spawn.mp3"]
        else:
            self._spawn_sounds = spawn_sounds

    def get_spawn_sound(self):
        return random.choice(self._spawn_sounds)
