from Figure import Figure
import math


class Square(Figure):
    def __init__(self, a):
        self.name = "square"
        super().__init__(self.name)
        self._a = a
        self._b = self._c = self._d = self._a

    @property
    def area(self):
        return math.pow(self._a, 2)

    @property
    def perimeter(self):
        return 4 * self._a
