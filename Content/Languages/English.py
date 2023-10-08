from Localization.Language import Language


class English(Language):
    def __init__(self):
        super().__init__(
            "English",
            play="Play",
            back="Back",
            settings="Settings",
            guest="Guest",
            username="username",
            create_guest="Create Guest",
            login="Login",
            login_not_available="Login not available yet...",
            audio="Audio",
            graphics="Graphics",
            music="Music",
            music_volume="Music Volume",
            sound="Sound",
            sound_volume="Sound Volume",
            volume="Volume",
            fullscreen="Fullscreen",
            extra_ui_info="Extra UI Info",
            apply="Apply",
            applied_settings="Applied Settings"
        )
