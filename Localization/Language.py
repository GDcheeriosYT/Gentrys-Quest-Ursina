class Language:
    def __init__(self, name: str, **kwargs):
        self.name = name

        # langauge data
        self.play = "Play"
        self.back = "Back"
        self.settings = "Settings"
        self.guest = "Guest"
        self.username = "username"
        self.create_guest = "Create Guest"
        self.login = "Login"
        self.login_not_available = "Login not available yet..."
        self.audio = "Audio"
        self.graphics = "Graphics"
        self.music = "Music"
        self.music_volume = "Music Volume"
        self.sound = "Sound"
        self.sound_volume = "Sound Volume"
        self.volume = "Volume"
        self.fullscreen = "Fullscreen"
        self.extra_ui_info = "Extra UI Info"
        self.apply = "Apply"
        self.applied_settings = "Applied Settings"

        for key, value in kwargs.items():
            setattr(self, key, value)
