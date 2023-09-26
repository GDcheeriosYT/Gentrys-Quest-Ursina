from  .EditorStates import EditorStates


class MapEditor:
    def __init__(self):
        self.map_name = None
        self.objects = []
        self.state = EditorStates.MapSelection
        self.state_updated = False
