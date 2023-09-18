from ursina import *
from utils.StringMethods import *


class StarRatingText(Text):
    def __init__(self, star_rating, *args, **kwargs):
        text_color = color.white
        if star_rating == 1:
            star_rating = 0
        if star_rating == 2:
            text_color = color.green
        if star_rating == 3:
            text_color = color.cyan
        if star_rating == 4:
            text_color = color.pink
        if star_rating == 5:
            text_color = color.gold

        super().__init__(
            repeat_string("*", star_rating),
            color=text_color,
            *args,
            **kwargs
        )
