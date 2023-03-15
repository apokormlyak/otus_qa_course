from Rectangle import Rectangle
import math


class Square(Rectangle):
    def __init__(self, a):
        self.name = "square"
        self._a = a

    @property
    def area(self):
        return math.pow(self._a, 2)

    @property
    def perimeter(self):
        return 4 * self._a
