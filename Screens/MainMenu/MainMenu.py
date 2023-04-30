from ..Screen import Screen
from Graphics.TextStyles.TitleText import TitleText
from Graphics.TextStyles.VersionText import VersionText
from Graphics.FadeScreen import FadeScreen
from Graphics.Buttons.TabButton import TabButton
from .LoginBox import LoginBox
from utils.BooleanMethods import switch


from ursina import *

def mode_switch_checker():
    if MainMenu.is_guest_menu:
        pass



class MainMenu(Screen):
    intro_music = None
    title = TitleText("Gentry's Quest")
    version = None
    play_button = Button("Play", position=(0, -0.1), scale=(0.2, 0.05))
    is_guest_menu = True
    is_login_menu = False
    guest_button = TabButton("Guest", position=(-0.20, 0.45))
    guest_button.on_click =
    login_button = TabButton("Login", position=(0.20, 0.45))
    menu = Entity("quad", scale=(1, 1), parent=camera.ui)
    guest_button.disable()
    login_button.disable()

    def __init__(self, version: str, intro_music: Audio):
        super().__init__()
        MainMenu.intro_music = intro_music
        MainMenu.version = VersionText(version)
        MainMenu.play_button.on_click = self.play
        self.show()

    @property
    def name(self) -> str:
        return "Main Menu"

    @property
    def allow_back(self) -> bool:
        return False

    def on_show(self) -> None:
        self.title.fade_in(1, 1)

    def on_hide(self) -> None:
        self.title.fade_out(0, 0.5)
        self.play_button.fade_out(0, 0.5)

    def play(self) -> None:
        time = 0.6
        MainMenu.intro_music.fade_out(0, time)
        invoke(lambda: MainMenu.intro_music.disable(), delay=time)
        fade_screen = FadeScreen()
        fade_screen.fade_in(1, time)
        invoke(lambda: MainMenu.play_button.disable(), delay=time)
        invoke(lambda: MainMenu.title.disable(), delay=time)
        invoke(lambda: MainMenu.guest_button.enable(), delay=time)
        invoke(lambda: Entity(model='quad', position=(0, 0.45), origin=(0, 0.5), color=rgb(0,0,0), scale=(0.05, 0.15), parent=camera.ui), delay=time)
        invoke(lambda: MainMenu.login_button.enable(), delay=time)
        ambient_1 = Audio("Audio/Gentrys_Quest_Ambient_1.mp3", volume=0, loop=True)
        invoke(lambda: ambient_1.fade_in(1, time), delay=time * 2)
        invoke(lambda: fade_screen.fade_out(0, time), delay=time * 2)

    def update(self):
        if MainMenu.is_guest_menu:
            MainMenu.guest_button.color = color.white
