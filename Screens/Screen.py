from ursina import *
from utils.Event import Event


class Screen(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )
        # if self.allow_back: self.back_button = Button("back", position=(-0.5, -0.4), scale=(0.2, 0.05))
        self.on_show = Event('OnShow', 0)
        self.on_hide = Event('OnHide', 0)

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
    def allow_back(self) -> bool:
        """
        Whether the user is allowed to use the back button to navigate away from this screen.
        """
        return True

    def on_back_button(self) -> bool:
        """
        Called when the user presses the back button while this screen is active.

        Returns:
            bool: True if the back button press should be handled by this screen, False otherwise.
        """
        return False

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

    def hide(self) -> None:
        self.disable()
        self.on_hide()
