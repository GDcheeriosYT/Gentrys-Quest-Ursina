from ursina import *
from utils.StringMethods import *
from Graphics.TextStyles.StarRatingText import StarRatingText


class EntityIcon(Button):
    """
    EntityIcon acts as an icon for an entity.
    """
    def __init__(self, entity, scale: tuple = (0.15, 0.15), *args, **kwargs):
        """

        :param entity: The Entity to create an icon of.
        :param args: Entity arguments.
        :param kwargs: Entity keyword arguments.
        """
        super().__init__(
            scale=scale,
            color=color.clear if entity else rgb(64, 64, 64, 200),
            *args,
            **kwargs
        )

        self.highlight_color = rgb(100, 200, 100, 150)

        if entity:
            self._icon = Entity(
                model=Quad(0.1),
                texture=entity.texture,
                scale=(1, 1),
                parent=self
            )
            self._icon.z -= 1

            self.stars = StarRatingText(
                entity.star_rating,
                origin=(0, 0),
                position=(0, 0.45, -2),
                scale=(8, 9),
                parent=self
            )

            self._text = Text(
                entity.name,
                position=(0, -0.45, -2),
                scale=(5, 5),
                origin=(0, 0),
                color=color.black,
                parent=self
            )
        else:
            self._icon = Entity(
                model=Quad(0.1),
                color=color.clear,
                scale=(1, 1),
                parent=self
            )

            self.stars = StarRatingText(0)

            self._text = Text(
                "empty",
                position=(0, 0, -1),
                scale=(5, 5),
                origin=(0, 0),
                color=color.black,
                parent=self
            )


        self._text.create_background(color=color.white)
