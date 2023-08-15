class Test:
    def __init__(self, class_type):
        self.name = class_type.__name__

    def load(self):
        pass

    def test_method(self):
        print("this is a test method")
