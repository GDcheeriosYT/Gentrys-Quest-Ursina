from ursina import *


class Screen(Entity):
    def __init__(self):
        super().__init__()
        if self.allow_back: self.back_button = Button("back", position=(-0.5, -0.4), scale=(0.2, 0.05))

    @property
    def name(self) -> str:
        print("screen name given")
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

    def show(self) -> None:
        self.on_show()

    def hide(self) -> None:
        self.on_hide()

    def on_show(self) -> None:
        """
        Called when this screen is shown.
        """
        pass

    def on_hide(self) -> None:
        """
        Called when this screen is hidden.
        """
        pass
