import pytest
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square
from Circle import Circle


@pytest.fixture(scope='session')
def start_stop_service():
    print('\nstart service')
    yield
    print('\nstop service')


@pytest.fixture(autouse=True)
def cleanup():
    yield
    print('\nCleanup')


class TestFigure:

    @pytest.mark.parametrize(
        'a, b, c, instance', [(1, 2, 3, ValueError), (1, 2, 2, Triangle), (6, 2, 3, ValueError), (5, 2, 4, Triangle)]
    )
    def test_is_triangle(self, a, b, c, instance):
        triangle = Triangle.create_triangle(a, b, c)
        assert isinstance(triangle, instance)

    @pytest.mark.parametrize(
        'a, b, c, area', [(1, 2, 3, ValueError), (3, 4, 5, 6), (6, 2, 3, ValueError), (5, 2, 4, 3.8)]
    )
    def test_triangle_area(self, a, b, c, area):
        triangle = Triangle.create_triangle(a, b, c)
        try:
            assert triangle.area == area
        except AttributeError:
            assert isinstance(triangle, area)

    @pytest.mark.parametrize(
        'a, b, c, perimeter', [(1, 2, 3, ValueError), (3, 4, 5, 12), (6, 2, 3, ValueError), (5, 2, 4, 11)]
    )
    def test_triangle_perimeter(self, a, b, c, perimeter):
        triangle = Triangle.create_triangle(a, b, c)
        try:
            assert triangle.perimeter == perimeter
        except AttributeError:
            assert isinstance(triangle, perimeter)

    @pytest.mark.parametrize(
        'a, b, c, name', [(1, 2, 3, ValueError), (3, 4, 5, 'triangle')]
    )
    def test_triangle_perimeter(self, a, b, c, name):
        triangle = Triangle.create_triangle(a, b, c)
        try:
            assert triangle.name == name
        except AttributeError:
            assert isinstance(triangle, name)

    @pytest.mark.parametrize(
        'a, b, c, triangle_type', [(1, 2, 3, ValueError), (3, 4, 5, 'разносторонний'), (4, 4, 5, 'равнобедренный'),
                                   (5, 5, 5, 'равносторонний')]
    )
    def test_triangle_type(self, a, b, c, triangle_type):
        triangle = Triangle.create_triangle(a, b, c)
        try:
            assert triangle.triangle_type == triangle_type
        except AttributeError:
            assert isinstance(triangle, triangle_type)

    @pytest.mark.parametrize(
        'a, b, area', [(1, 2, 2), (0, 5, 0)]
    )
    def test_rectangle_area(self, a, b, area):
        rectangle = Rectangle(a, b)
        assert rectangle.area == area

    @pytest.mark.parametrize(
        'a, b, perimeter', [(1, 2, 6), (0, 5, 10)]
    )
    def test_rectangle_perimeter(self, a, b, perimeter):
        rectangle = Rectangle(a, b)
        assert rectangle.perimeter == perimeter

    @pytest.mark.parametrize(
        'a, b, name', [(1, 2, "rectangle"), (0, 5, "rectangle")]
    )
    def test_rectangle_name(self, a, b, name):
        rectangle = Rectangle(a, b)
        assert rectangle.name == name

    @pytest.mark.parametrize(
        'a, area', [(7, 153.94), (0, 0)]
    )
    def test_circle_area(self, a, area):
        circle = Circle(a)
        assert circle.area == area

    @pytest.mark.parametrize(
        'a, perimeter', [(10, 62.83), (0, 0)]
    )
    def test_circle_perimeter(self, a, perimeter):
        circle = Circle(a)
        assert circle.perimeter == perimeter

    @pytest.mark.parametrize(
        'a, diameter', [(10, 20), (0, 0)]
    )
    def test_circle_diameter(self, a, diameter):
        circle = Circle(a)
        assert circle.diameter == diameter

    @pytest.mark.parametrize(
        'a, name', [(10, "circle"), (0, "circle")]
    )
    def test_circle_name(self, a, name):
        circle = Circle(a)
        assert circle.name == name

    @pytest.mark.parametrize(
        'a, area', [(5, 25), (0, 0)]
    )
    def test_square_area(self, a, area):
        square = Square(a)
        assert square.area == area

    @pytest.mark.parametrize(
        'a, perimeter', [(7, 28), (0, 0)]
    )
    def test_rectangle_perimeter(self, a, perimeter):
        square = Square(a)
        assert square.perimeter == perimeter

    @pytest.mark.parametrize(
        'a, name', [(1, "square"), (0, "square")]
    )
    def test_rectangle_name(self, a, name):
        square = Square(a)
        assert square.name == name

    def test_add_area(self):
        triangle = Triangle.create_triangle(7, 7, 7)
        square = Square(5)
        circle = Circle(5)
        rectangle = Rectangle(7, 2)
        assert triangle.add_area(circle) == triangle.area + circle.area
        assert circle.add_area(square) == circle.area + square.area
        assert rectangle.add_area(triangle) == rectangle.area + triangle.area
        assert square.add_area(rectangle) == square.area + rectangle.area
        assert square.add_area('rectangle') == ValueError
        assert square.add_area(4) == ValueError




