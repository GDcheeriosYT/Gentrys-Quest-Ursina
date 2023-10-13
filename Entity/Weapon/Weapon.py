import Game
from ..GameEntityBase import GameEntityBase
from ursina import *
from utils.Event import Event
from utils.TypeMethods import determine_hit_type
from Entity.Buff import Buff
from Entity.EntityPool import EntityPool
from Graphics.TextStyles.DamageText import DamageText


class Weapon(GameEntityBase):
    def __init__(self, buff: Buff = Buff(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_attack = Event('onAttack')
        self.on_equip = Event('onEquip')
        self.on_de_equip = Event('onDeEquip')
        self._equipped_entity = None
        self.buff = buff
        self.buff.handle_value(self.star_rating)
        self._instance = None
        self._attacking = False
        self.damage = 0
        self.model = None
        self.entity_hit_type = None
        self.hit_list = []
        self.time_started = 0
        self.speed = 0
        self.angle = 0
        self.enable()
        self.update_stats()

        self.on_level_up += self.update_stats

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def base_attack(self) -> int:
        raise NotImplementedError

    @property
    def base_speed(self) -> int:
        raise NotImplementedError

    @property
    def weapon_type(self) -> str:
        raise NotImplementedError

    @property
    def texture(self) -> str:
        raise NotImplementedError

    @property
    def star_rating(self) -> int:
        raise NotImplementedError

    @property
    def range(self) -> int:
        raise NotImplementedError

    @property
    def equipped_entity(self):
        return self._equipped_entity

    def update_stats(self):
        self.damage = int(self.base_attack + (self.experience.level * 1.2) + (self.star_rating * self.experience.level))
        self.buff.level = self.experience.level
        self.buff.handle_value(self.star_rating, True)
        self.try_update_equipped_stats()

    def try_update_equipped_stats(self):
        try:
            self._equipped_entity.update_stats
        except AttributeError:
            pass

    def equip(self, entity):
        self._equipped_entity = entity
        self.entity_hit_type = determine_hit_type(self._equipped_entity)
        self.on_equip()

    def de_equip(self):
        self._equipped_entity = None
        self.on_de_equip()

    def is_ready(self) -> bool:
        return not self._attacking

    def attack(self, direction):
        self._attacking = True
        self.on_attack()
        return self.attack_process(direction)

    def destroy_instance(self):
        destroy(self._instance)
        self._instance = None
        self._attacking = False

    def attack_process(self, direction):
        pass

    def manage_collision(self, is_down: bool = True):
        hit_info = raycast(
            self._instance.world_position,
            self._instance.down if is_down else self._instance.up,
            ignore=[self],
            distance=self.range,
            debug=False
           )
        if hit_info.hit:
            try:
                hit_entity = hit_info.entity
                if hit_entity not in self.hit_list and self.matches_condition(hit_entity):
                    is_crit = random.randint(0, 100) < self._equipped_entity.stats.crit_rate.get_value()
                    crit_damage = (self._equipped_entity.stats.attack.get_value() * (
                                self._equipped_entity.stats.crit_damage.get_value() * 0.01)) if is_crit else 1
                    damage = self.damage + self._equipped_entity.stats.attack.get_value() + crit_damage
                    amount = int(round((damage * self.base_speed) - hit_entity.stats.defense.get_value()))
                    hit_entity.damage(amount, color.red if is_crit else color.white)
                    self.hit_list.append(hit_entity)
            except AttributeError as e:
                print(e)

    def matches_condition(self, entity) -> bool:
        print(type(self._equipped_entity))
        print(type(entity))
        print(entity.affiliation, self._equipped_entity.affiliation)
        print(entity == self._equipped_entity)
        print(entity.check_affiliation(self._equipped_entity), Game.rules.friendly_fire)
        print(id(self._equipped_entity), id(entity))

        if entity == self._equipped_entity:
            return False

        if entity.check_affiliation(self._equipped_entity) and not Game.rules.friendly_fire:
            return False

        return True

    def jsonify(self):
        return {
            "buff": self.buff.jsonify(),
            "name": self.name,
            "description": self.description,
            "star rating": self.star_rating,
            "experience": {
                "xp required": self.experience.get_xp_required(self.star_rating),
                "level": self.experience.level,
                "xp": self.experience.xp,
                "previous xp required": 0
            }
        }
