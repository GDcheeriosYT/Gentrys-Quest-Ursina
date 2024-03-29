from ursina import *
from ursina.prefabs.input_field import InputField
from User.User import User
from Graphics.GameText import GameText
import Game


class LoginUI(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model="quad",
            origin=(0, 0),
            scale=(0.95, 0.8),
            color=rgb(117, 117, 117, 0),
            parent=camera.ui,
            *args,
            **kwargs
        )

        self.text = GameText(Game.language.login_not_available, position=(0, 0.28), origin=(0, 0), scale=(2.6, 3.2), parent=self)

        #self.username_box = InputField("Username", position=(0, 0.2), parent=self)
        #self.password_box = InputField("Password", position=(0, -0.1), hide_content=True, parent=self)
        #self.login_status = Text("", position=(0, 0.28), origin=(0, 0), scale=(3, 3.2), parent=self)
        #self.submit_button = GameButton("Submit", position=(0, -0.4), scale=(0.2, 0.15), parent=self)
        #self.submit_button.on_click = self.on_submit
