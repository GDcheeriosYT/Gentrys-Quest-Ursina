from enum import Enum
import os

cwd = os.getcwd()

class FontStyles(Enum):
    MainFont = 1
    InfoFont = 2

    def get_font_path(self):
        if self == FontStyles.MainFont:
            return f"{cwd}/Content/Fonts/main_font.ttf"

        elif self == FontStyles.InfoFont:
            return f"{cwd}/Content/Fonts/info_font.ttf"
