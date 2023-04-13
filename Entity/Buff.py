class Buff:
    def __init__(self, stat: str):
        self._stat = stat
        self._level = 1

    @property
    def stat(self) -> str:
        return self._stat

    @property
    def level(self) -> int:
        return self._level
