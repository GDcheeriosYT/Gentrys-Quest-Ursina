import random


class ArtifactFamily:
    def __init__(self, artifacts: list):
        self.artifacts = artifacts

    @property
    def name(self) -> str:
        raise NotImplementedError

    def get_random_artifact(self):
        return random.choice(self.artifacts)
