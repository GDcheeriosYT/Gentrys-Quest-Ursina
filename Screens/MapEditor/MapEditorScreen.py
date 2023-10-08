from ..Screen import Screen

from .MapEditor import MapEditor
from .MapSelector import MapSelector
from .EditorStates import EditorStates


class MapEditorScreen(Screen):
    def __init__(self):
        super().__init__(allow_back=False)

        self.editor = MapEditor()
        self.map_selector = MapSelector()

    @property
    def name(self) -> str:
        return "Map Editor"

    @property
    def fades(self) -> bool:
        return False

    def switch_state(self):
        pass

    def update(self):
        if not self.editor.state_updated:
            if self.editor.state == EditorStates.MapSelection:
                self.map_selector.enable()

