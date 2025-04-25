import math
from shape import Shape
from loggable import Loggable

class Triangle(Shape, Loggable):
    def __init__(self, sides):
        super().__init__("triangle", sides)
    
    def is_valid(self) -> bool:
        if len(self.sides) == 3:
            a, b, c = sorted(self.sides)
            return a + b > c
        return False

    def area(self):
        if self.is_valid():
            a, b, c = self.sides
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        return None

    def perimeter(self):
        return sum(self.sides) if self.is_valid() else None
