import unittest
from unittest.mock import patch
from visual import Point, Vector, distance, a, b, perm, milieu, average

class TestVisualLibrary(unittest.TestCase):

    def test_point_operations(self):
        p = Point(3, 4, 'A')
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)
        self.assertEqual(str(p), 'A')
        self.assertEqual(p, Point(3, 4))

    def test_vector_operations(self):
        v1 = Vector(x=3, y=4)
        v2 = Vector(x=1, y=2)
        self.assertEqual(v1 + v2, Vector(x=4, y=6))
        self.assertEqual(v1 - v2, Vector(x=2, y=2))
        self.assertEqual(v1 * 2, Vector(x=6, y=8))
        self.assertEqual(v1 / 2, Vector(x=1.5, y=2.0))

    def test_distance(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(distance(p1, p2), 5)

    def test_milieu(self):
        p1 = Point(0, 0)
        p2 = Point(2, 2)
        self.assertEqual(milieu(p1, p2), Point(1, 1))

    def test_average(self):
        self.assertEqual(average([1, 2, 3]), 2)

    def test_slope_and_intercept(self):
        p1 = Point(1, 2)
        p2 = Point(3, 6)
        self.assertEqual(a(p1, p2), 2)
        self.assertEqual(b(2, p1), 0)

    def test_perm(self):
        self.assertEqual(perm(5, 2), 20.0)

if __name__ == '__main__':
    unittest.main()