from ursina import *
from Location.Map import Map
from Content.Enemies.AngryPedestrian.AngryPedestrian import AngryPedestrian
from Content.Enemies.AngryChineseMan.AngryChineseMan import AngryChineseMan
from Content.ArtifactFamilies.BraydenMesserschmidt.BraydenMesserschmidtFamily import BraydenMesserschmidtFamily
from Content.ArtifactFamilies.HyVee.HyVee import HyVee


grass = Entity(
    model='quad',
    position=(0, 0, 1),
    scale=(40, 40),
    color=rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    enabled=False
)

collision_entity = Entity(
    model='quad',
    color=color.black,
    collider='box',
    position=(0, 0, 0),
    enabled=False
)

collision_entities = [duplicate(collision_entity, position=(random.randint(-40, 40), random.randint(-40, 40)), scale=(random.randint(-10, 10), random.randint(-10, 10))) for i in range(20)]

entities = [
    grass
]

[entities.append(new_entity) for new_entity in collision_entities]

class TestMap(Map):
    def __init__(self):
        super().__init__(
            entities=entities,
            enemies=[
                AngryPedestrian,
                AngryChineseMan
            ],
            artifact_families=[
                BraydenMesserschmidtFamily(),
                HyVee()
            ]
        )
