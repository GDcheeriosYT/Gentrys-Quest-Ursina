from ursina import *
import Game


class Register(Entity):
    def __init__(self, gas_station):
        super().__init__(
            model='quad',
            color=color.white,
            collider='box',
            position=(-0.3, -0.2, -1),
            scale=(0.06, 0.5),
            parent=gas_station
        )

    def update(self):
        if self.intersects().hit:
            entity = self.intersects().entity
            if entity == Game.user.get_equipped_character():
                if entity.user_data: # check for ramen
                    pass