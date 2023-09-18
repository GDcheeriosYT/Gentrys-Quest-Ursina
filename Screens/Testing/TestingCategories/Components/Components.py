from ...Category import Category

from .DirectionalContainerTest import DirectionalContainerTest


class Components(Category):
    def __init__(self):
        super().__init__(
            "Components",
            [
                DirectionalContainerTest()
            ]
        )
