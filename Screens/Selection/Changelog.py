from ursina import *

import Game
from Graphics.GameText import GameText


class ChangelogMenu(Entity):
    def __init__(self, parent):
        super().__init__(
            model=Quad(0.02),
            color=color.gray,
            parent=parent
        )

        self.heading_text = GameText(
            Game.language.get_localized_text(Game.language.changelog_title, Game.version),
            origin=(0, 0),
            scale=(self.parent.scale_x, self.parent.scale_x + 0.5),
            position=(0, 0.45),
            parent=self
        )

        self.changes = []
        position_y = 0.42
        wordwrap = 52
        for change_category in Game.changelog.categories:
            category_text = GameText(
                change_category.category_name,
                color=color.white,
                scale=(self.parent.scale_x * 1, self.parent.scale_x * 1.5),
                origin=(-0.5, 0.5),
                position=(-0.45, position_y),
                parent=self
            )
            self.changes.append(category_text)
            for change in change_category.changes:
                position_y -= 0.05 * self.parent.scale_x
                change_text = GameText(
                    change.get_string(),
                    color=color.black,
                    scale=(self.parent.scale_x, self.parent.scale_x + 0.5),
                    origin=(-0.5, 0.5),
                    position=(-0.45, position_y),
                    wordwrap=wordwrap,
                    parent=self
                )
                self.changes.append(change_text)
                position_y -= (0.05 * int(len(change.get_string())/wordwrap)) * self.parent.scale_x

            position_y -= 0.06 * self.parent.scale_x
