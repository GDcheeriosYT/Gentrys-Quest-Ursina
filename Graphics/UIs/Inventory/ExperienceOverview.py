from ursina import *


class ExperienceOverview(Text):
    def __init__(self, entity, *args, **kwargs):
        super().__init__(
            text=f"level {entity.experience.level}{f'/{entity.experience.limit}' if entity.experience.limit else ''} {int(entity.experience.xp)}/{entity.experience.get_xp_required(entity.star_rating)}xp",
            origin=(0.5, 0),
            position=(-0.6, 0.5),
            scale=(4, 4),
            *args,
            **kwargs
        )
