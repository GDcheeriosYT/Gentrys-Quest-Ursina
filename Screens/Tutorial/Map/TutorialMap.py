from ursina import *
import Game
from .GasStation import GasStation
from .ParkingLot import ParkingLot
from Content.Enemies.AngryPedestrian.AngryPedestrian import AngryPedestrian


class TutorialMap(Entity):
    def __init__(self):
        super().__init__(
            # model='quad',
            # color=color.clear,
            # collider='box',
            # scale=(20, 60),
            # parent=self
        )
        self.angry_pedestrian = AngryPedestrian()
        self.angry_pedestrian.disable()
        self.angry_pedestrian.position = (0, 0 , -1)
        self.angry_pedestrian.can_move = False
        self.angry_pedestrian.follow_entity(Game.user.get_equipped_character())
        self.gas_station = GasStation()
        self.parking_lot = ParkingLot()
        self.enemy_cutscene_intro = False
        self.character_copy = Entity(
            model="quad",
            texture=Game.user.get_equipped_character().texture,
        )
        self.character_copy.disable()

        Game.user.get_equipped_character().on_death += self.death_transition

    def death_transition(self):
        invoke(self.gas_station.disable, delay=4)
        invoke(self.parking_lot.disable, delay=4)
        destroy(self.angry_pedestrian, 4)

    def update(self):
        if not self.enemy_cutscene_intro:
            if self.parking_lot.cutscene_toggler.intersects().entity == Game.user.get_equipped_character():
                self.enemy_cutscene_intro = True
                Game.user.get_equipped_character().disable()
                self.character_copy.position = Game.user.get_equipped_character().position
                self.character_copy.animate_position(self.character_copy.position + (0, -1, 0), 0.2, curve=curve.linear)
                Game.user.get_equipped_character().animate_position(self.character_copy.position + (0, -1, 0), 0.2, curve=curve.linear)
                self.character_copy.enable()
                self.angry_pedestrian.experience.level = 10
                self.angry_pedestrian.update_stats()
                self.angry_pedestrian.stats.boost_all_stats(200)
                self.angry_pedestrian.position = (self.character_copy.x + 10, self.character_copy.y - 1, self.character_copy.z)
                invoke(lambda: camera.animate_position((10, camera.y, -20), 2.5, curve=curve.linear), delay=1)
                invoke(self.angry_pedestrian.spawn, delay=4)
                invoke(self.angry_pedestrian.toggle_movement, delay=5)
                invoke(self.character_copy.disable, delay=5)
                invoke(Game.user.get_equipped_character().enable, delay=5)
                invoke(Game.user.get_equipped_character().toggle_movement, delay=5)
