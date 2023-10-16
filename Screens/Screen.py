from ursina import *

from GameStates import GameStates
from utils.Event import Event
from .BackButton import BackButton


class Screen(Entity):
    def __init__(self, allow_back: bool = False, return_to: GameStates = GameStates.mainMenu):
        super().__init__(
            parent=camera.ui
        )
        self.allow_back = allow_back
        self.back_button = BackButton(return_to)
        self.back_button.disable()
        if self.allow_back:
            self.back_button.enable()

        self.on_show = Event('OnShow')
        self.on_hide = Event('OnHide')

    @property
    def name(self) -> str:
        """
        The name of the screen. This should be a unique identifier.
        """
        raise NotImplementedError

    @property
    def color(self) -> color:
        return color.white

    @property
    def fades(self) -> bool:
        """
        Determines if the screen should fade or not on changing the screen
        """
        return True

    @staticmethod
    def disable_audio(audio: Audio, fade_time: int):
        audio.fade_out(duration=fade_time)
        invoke(lambda: audio.disable(), delay=fade_time + 5)

    def show(self) -> None:
        self.enable()
        self.on_show()
        if self.allow_back:
            self.back_button.enable()

    def hide(self) -> None:
        self.disable()
        self.on_hide()
        if self.allow_back:
            self.back_button.disable()

    def on_destroy(self):
        destroy(self.back_button)
