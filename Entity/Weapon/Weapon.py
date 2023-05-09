from ..GameEntityBase import GameEntityBase
from ursina import *
from utils.Event import Event


class Weapon(GameEntityBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_attack = Event('onAttack', 0)
        self.disable()

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
    def weapon_texture(self) -> str:
        raise NotImplementedError

    def attack(self, damage, speed):
        self.on_attack()
        damage += self.base_attack
        self.attack_process(damage, speed)

    #def handle_collision(self, damage):
    #    hit_info = raycast(self.position, self.left, ignore=[self], distance=1, debug=True)
    #    if hit_info.hit:
    #        enemy = hit_info.entity
    #        if isinstance(enemy, Enemy):
    #            enemy.damage(damage)
