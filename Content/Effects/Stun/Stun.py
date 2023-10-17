from ursina import *

from Entity.Effect import Effect
from typing import Union


class Stun(Effect):
    def __init__(self, delay: Union[int, float] = inf):
        super().__init__(ticks=1, delay=delay)

    @property
    def name(self) -> str:
        return "Stun"

    @property
    def texture(self) -> str:
        return "stun.png"

    @property
    def description(self) -> str:
        return f"stuns the entity for x seconds"
