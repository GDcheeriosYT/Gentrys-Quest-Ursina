class ColorChannel:
    def __init__(self, number: int):
        if number < 0:
            self.number = 0
        elif number > 255:
            self.number = 255
        else:
            self.number = number

    def __repr__(self):
        return self.number