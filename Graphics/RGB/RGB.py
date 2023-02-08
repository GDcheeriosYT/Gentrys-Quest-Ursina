from .ColorChannel import ColorChannel

class RGB:
    def __init__(self, R: ColorChannel = 0, G: ColorChannel = 0, B: ColorChannel = 0):
        self.R = R
        self.G = G
        self.B = B

    def __repr__(self):
        return self.R, self.G, self.B