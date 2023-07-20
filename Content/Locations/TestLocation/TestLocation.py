from Location.Location import Location
from ...Maps.TestMap import TestMap


class TestLocation(Location):
    def __init__(self):
        test_map_2 = TestMap()
        super().__init__(
            "Test Location",
            [
                TestMap()
            ]
        )
