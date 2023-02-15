# game packages
# graphics packages
from ..Text import Text, FontStyles


class InfoText(Text):
    def __init__(self, text: str, position: tuple, font_size: int = 12, color: tuple = (0, 0, 0)):
        super().__init__(
            text,
            position,
            font_size,
            color,
            FontStyles.InfoFont
        )