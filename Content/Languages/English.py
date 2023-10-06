from Localization.Language import Language


class English(Language):
    def __init__(self):
        super().__init__(
            "English",
            play="Play",
            settings="Settings",
            guest="Guest",
            username="username",
            create_guest="Create Guest",
            login="Login",
            login_not_available="Login not available yet..."
        )
