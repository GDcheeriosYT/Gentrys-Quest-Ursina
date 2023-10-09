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
        self.confirm_guest = "Would you like to play as ::player_name::?"
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
        self.changelog = "Changelog",
        self.changelog_title = f"Changelog for ::version::"
        self.travel = "Travel"
        self.gacha = "Gacha"
        self.equip = "Equip"
        self.upgrade = "Upgrade"
        self.upgrade_with_weapons = "Upgrade with weapons"
        self.not_number_error = "This isn't a number..."
        self.cant_afford = "Can't afford..."
        self.amount = "Amount"
        self.pull_character = "Pull Character"
        self.pull_weapon = "Pull Weapon"
        self.character_amount = "::amount:: Characters"
        self.weapon_amount = "::amount:: Weapons"
        self.empty = "Empty",
        self.damage = "Damage: ::Damage::"
        self.buff = "Buff: ::buff::"
        self.attack_speed = "attack_speed: ::attack_speed::"
        self.range = "range: ::Damage::"
        self.seconds = "seconds"
        self.health = "Health: ::health::"
        self.attack = "Attack: ::attack::"
        self.defense = "Defense: ::defense::"
        self.critrate = "CritRate: ::critrate::"
        self.critdamage = "CritDamage: ::critdamage::"
        self.speed = "Speed: ::speed::"


        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def get_localized_text(text: str, *args) -> str:
        if "::" in text:
            text = text.split("::")
            arg_counter = 0
            for text_part in text:
                index = text.index(text_part)
                if index % 2 != 0:
                    text[index] = str(args[arg_counter])
                    arg_counter += 1

            return ''.join(text)

        else:
            return text
