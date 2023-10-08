class Language:
    def __init__(self, name: str, **kwargs):
        self.name = name

        # langauge data
        self.play = "Play"
        self.back = "Back"
        self.done = "Done"
        self.next = "Next"
        self.confirm = "Confirm"
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
        self.inventory = "Inventory"
        self.characters = "Characters"
        self.character = "Character"
        self.artifacts = "Artifacts"
        self.weapons = "Weapons"
        self.weapon = "Weapon"
        self.changelog = "Changelog"
        self.travel = "Travel"
        self.gacha = "Gacha"
        self.equip = "Equip"
        self.upgrade = "Upgrade"
        self.upgrade_with_weapons = "Upgrade with weapons"
        self.not_number_error = "This isn't a number..."
        self.cant_afford = "Can't afford"

        for key, value in kwargs.items():
            setattr(self, key, value)
