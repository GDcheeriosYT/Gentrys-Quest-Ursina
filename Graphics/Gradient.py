from ursina import *


class Gradient(Mesh):
    def __init__(self, color1=color.white, color2=color.black, direction='vertical', size=1, subdivisions=32):
        super().__init__()
        self.vertices = []
        self.colors = []
        self.triangles = []

        if direction == 'vertical':
            for i in range(subdivisions+1):
                x = -size/2
                y = lerp(-size/2, size/2, i/subdivisions)
                self.vertices += [(x, y, 0)]
                self.vertices += [(x+size, y, 0)]
                self.colors += [lerp(color1, color2, i/subdivisions)]
                self.colors += [lerp(color1, color2, i/subdivisions)]

        elif direction == 'horizontal':
            for i in range(subdivisions+1):
                x = lerp(-size/2, size/2, i/subdivisions)
                y = -size/2
                self.vertices += [(x, y, 0)]
                self.vertices += [(x, y+size, 0)]
                self.colors += [lerp(color1, color2, i/subdivisions)]
                self.colors += [lerp(color1, color2, i/subdivisions)]

        for i in range(subdivisions):
            self.triangles += [i*2, i*2+1, i*2+2]
            self.triangles += [i*2+2, i*2+1, i*2+3]

        self.colors *= 2
        self.colors = [color.rgba(*c) for c in self.colors]

        self.generate()

if __name__ == '__main__':
    app = Ursina()

    Gradient(color1=color.red, color2=color.blue, direction='horizontal', size=2)

    app.run()
