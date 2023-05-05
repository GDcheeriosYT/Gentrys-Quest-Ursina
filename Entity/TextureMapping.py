from ursina import *
import random
import os


class TextureMapping:
    def __init__(self, idle_textures: list = None, damage_textures: list = None):
        if not idle_textures:
            self._idle_textures = ["Textures/huh.png"]
        else:
            self._idle_textures = idle_textures

        if not damage_textures:
            self._damage_textures = ["Textures/huh.png"]
        else:
            self._damage_textures = damage_textures

    def get_idle_texture(self):
        return random.choice(self._idle_textures)

    def get_damage_texture(self):
        return random.choice(self._damage_textures)
