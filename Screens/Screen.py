from ursina import *
from utils.Event import Event


class Screen(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )
        # if self.allow_back: self.back_button = Button("back", position=(-0.5, -0.4), scale=(0.2, 0.05))
        self.on_show = Event('OnShow', 0)
        self.on_show += self.enable
        self.on_hide = Event('OnHide', 0)
        self.on_hide += self.disable

    @property
    def name(self) -> str:
        """
        The name of the screen. This should be a unique identifier.
        """
        raise NotImplementedError

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

    def disable_audio(self, audio: Audio, fade_time: int):
        audio.fade_out(duration=fade_time)
        invoke(audio.disable(), delay=fade_time * 2)

    def show(self) -> None:
        self.on_show()

    def hide(self) -> None:
        self.on_hide()
