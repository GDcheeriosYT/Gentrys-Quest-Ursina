from typing import Union


class Stat:
    def __init__(self, name: str, value: Union[int, float] = 1):
        self._name = name
        self._minimum_value = value
        self._default_value = 0
        self._additional_value = 0
        self.calculate_value()
        self.current_value = self._value
        self.points = 0

    def calculate_value(self):
        self._value = self._minimum_value + self._default_value + self._additional_value
        self.current_value = self._value

    @property
    def name(self) -> str:
        return self._name

    def get_value(self):
        return round(self._value, 2)

    def get_default_value(self):
        return round(self._default_value, 2)

    def get_additional_value(self):
        return round(self._additional_value, 2)

    def set_name(self, name):
        self._name = name

    def set_default_value(self, value):
        self._default_value = value
        self.calculate_value()

    def get_percent_of_stat(self, percent, include_additional: bool = True):
        if include_additional:
            return self.get_value() * (percent * 0.01)
        else:
            return self.get_default_value() * (percent * 0.01)

    def set_additional_value(self, value):
        self._additional_value = value
        self.calculate_value()

    def boost_stat(self, percentage):
        self._additional_value += self.get_default_value() + (self.get_default_value() * (percentage * 0.01))
        self.calculate_value()

    def add_value(self, amount):
        self._additional_value += amount
        self.calculate_value()

    def remove_value(self, amount):
        if self._additional_value - amount < 0:
            self._additional_value = 0
        else:
            self._additional_value -= amount

        self.calculate_value()

    def __repr__(self):
        if self._additional_value > 0:
            return f"{self._name}: {round(self._minimum_value + self._default_value, 2)} + {round(self._additional_value, 2)} ({self._value})"
        else:
            return f"{self._name}: {round(self._value, 2)}"
