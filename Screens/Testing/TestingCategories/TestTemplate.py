from ursina import *

from ...Test import Test


class TestNameTest(Test):
    def __init__(self):
        super().__init__(TestClass)
        self.on_load += self._load
        self.on_unload += self._unload

    def _load(self):
        pass

    def _unload(self):
        pass
