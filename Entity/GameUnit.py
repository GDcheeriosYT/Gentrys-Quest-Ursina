from .GameEntityBase import GameEntityBase
from .Stats import Stats
from .TextureMapping import TextureMapping
from .AudioMapping import AudioMapping
from utils.Event import Event
from .EntityOverHead import EntityOverhead
from ursina import *


class GameUnit(GameEntityBase):
    def __init__(self):
        super().__init__()

        # event initialization
        self.on_heal = Event("OnHeal", 0)
        self.on_damage = Event("OnDamage", 0)
        self.on_attack = Event("OnAttack", 0)
        self.on_death = Event("OnDeath", 0)
        self.on_move = Event("OnMove", 0)

        self.on_level_up += self.print_data
        self.on_level_up += self.update_stats
        print("We just created a GameUnit!")

    @property
    def difficulty(self) -> int:
        return 1

    @property
    def overhead(self) -> EntityOverhead:
        print("I'm making a overhead")
        return EntityOverhead(self)

    @difficulty.setter
    def difficulty(self, value) -> None:
        self.difficulty = value

    @property
    def stats(self) -> Stats:
        return Stats()

    @property
    def texture_mapping(self) -> TextureMapping:
        return TextureMapping()

    @property
    def audio_mapping(self) -> AudioMapping:
        return AudioMapping()

    def set_idle_texture(self):
        self.texture = self.texture_mapping.get_idle_texture()

    def set_damage_texture(self):
        self.texture = self.texture_mapping.get_damage_texture()

    def damage(self, amount):
        self.stats.health.current_value -= amount
        self.on_damage()
        if self.stats.health.current_value <= 0:
            self.die()

    def heal(self, amount):
        self.stats.health.current_value += amount
        self.on_heal()

    def die(self):
        self.on_death()

    def move_left(self):
        self.x -= self.stats.speed.current_value * time.dt
        self.on_move()

    def move_right(self):
        self.x += self.stats.speed.current_value * time.dt
        self.on_move()

    def move_up(self):
        self.y += self.stats.speed.current_value * time.dt
        self.on_move()

    def move_down(self):
        self.y -= self.stats.speed.current_value * time.dt
        self.on_move()

    def spawn(self) -> None:
        self.enable()
        self.spawn_sequence()

    def spawn_sequence(self) -> None:
        Audio(self.audio_mapping.get_spawn_sound())

    def print_data(self, *_) -> None:
        print(self.name)
        print(self.experience)
        print(self.stats)
