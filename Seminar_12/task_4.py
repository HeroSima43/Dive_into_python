# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.

class Rectangle:

    def __init__(self, len_rec, width = None):
        self._len_rec = len_rec
        if width is None:
            self._width = len_rec
        else:
            self._width = width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self.width = value
        else:
            raise ValueError ('width должно быть > 0')

    def perimeter(self):
        return 2 * (self.len_rec + self.width)

    def square(self):
        return self.len_rec * self.width

    def __add__(self, other):
        return Rectangle(self.len_rec + other.len_rec, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.len_rec - other.len_rec), abs(self.width - other.width))

    def __eq__(self, other):
        return self.square() == other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __gt__(self, other):
        return self.square() > other.square()


s = Rectangle(4, -5)
print(s._width)
print(s.width)
s._width = -10
print(s._width)
s.width = -10
print(s.width)