from typing import Optional

from Figure import Figure
import math
import logging


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.name = "triangle"
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def create_triangle(a, b, c) -> Optional["Triangle"]:
        try:
            if a < b + c and b < a + c and c < a + b:
                return Triangle(a, b, c)
            else:
                raise ValueError
        except ValueError as e:
            logging.error(e)
            return ValueError()

    @property
    def area(self):
        p = self.perimeter/2
        area = math.sqrt(p*(p-self._a)*(p-self._b)*(p-self._c))
        return round(area, 2)

    @property
    def perimeter(self):
        perimeter = self._a + self._b + self._c
        return perimeter

    @property
    def triangle_type(self):
        if self._a == self._b and self._a == self._c and self._c == self._b:
            return 'равносторонний'
        elif self._a == self._b and self._a != self._c or self._a == self._c and self._a != self._b or self._b == \
                self._c and self._a != self._b:
            return 'равнобедренный'
        else:
            return 'разносторонний'

