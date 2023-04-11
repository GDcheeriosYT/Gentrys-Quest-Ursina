from ursina import *
from ..GameUnit import GameUnit
from typing import Union
from ..EntityOverHead import EntityOverhead


class Enemy(GameUnit):
    def __init__(self):
        super().__init__()
