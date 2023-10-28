class Rectangle:
    def __init__(self, len_rec, width = None):
        self.len_rec = len_rec
        if width is None:
            self.width = len_rec
        else:
            self.width = width            

    def perimeter(self):
        return 2 * (self.len_rec + self.width)

    def area(self):
        return self.len_rec * self.width
    
    def __add__(self, other):
        return Rectangle(self.len_rec + other.len_rec, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.len_rec - other.len_rec), abs(self.width - other.width))
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __le__(self, other):
        return self.area() <= other.area()
    
    def __ne__(self, other):
        return self.area() != other.area()
    
    def __ge__(self, other):
        return self.area() >= other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self.len_rec} и {self.width}'
    
    def __repr__(self) -> str:
        return f'Rectangle({self.len_rec}, {self.width})'
    
