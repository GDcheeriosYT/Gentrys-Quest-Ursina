from Entity.Enemy.Enemy import Enemy


class TestEnemey(Enemy):

    @property
    def name(self) -> str:
        return "Test Enemy"