from ursina import *


class GPText(Text):
    def __init__(self, gp: int, ranking: str, *args, **kwargs):
        super().__init__(
            f"{gp} GP",
            *args,
            **kwargs
        )

        if ranking == 'copper':
            self.color = color.red
        elif ranking == 'bronze':
            self.color = color.brown
        elif ranking == 'silver':
            self.color = color.light_gray
        elif ranking == 'gold':
            self.color = color.gold
        elif ranking == 'platinum':
            self.color = color.blue
        elif ranking == 'diamond':
            self.color = color.cyan
        elif ranking == 'gentry warrior':
            self.color = color.lime
        else:
            self.color = color.white
