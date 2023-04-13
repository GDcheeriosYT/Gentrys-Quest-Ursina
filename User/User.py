from .UserData import UserData


class User:
    def __init__(self, username: str):
        self._username = username
        self._user_data = UserData()

    @property
    def username(self) -> str:
        return self._username

    @property
    def user_data(self) -> None:
        return None

    def login(self, is_guest: bool, username: str = None, password: str = None) -> None:
        if is_guest:
            pass

        pass

