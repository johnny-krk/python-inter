"""
* Assignment: DevOps Unittest Rectangle
* Complexity: medium
* Lines of code: 100 lines
* Time: 21 min

English:
    1. Write unittest for `Rectangle`
    2. Run unittest - all must succeed

Polish:
    1. Napisz testy jednostkowe dla `Rectangle`
    2. Uruchom unittest - wszystkie muszą się powieść
"""

import unittest


class Rectangle:

    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

        if a <= 0 or b <= 0:
            raise ValueError('Side length must be positive')

    def area(self) -> int:
        return self.side_a * self.side_b

    def circumference(self) -> int:
        return (self.side_a + self.side_b) * 2

    def __str__(self):
        return f'Rectangle({self.side_a}, {self.side_b})'


# Solution
class TestRectangle(unittest.TestCase):
    def test_creation(self):
        self.assertRaises(ValueError, Rectangle, -1, 0)
        self.assertRaises(ValueError, Rectangle, 0, -1)
        self.assertRaises(ValueError, Rectangle, 1, -1)

    def test_area(self):
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)

    def test_circumference(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.circumference(), 6)

    def test_str(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.__str__(), 'Rectangle(2, 3)')
