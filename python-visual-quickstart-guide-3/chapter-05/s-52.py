import unittest
import math


def area(radius):
    """Returns the area of a circle with the given radius.
    for example:
    >>> area(5.5)
    95.033177771091246
    """
    return math.pi * radius ** 2


class S52Test(unittest.TestCase):
    def test_area_1(self):
        s1 = area(1)
        self.assertGreater(s1, 3)

    def test_area_5_5(self):
        s2 = area(5.5)
        self.assertGreater(s2, 95)


if __name__ == '__main__':
    unittest.main()
