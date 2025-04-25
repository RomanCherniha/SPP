from abc import ABC, abstractmethod

class Shape(ABC):
    """Base class for shapes."""
    
    def __init__(self, shape, sides):
        self.shape = shape
        self.sides = sides

    def log(self):
        from logger import Logger  
        Logger.log_shape(self)  

    @abstractmethod
    def is_valid(self):
        raise NotImplementedError("ggg")
    
    @abstractmethod
    def area(self):
        raise NotImplementedError("ggg")
    
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("ggg")
    

class SolidShape(Shape):
    """Base class for solid shapes (3D)."""
    
    def __init__(self, shape, sides, depth):
        super().__init__(shape, sides)
        self.depth = depth  

    def volume(self):
        """Volume should be implemented in subclasses"""
        raise NotImplementedError("Subclasses must implement volume method")
