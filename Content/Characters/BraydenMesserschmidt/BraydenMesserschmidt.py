from Entity.Character.Character import Character
from Entity.TextureMapping import TextureMapping
from Entity.AudioMapping import AudioMapping
from .Skills.CircleThrow import CircleThrow
from .Skills.Dash import Dash
from ursina import *
import Game
from Overlays.Notification import Notification


class BraydenMesserschmidt(Character):
    def __init__(self):
        super().__init__(
            TextureMapping(
                idle_textures=["Content/Characters/BraydenMesserschmidt/Textures/body.png"]
            ),
            AudioMapping(
                spawn_sounds=["Audio/spawn.mp3"],
                damage_sounds=["Audio/damage.mp3"]
            )
        )
        # stats
        self._stats.speed.points = 1
        self._stats.crit_rate.points = 2
        self._stats.attack_speed.points = 1

        # skills
        self.secondary = CircleThrow()
        self.utility = Dash()
        self.ultimate = CircleThrow()

        # spawn event
        self.on_update_stats += self.check_weapon

    @property
    def name(self) -> str:
        return "Brayden Messerschmidt"

    @property
    def description(self) -> str:
        return "An osu player who formed a contract with ppy(Dean Herbert) to not talk to females."

    @property
    def star_rating(self) -> int:
        return 5

    def check_weapon(self):
        if self.weapon:
            print(self.weapon.name)
            if self.weapon.name == "Braydens Osu Pen":
                Game.notification_manager.add_notification(Notification("Brayden Messerschmidt Weapon Bonus", color=color.gold))
                self.stats.boost_all_stats(10)
