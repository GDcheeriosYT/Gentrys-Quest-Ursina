from ursina import *


class Container(Entity):
    def __init__(self, parent=None, model="quad", color=color.clear, allow_highlighting: bool = True, *args, **kwargs):
        super().__init__(
            parent=camera.ui if not parent else parent,
            model=model,
            color=color,
            *args,
            **kwargs
        )

        self._allow_highlighting = allow_highlighting
        self.original_color = self.color
        self.highlighted = False

    def input(self, key):
        if key == "h":
            if self._allow_highlighting:
                if self.highlighted:
                    self.unhighlight()
                else:
                    self.highlight()

    def highlight(self):
        self.color = rgb(17, 17, 17, 125)
        self.highlighted = True

    def unhighlight(self):
        self.color = self.original_color
        self.highlighted = False
