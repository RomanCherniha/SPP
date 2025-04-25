from shape import Shape
from loggable import Loggable

class Rectangle(Shape, Loggable):
    def __init__(self, sides):
        super().__init__("rectangle", sides)

    def is_valid(self) -> bool:
        """ Validate recatngle via comparing sides """
        return len(self.sides) == 4 and self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]

    def area(self):
        """Calculate rectangle area"""
        return self.sides[0] * self.sides[1] if self.is_valid() else None

    def perimeter(self):
        """Calculate rectangle perimeter"""
        return 2 * (self.sides[0] + self.sides[1]) if self.is_valid() else None