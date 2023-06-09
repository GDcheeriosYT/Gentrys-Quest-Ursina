from ursina import *
from Location.Map import Map
from Content.Enemies.AngryPedestrian.AngryPedestrian import AngryPedestrian
from Content.Enemies.AngryChineseMan.AngryChineseMan import AngryChineseMan
from Content.ArtifactFamilies.BraydenMesserschmidt.BraydenMesserschmidtFamily import BraydenMesserschmidtFamily
from Content.ArtifactFamilies.Jvee.Jvee import Jvee


grass = Entity(
    model='quad',
    position=(0, 0, 1),
    scale=(40, 40),
    color=color.green
)
grass.disable()


class TestMap(Map):
    def __init__(self):
        super().__init__(
            entities=[
                grass
            ],
            enemies=[
                AngryPedestrian,
                AngryChineseMan
            ],
            artifact_families=[
                BraydenMesserschmidtFamily(),
                Jvee()
            ]
        )
