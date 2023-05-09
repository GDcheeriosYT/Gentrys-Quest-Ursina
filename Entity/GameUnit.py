import random

import GameConfiguration
from .GameEntityBase import GameEntityBase
from .Stats import Stats
from .TextureMapping import TextureMapping
from .AudioMapping import AudioMapping
from utils.Event import Event
from .EntityOverHead import EntityOverhead
from ursina import *
from .Weapon.Weapon import Weapon

low = GameConfiguration.random_pitch_range[0]
high = GameConfiguration.random_pitch_range[1]


class GameUnit(GameEntityBase):
    def __init__(self, texture_mapping: TextureMapping, audio_mapping: AudioMapping):
        super().__init__(
            scale=(1, 1),
        )
        self._stats = Stats()
        self._overhead = EntityOverhead(self)
        self._difficulty = 1
        self._texture_mapping = texture_mapping
        self._audio_mapping = audio_mapping

        # event initialization
        self.on_heal = Event("OnHeal", 0)
        self.on_damage = Event("OnDamage", 0)
        self.on_attack = Event("OnAttack", 0)
        self.on_death = Event("OnDeath", 0)
        self.on_move = Event("OnMove", 0)
        self.on_spawn = Event("OnSpawn", 0)

        self.on_level_up += self.print_data
        self.on_level_up += self.update_stats
        self.on_level_up += self._overhead.update_data
        self.on_level_up += lambda: Audio(self.audio_mapping.get_levelup_sound(), volume=GameConfiguration.volume)
        self.on_spawn += self.update_stats
        self.on_heal += self._overhead.update_data
        self.on_damage += self._overhead.update_data
        self.on_damage += lambda: Audio(self.audio_mapping.get_damage_sounds(), pitch=random.uniform(low, high), volume=GameConfiguration.volume)
        self.on_death += lambda: Audio(self.audio_mapping.get_death_sounds(), pitch=random.uniform(low, high), volume=GameConfiguration.volume)

        # equips
        self._weapon = None

    @property
    def difficulty(self) -> int:
        return self._difficulty

    @property
    def stats(self) -> Stats:
        """
        The stats of the Entity
        """
        return self._stats

    @property
    def texture_mapping(self) -> TextureMapping:
        return self._texture_mapping

    @property
    def audio_mapping(self) -> AudioMapping:
        return self._audio_mapping

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    def set_idle_texture(self):
        self.texture = self._texture_mapping.get_idle_texture()

    def set_damage_texture(self):
        self.texture = self._texture_mapping.get_damage_texture()

    def damage(self, amount):
        self.stats.health.current_value -= amount
        self.on_damage()
        damage_text = Text(str(amount), scale=(15, 15), origin=(0, 0), position=(0, 0.5, -1), color=rgb(255, 12, 12), parent=self)
        damage_text.animate_position((damage_text.x + 0.1, damage_text.y + 0.5), 1)
        damage_text.fade_out(0, 1)
        destroy(damage_text, delay=1.5)
        if self.stats.health.current_value <= 0:
            self.die()

    def swap_weapon(self, weapon: Weapon) -> Weapon:
        old_weapon = self._weapon
        self._weapon = weapon
        return old_weapon

    def attack(self):
        crit_damage = (self._stats.attack.get_value() + (self._stats.crit_damage.get_value() * 0.01)) if random.randint(0, 100) < self._stats.crit_rate.get_value() else 0
        damage = int(round(self._stats.attack.get_value() * crit_damage))
        self.on_attack()
        self.weapon.attack(damage, self._stats.attack_speed.get_value())

    def heal(self, amount):
        self.stats.health.current_value += amount
        self.on_heal()

    def die(self):
        self.disable()
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
        self.on_spawn()
        Audio(self._audio_mapping.get_spawn_sound(), pitch=random.uniform(low, high), volume=GameConfiguration.volume)
        self._overhead.entity_name.text = self.name

    def print_data(self, *_) -> None:
        print(self.name, self._difficulty)
        print(self._experience)
        print(self._stats)
