from ursina import *
from Graphics.Container import Container
from Entity.Character import Character


class SkillsContainer(Container):
    def __init__(self, player):
        text_size = (2.6, 2.6)
        text_height = 0.2
        self._player = player
        super().__init__(
            position=(0.6, -0.37),
            scale=(0.7, 0.5)
        )
        self.primary_info = Text("ready", position=(-0.5, text_height), scale=text_size, origin=(0, 0), parent=self)
        self.primary_key = Text("M1", position=(-0.5, -text_height), scale=text_size, origin=(0, 0), parent=self)
        self.primary_box = Entity(
            model='quad',
            position=(-0.5, 0),
            scale=(0.25, 0.25),
            parent=self
        )
        self.secondary_info = Text("ready", position=(-0.25, text_height), scale=text_size, origin=(0, 0), parent=self)
        self.secondary_key = Text("M2", position=(-0.25, -text_height), scale=text_size, origin=(0, 0), parent=self)
        self.secondary_box = Entity(
            model='quad',
            position=(-0.25, 0),
            scale=(0.25, 0.25),
            parent=self
        )
        self.utility_info = Text("ready", position=(0, text_height), scale=text_size, origin=(0, 0), parent=self)
        self.utility_key = Text("Shift", position=(0, -text_height), scale=text_size, origin=(0, 0), parent=self)
        self.utility_box = Entity(
            model='quad',
            position=(0, 0),
            scale=(0.25, 0.25),
            parent=self
        )
        self.ultimate_info = Text("ready", position=(0.25, text_height), scale=text_size, origin=(0, 0), parent=self)
        self.ultimate_key = Text("C", position=(0.25, -text_height), scale=text_size, origin=(0, 0), parent=self)
        self.ultimate_box = Entity(
            model='quad',
            position=(0.25, 0),
            scale=(0.25, 0.25),
            parent=self
        )

    def update(self):
        try:
            self.primary_box.texture = self._player.weapon.texture
            self.primary_info.text = "ready" if self._player.weapon.is_ready() else "not ready"
        except:
            pass
        try:
            self.secondary_box.texture = self._player.secondary.icon
            self.secondary_info.text = "ready" if self._player.secondary.is_ready else f"{int(self._player.secondary.percentage*100)}%"
        except:
            pass
        try:
            self.utility_box.texture = self._player.utility.icon
            self.utility_info.text = "ready" if self._player.utility.is_ready else f"{int(self._player.utility.percentage*100)}%"
        except:
            pass
        try:
            self.ultimate_box.texture = self._player.ultimate.icon
            self.ultimate_info.text = "ready" if self._player.ultimate.is_ready else f"{int(self._player.ultimate.percentage*100)}%"
        except:
            pass
