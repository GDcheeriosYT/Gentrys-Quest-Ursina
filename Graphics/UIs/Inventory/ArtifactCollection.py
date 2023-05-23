from ursina import *
from .EntityIcon import EntityIcon
from .BlankArtifact import BlankArtifact
from .EntityChooseWindow import EntityChooseWindow


class ArtifactCollection(Entity):
    def __init__(self, character, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs
        )

        self.artifact_1 = self.create_artifact_entity(character, 1)
        self.artifact_2 = self.create_artifact_entity(character, 2)
        self.artifact_3 = self.create_artifact_entity(character, 3)
        self.artifact_4 = self.create_artifact_entity(character, 4)
        self.artifact_5 = self.create_artifact_entity(character, 5)

    def create_artifact_entity(self, character, number: int):
        if character.artifacts[number - 1]:
            icon = EntityIcon(
                character.artifacts[number - 1],
                position=(0, number*-0.12),
                parent=self
            )

            icon.scale = (0.10, 0.10)

            Text(
                character.artifacts[number - 1].experience,
                origin=(-0.5, 0),
                position=(0.8, 0),
                scale=(9, 9),
                parent=icon
            )
            return icon

        else:
            icon = BlankArtifact(
                position=(0, number * -0.12),
                scale=(0.15, 0.05),
                parent=self
            )

            return icon
