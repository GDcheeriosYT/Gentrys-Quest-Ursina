from Entity.Enemy.Enemy import Enemy


class TestEnemey(Enemy):
    def __init__(self):
        super().__init__()
    
    @property
    def name(self) -> str:
        return "Test Enemy"

