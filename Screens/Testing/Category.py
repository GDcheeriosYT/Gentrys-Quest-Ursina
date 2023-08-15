class Category:
    def __init__(self, name: str, tests: list):
        self.name = name
        self.tests = tests
        self.selected_test = tests[0] if len(tests) > 0 else None

    def select_test(self, index: int):
        self.selected_test = self.tests[index]
        self.selected_test.load
