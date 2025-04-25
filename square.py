from shape import Shape
from loggable import Loggable


class Square(Shape, Loggable):
    def __init__(self, sides) -> None:
        super().__init__("square", sides)
    
    def is_valid(self) -> bool:
        """ Validate square via comparing sides """
        return len(self.sides) == 4 and len(set(self.sides)) == 1

    def area(self):
        """Calculate square area"""
        return self.sides[0] ** 2 if self.is_valid() else None

    def perimeter(self):
        """Calculate square perimeter"""
        return 4 * self.sides[0] if self.is_valid() else None

    