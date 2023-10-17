from ursina import *

import Game

from Entity.EntityPool import EntityPool


class ScoreText(Text):
    def __init__(self, **kwargs):
        super().__init__(
            "0 Score",
            color=color.black,
            **kwargs
        )
        self.score = 0
        Game.score_manager.on_score += self.transition_score

    def apply_text(self, amount):
        if (self.score + amount) < Game.score_manager.get_score():
            self.score += amount
            invoke(lambda: self.apply_text(amount), delay=time.dt)
            self.text = f"{int(round(self.score))} score"
        else:
            self.score = Game.score_manager.get_score()
            self.animate_scale((2, 2), 0.25)
            self.animate_color(color.black, 0.25)

            self.text = f"{int(round(self.score))} score\n"

    def transition_score(self):
        self.animate_scale((3.5, 3.5), 0.25)
        difference = Game.score_manager.get_score() - self.score
        self.animate_color(color.light_gray, 0.25)
        fps = int(window.fps_counter.text)
        amount = difference / fps
        self.apply_text(amount)

    def on_destroy(self):
        Game.score_manager.on_score -= self.transition_score
