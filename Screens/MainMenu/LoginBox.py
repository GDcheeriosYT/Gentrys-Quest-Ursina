from ursina import *
from ursina.prefabs.input_field import InputField
from User.User import User


class LoginBox(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model="quad",
            origin=(0, 0),
            scale=(0.95, 0.8),
            color=rgb(117, 117, 117, 0),
            parent=camera.ui,
            **kwargs
        )

        self.title = Text("Login", color=rgb(0, 0, 0), origin=(0, 0), scale=(4, 4.2), position=(0, 0.4), parent=self)
        self.username_box = InputField("Username", position=(0, 0.2), parent=self)
        self.password_box = InputField("Password", position=(0, -0.1), hide_content=True, parent=self)
        self.login_status = Text("", position=(0, 0.28), origin=(0, 0), scale=(3, 3.2), parent=self)
        self.submit_button = Button("Submit", position=(-0.25, -0.4), scale=(0.2, 0.15), parent=self)
        self.submit_button.on_click = self.on_submit
        self.guest_button = Button("Guest", position=(0.25, -0.4), scale=(0.2, 0.15), parent=self)
        self.guest_button.on_click = self.on_guest_submit

    def on_submit(self) -> None:
        user = User()
        username = self.username_box.text
        password = self.password_box.text


    def on_guest_submit(self) -> None:
        pass