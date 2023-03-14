from Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.name = "rectangle"
        super().__init__(self.name)
        self._a = a
        self._b = b
        self._c = self._a
        self._d = self._b

    @property
    def area(self):
        return round(self._a * self._b)

    @property
    def perimeter(self):
        return round(2*(self._a + self._b))
