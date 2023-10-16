import Game
from ..Screen import Screen

from .MapEditor import MapEditor
from .MapSelector import MapSelector
from .EditorStates import EditorStates
from .MapMetadata import MapMetadata


class MapEditorScreen(Screen):
    def __init__(self):
        super().__init__(allow_back=False)

        self.editor = MapEditor()
        self.map_selector = MapSelector(self)
        self.map_metadata = MapMetadata()

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
            if self.editor.state == EditorStates.MapMetadata:
                self.map_metadata.enable()
                self.map_metadata.load(Game.content_manager.)
