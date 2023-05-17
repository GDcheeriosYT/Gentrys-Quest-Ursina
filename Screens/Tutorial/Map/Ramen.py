from ursina import *
import Game


class Ramen(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(
            model='quad',
            texture='Textures/ramen.png',
            scale=(1, 1),
            collider='Box',
            *args,
            **kwargs
        )

    def update(self):
        if self.intersects(Game.user.get_equipped_character()).hit:
            destroy(self)
