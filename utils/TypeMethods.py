from Entity.Enemy.Enemy import Enemy
from Entity.Character.Character import Character


def determine_hit_type(entity):
    if issubclass(type(entity), Enemy):
        return Character
    else:
        return Enemy
