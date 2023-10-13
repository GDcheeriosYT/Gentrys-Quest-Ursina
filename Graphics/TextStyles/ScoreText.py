from ursina import *

import Game


class ScoreText(Text):
    def __init__(self):
        super().__init__(
            "0 Score",
            color=color.black,
            position=window.top,
            origin=(0, 0.5),
            scale=(1, 1),
            parent=camera.ui
        )
        self.score = 0
        Game.score_manager.on_score += self.transition_score

    def apply_text(self, amount):
        if (self.score + amount) < Game.score_manager.get_score():
            self.score += amount
            invoke(lambda: self.apply_text(amount), delay=time.dt)
        else:
            self.score = Game.score_manager.get_score()
            self.animate_scale((1, 1), 0.15)

        self.text = f"{int(round(self.score))} score"

    def transition_score(self):
        self.animate_scale((1.5, 1.5), 0.15)
        difference = Game.score_manager.get_score() - self.score
        fps = int(window.fps_counter.text)
        amount = difference / fps
        self.apply_text(amount)

    def on_destroy(self):
        Game.score_manager.on_score -= self.transition_score
