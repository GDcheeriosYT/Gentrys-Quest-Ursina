from ursina import *
import Game


class Ramen(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model='quad',
            texture='Textures/ramen.png',
            scale=(1, 1),
            collider='box',
            *args,
            **kwargs
        )

    def update(self):
        if self.intersects().hit:
            entity = self.intersects().entity
            if entity == Game.user.get_equipped_character():
                Game.user.user_data.items.append("Ramen")
                destroy(self)
