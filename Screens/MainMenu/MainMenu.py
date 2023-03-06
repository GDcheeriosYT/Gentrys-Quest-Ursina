from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText

from ursina.prefabs.button import Button


class MainMenu(Screen):
    def __init__(self):
        self.title = TitleText("Gentry's Quest", hidden=True)
        self.play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
        super().__init__()

    @property
    def name(self) -> str:
        return "Main Menu"

    def on_show(self) -> None:
        self.title.fade_in(1, 2)

    def on_hide(self) -> None:
        self.title.fade_out(0, 0.5)
        self.play_button.fade_out(0, 0.5)