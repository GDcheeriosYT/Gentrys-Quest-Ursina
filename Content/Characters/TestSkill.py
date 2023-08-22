from Entity.Character.Skill.Skill import Skill


class TestSkill(Skill):
    def __init__(self):
        super().__init__()
        self.on_activate += self._on_activate

    @property
    def name(self) -> str:
        return "Test Skill"

    def _on_activate(self):
        self.deactivate()

    @property
    def description(self) -> str:
        return f'''
        test skill
        '''

    @property
    def cooldown(self) -> int:
        return 1
