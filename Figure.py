from abc import abstractmethod
import logging


class Figure:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def add_area(self, figure) -> float:
        try:
            if isinstance(figure, Figure):
                return self.area + figure.area
            else:
                raise ValueError
        except ValueError as e:
            logging.error(e)
            return ValueError
