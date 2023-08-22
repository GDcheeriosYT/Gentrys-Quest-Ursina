from utils.Event import Event
from typing import Union
from ursina import *


class Effect:
    def __init__(self, ticks: int, delay: Union[int, float]):
        """
        Determines the values of the effect

        :param ticks: The amount of ticks before it finishes
        :param delay: The amount of time in seconds before activating the next tick
        """

        self._effector = None
        self._stack = 1
        self._counter = 0
        self.ticks = ticks
        self.delay = delay
        self._time_started = None

        # events
        self.on_effect = Event('onEffect', 0)
        self.on_effect += self._on_effect
        self.on_finish = Event("onFinish", 0)

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def description(self) -> str:
        raise NotImplementedError

    @property
    def texture(self) -> str:
        raise NotImplementedError

    def reset_counter(self):
        self._counter = 0

    def set_effector(self, entity):
        self._time_started = time.time()
        self._effector = entity

    def add_stack(self):
        self._stack += 1

    def get_stack(self):
        return self._stack

    def _on_effect(self):
        self._time_started = time.time()
        self._counter += 1
        if self._counter == self.ticks:
            self.finish()

    def finish(self):
        self.on_finish()
        self._effector.effects.remove(self)
        self._effector.on_affected()
        del self

    def effect(self):
        if (time.time() - self._time_started) >= self.delay:
            self.on_effect()
            self._effector.on_affected()
