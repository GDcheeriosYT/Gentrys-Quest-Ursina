from ursina import *
import random
import os


class TextureMapping:
    def __init__(self, idle_textures: list = None, damage_textures: list = None, walk_textures: list = None):
        if not idle_textures:
            self._idle_textures = ["Textures/huh.png"]
        else:
            self._idle_textures = idle_textures

        if not damage_textures:
            self._damage_textures = ["Textures/huh.png"]
        else:
            self._damage_textures = damage_textures

        if not walk_textures:
            self._walk_textures = ["Textures/huh.png"]
        else:
            self._walk_textures = walk_textures

    def get_idle_texture(self):
        return random.choice(self._idle_textures)

    def get_damage_texture(self):
        return random.choice(self._damage_textures)

    # def play_walk_animation(self, entity):
    #         entity.animate(frames=self._walk_textures, fps=5)
