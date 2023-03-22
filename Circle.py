from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, r):
        self.name = "circle"
        self._r = r

    @property
    def area(self):
        return round(math.pi * math.pow(self._r, 2), 2)

    @property
    def perimeter(self):
        return round(2 * math.pi * self._r, 2)

    @property
    def diameter(self):
        return 2 * self._r
