import Game
import GameConfiguration
from Graphics.TextStyles.DamageText import DamageText
from .EntityPool import EntityPool
from .GameEntityBase import GameEntityBase
from .Stats import Stats
from .TextureMapping import TextureMapping
from .AudioMapping import AudioMapping
from utils.Event import Event
from .EntityOverHead import EntityOverhead
from ursina import *
from .Loot import Loot
from .Effect import Effect
from .Affiliation import Affiliation

low = GameConfiguration.random_pitch_range[0]
high = GameConfiguration.random_pitch_range[1]


class GameUnit(GameEntityBase):
    def __init__(self, texture_mapping: TextureMapping, audio_mapping: AudioMapping, *args, **kwargs):
        super().__init__(
            scale=(1, 1),
            collider='box',
            *args,
            **kwargs
        )

        self._stats = Stats()
        self._overhead = EntityOverhead(self)
        self._difficulty = 1
        self._texture_mapping = texture_mapping
        self._audio_mapping = audio_mapping
        self.direction = Vec3(0, 0, 0).normalized()
        self.dead = False
        self.spawned = False
        self.range = 1
        self.damage_text_pool = EntityPool(20, DamageText)
        self.effects = []
        self.affiliation = Affiliation.Neutral
        self.is_current_player = False

        # audio
        # no audio lol

        # event initialization
        self.on_heal = Event("OnHeal", 0)
        self.on_damage = Event("OnDamage", 0)
        self.on_attack = Event("OnAttack", 0)
        self.on_death = Event("OnDeath", 0)
        self.on_move = Event("OnMove", 0)
        self.on_spawn = Event("OnSpawn", 0)
        self.on_update_stats = Event("OnUpdateStats", 0)
        self.on_swap_weapon = Event("OnSwapWeapon", 0)
        self.on_affected = Event("OnAffected", 0)

        self.on_level_up += self.print_data
        self.on_level_up += self.update_stats
        self.on_level_up += self._overhead.update_data
        self.on_level_up += lambda: Game.audio_system.play_sound(self._audio_mapping.get_levelup_sound(), True)
        self.on_spawn += self.update_stats
        self.on_heal += self._overhead.update_data
        self.on_damage += self._overhead.update_data
        self.on_damage += lambda: Game.audio_system.play_sound(self._audio_mapping.get_damage_sounds(), True)
        self.on_death += lambda: Game.audio_system.play_sound(self._audio_mapping.get_death_sounds(), True)
        self.on_swap_weapon += self.update_stats
        # self.on_move += self._texture_mapping.play_walk_animation(self)

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
    def weapon(self):
        return self._weapon

    def set_idle_texture(self):
        self.texture = self._texture_mapping.get_idle_texture()

    def set_damage_texture(self):
        self.texture = self._texture_mapping.get_damage_texture()

    def damage(self, amount: int, color: Vec4 = color.white):
        Game.score_manager.add_damage(amount)
        self._stats.health.current_value -= amount if amount > 0 else 0
        # self.set_damage_texture()
        self.damage_text_pool.get_entity().display(amount if amount > 0 else "miss", color, self)
        self.on_damage()
        if self.stats.health.current_value <= 0:
            self.die()

    def swap_weapon(self, weapon):
        old_weapon = self._weapon
        if old_weapon:
            old_weapon.on_level_up -= self.update_stats
            self._weapon.de_equip()

        self._weapon = weapon
        self._weapon.equip(self)
        if weapon:
            self.range = 1 + self._weapon.range
        self._weapon.on_level_up += self.update_stats
        self.on_swap_weapon()
        if old_weapon:
            return old_weapon

    def apply_effect(self, effect: Effect):
        found_extra = False
        for personal_effect in self.effects:
            if effect.name == personal_effect.name:
                personal_effect.add_stack()
                personal_effect.reset_counter()
                found_extra = True

        if not found_extra:
            effect.set_effector(self)
            self.effects.append(effect)

        self.on_affected()

    def is_effected_by(self, name: str):
        for effect in self.effects:
            if effect.name == name:
                return True

        return False

    def remove_effect(self, name: str):
        for effect in self.effects:
            if effect.name == name:
                self.effects.remove(effect)

    def handle_buffs(self):
        for effect in self.effects:
            effect.effect()

    def attack(self, direction=None):
        if self._weapon:
            if self._weapon.is_ready():
                if not direction:
                    mouse_pos = mouse.position
                    direction = math.atan2(mouse_pos[1], mouse_pos[0]) * (180 / 3.14)
                else:
                    direction = math.atan2(direction[1], direction[0]) * (180 / 3.14)

                self.on_attack()
                self.weapon.attack(direction)

    def heal(self, amount):
        Game.score_manager.add_heal(amount)
        if self.is_current_player:
            Game.stats.add_heal(amount)

        self.stats.health.current_value += amount
        self.on_heal()

    def recover_health(self):
        self.stats.health.calculate_value()
        self.on_heal()

    def die(self):
        self.disable()
        self.dead = True
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
        Game.audio_system.play_sound(self._audio_mapping.get_spawn_sound(), True)
        self.update_stats()
        self._stats.restore_stats()
        self._overhead.update_data()
        self.dead = False
        self.spawned = True

    def hits(self, direction):
        origin = self.world_position
        hit_info = raycast(origin, direction, ignore=[self], distance=.1, debug=False)
        return hit_info.hit

    def despawn(self):
        self.disable()
        self.dead = False
        self.spawned = False

    def get_loot(self) -> Loot:
        return Loot()

    def on_destroy(self):
        self.dead = True

    def print_data(self, *_) -> None:
        print(self.name, self._difficulty)
        print(self._experience)
        print(self._stats)

    def check_affiliation(self, entity) -> bool:
        return entity.affiliation == self.affiliation
