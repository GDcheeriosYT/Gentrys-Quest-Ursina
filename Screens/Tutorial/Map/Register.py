from ursina import *
import Game
import GameConfiguration
from Graphics.Containers.TextContainer import TextContainer


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

        self.bought = False

    def buy_sequence(self, entity):
        if entity == Game.user.get_equipped_character():
            text_container = TextContainer()
            if "Ramen" in Game.user.user_data.items:
                Game.user.user_data.items.remove("Ramen")
                text_container.set_text("Thanks for coming by have a good night!", 3)
                Audio("Audio/buy.mp3", volume=GameConfiguration.volume)
                destroy(text_container, 4)
                self.bought = True

            else:
                text_container.set_text("Do you need something sir?", 3)
                destroy(text_container, 0.1)


    def update(self):
        if self.intersects().hit and not self.bought:
            entity = self.intersects().entity
            self.buy_sequence(entity)
