from ursina import *

class GPText(Text):
    def __init__(self, gp: int, ranking: tuple, *args, **kwargs):
        rank_text = ranking[1]
        super().__init__(
            f"{gp} GP {rank_text}",
            *args,
            **kwargs
        )

        if ranking[0] == 'copper':
            self.color = color.red
        elif ranking[0] == 'bronze':
            self.color = color.brown
        elif ranking[0] == 'silver':
            self.color = color.light_gray
        elif ranking[0] == 'gold':
            self.color = color.gold
        elif ranking[0] == 'platinum':
            self.color = color.blue
        elif ranking[0] == 'diamond':
            self.color = color.cyan
        elif ranking[0] == 'gentry warrior':
            self.color = color.lime
        else:
            self.color = color.white
