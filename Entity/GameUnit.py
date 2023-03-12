from .GameEntityBase import GameEntityBase
from .Stats import Stats
from .TextureMapping import TextureMapping
from utils.Event import Event
from .EntityOverHead import EntityOverhead
from ursina import *


class GameUnit(GameEntityBase):

    @property
    def overhead(self) -> EntityOverhead:
        raise NotImplementedError

    @property
    def difficulty(self) -> int:
        return 1

    @difficulty.setter
    def difficulty(self, value) -> None:
        self.difficulty = value

    @property
    def stats(self) -> Stats:
        return Stats()

    @property
    def texture_mapping(self) -> TextureMapping:
        return TextureMapping()

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
        self.x -= self.stats.speed.get_value() * time.dt
        self.on_move()

    def move_right(self):
        self.x += self.stats.speed.get_value() * time.dt
        self.on_move()

    def move_up(self):
        self.y += self.stats.speed.get_value() * time.dt
        self.on_move()

    def move_down(self):
        self.y -= self.stats.speed.get_value() * time.dt
        self.on_move()

    # events
    @property
    def on_heal(self) -> Event:
        return Event("OnHeal", 0)

    @property
    def on_damage(self) -> Event:
        return Event("OnDamage", 0)

    @property
    def on_attack(self) -> Event:
        return Event("OnAttack", 0)

    @property
    def on_death(self) -> Event:
        return Event("OnDeath", 0)

    @property
    def on_move(self) -> Event:
        return Event("OnMove", 0)