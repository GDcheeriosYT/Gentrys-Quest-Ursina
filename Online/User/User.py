from .UserData import UserData


class User:

    @property
    def username(self) -> str:
        return "Username"

    @property
    def user_data(self) -> None:
        return None

    @username.setter
    def username(self, value) -> str:
        self.username = value

    def login(self) -> None:
