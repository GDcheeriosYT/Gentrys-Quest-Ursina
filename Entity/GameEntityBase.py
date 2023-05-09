from ursina import *

from Overlays.NoficationsManager import NotificationManager
from Overlays.Notification import Notification
from .Experience import Experience
from .TextureMapping import TextureMapping
from utils.Event import Event


class GameEntityBase(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model="quad",
            texture="huh.png",
            *args,
            **kwargs
        )
        self._experience = Experience()
        self.on_level_up = Event("OnLevelUp", 0)
        self.on_add_xp = Event("OnAddXp", 0)
        self.disable()

    @property
    def name(self) -> str:
        """
        The name of the GameEntity
        """
        raise NotImplementedError

    @property
    def experience(self) -> Experience:
        """
        The experience of the GameEntity
        """
        return self._experience

    def add_xp(self, amount):
        self.experience.xp += amount
        while self.experience.xp >= self.experience.get_xp_required(self.star_rating):
            self.level_up()
            self.experience.xp -= self.experience.get_xp_required(self.star_rating)

        self.on_add_xp()

    def level_up(self):
        self.experience.level += 1
        notification = Notification(f"{self.name} is now level {self.experience.level}", color.blue)
        NotificationManager.add_nofication(notification)
        self.on_level_up()

    def update_stats(self):
        pass

    @staticmethod
    def check_minimum(variable, multiplier=1, subtract_one_true=False):
        if variable < 1:
            return 1 if not subtract_one_true else 0
        else:
            return variable * multiplier
