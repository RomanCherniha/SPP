from shape import SolidShape
from loggable import Loggable

class Cube(SolidShape, Loggable):
    def __init__(self, sides) -> None:
        if len(sides) != 6 or len(set(sides)) != 1:
            raise ValueError("Cube requires six identical side lengths.")
        super().__init__("cube", sides, sides[0])
    
    def is_valid(self) -> bool:
        """Validate if cube has correct dimensions"""
        return len(self.sides) == 6 and len(set(self.sides)) == 1 and self.sides[0] > 0

    def area(self):
        """Calculate surface area of the cube"""
        return 6 * (self.sides[0] ** 2) if self.is_valid() else None

    def perimeter(self):
        """Calculate the perimeter of one face of the cube"""
        return 4 * self.sides[0] if self.is_valid() else None

    def volume(self):
        """Calculate the volume of the cube"""
        return self.sides[0] ** 3 if self.is_valid() else None
