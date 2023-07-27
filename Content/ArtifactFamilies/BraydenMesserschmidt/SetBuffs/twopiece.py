from Entity.Artifact.TwoPieceBuff import TwoPieceBuff


class TwoPiece(TwoPieceBuff):
    def __init__(self):
        super().__init__(
            "increases crit damage by 20%"
        )

    def apply_buff(self, character):
        print("I was called")
        character.stats.crit_damage.add_value(20)
