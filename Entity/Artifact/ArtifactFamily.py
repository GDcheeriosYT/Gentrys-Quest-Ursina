import random

from .TwoPieceBuff import TwoPieceBuff
from .FourPieceBuff import FourPieceBuff


class ArtifactFamily:
    def __init__(self, artifacts: list, two_piece_buff: TwoPieceBuff = TwoPieceBuff(""), four_piece_buff: FourPieceBuff = FourPieceBuff("")):
        self.artifacts = artifacts
        self.two_piece_buff = two_piece_buff
        self.four_piece_buff = four_piece_buff

    @property
    def name(self) -> str:
        raise NotImplementedError

    def get_random_artifact(self):
        return random.choice(self.artifacts)
