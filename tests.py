import unittest
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from loggable import Loggable

class TestTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        t = Triangle([3, 4, 5])
        self.assertTrue(t.is_valid())
        self.assertEqual(t.area(), 6.0)
        self.assertEqual(t.perimeter(), 12)
    
    def test_invalid_triangle(self):
        t = Triangle([1, 2, 3])
        self.assertFalse(t.is_valid())
        self.assertIsNone(t.area())
        self.assertIsNone(t.perimeter())

class TestRectangle(unittest.TestCase):
    def test_valid_rectangle(self):
        r = Rectangle([4, 6, 4, 6])
        self.assertTrue(r.is_valid())
        self.assertEqual(r.area(), 24)
        self.assertEqual(r.perimeter(), 20)
    
    def test_invalid_rectangle(self):
        r = Rectangle([4, 6, 5, 6])
        self.assertFalse(r.is_valid())
        self.assertIsNone(r.area())
        self.assertIsNone(r.perimeter())

class TestSquare(unittest.TestCase):
    def test_valid_square(self):
        s = Square([5, 5, 5, 5])
        self.assertTrue(s.is_valid())
        self.assertEqual(s.area(), 25)
        self.assertEqual(s.perimeter(), 20)
    
    def test_invalid_square(self):
        s = Square([5, 5, 4, 5])
        self.assertFalse(s.is_valid())
        self.assertIsNone(s.area())
        self.assertIsNone(s.perimeter())

class TestLoggable(unittest.TestCase):
    def test_loggable_implementation(self):
        t = Triangle([3, 4, 5])
        self.assertIsInstance(t, Loggable)
        
        s = Square([5, 5, 5, 5])
        self.assertIsInstance(s, Loggable)
    
    def test_logging_output(self):
        t = Triangle([3, 4, 5])
        with self.assertLogs() as captured:
            t.log()
        self.assertTrue(any("triangle" in log for log in captured.output))

if __name__ == '__main__':
    unittest.main()
