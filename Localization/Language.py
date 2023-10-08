class Language:
    def __init__(self, name: str, **kwargs):
        self.name = name

        # langauge data
        self.play = None
        self.settings = None
        self.guest = None
        self.create_guest = None
        self.username = None
        self.login = None
        self.login_not_available = None
        self.audio = None
        self.graphics = None
        self.music = None
        self.sound = None
        self.volume = None
        self.fullscreen = None
        self.extra_ui_info = None
        self.apply = None

        for key, value in kwargs.items():
            setattr(self, key, value)
