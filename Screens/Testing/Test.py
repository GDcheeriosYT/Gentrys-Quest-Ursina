class Test:
    screen = None

    def __init__(self, class_type):
        self.name = class_type.__name__
        self.method_buttons = []

    def get_info(self):
        return {
            'name': self.name
        }

    def test_method(self):
        print("this is a test method")
