import math
import unittest

from squares import Triangle, Circle
from squares.errors import InvalidArgumentsError


class TestTriangle(unittest.TestCase):
    def test_can_create_triangle(self):
        cases = [
            (2, 5, 4),
            (7, 6, 8),
            (60000, 30000, 50000),
        ]
        for sides in cases:
            t = Triangle(*sides)
            self.assertEqual(t.a, sides[0])
            self.assertEqual(t.b, sides[1])
            self.assertEqual(t.c, sides[2])

    def test_raises_if_sides_are_invalid(self):
        cases = [
            [(0, 0, 0), InvalidArgumentsError],
            [(1, 2, 0), InvalidArgumentsError],
            [(1, 0, 2), InvalidArgumentsError],
            [(0, 1, 2), InvalidArgumentsError],
            [(-1, 1, 2), InvalidArgumentsError],
            [(1, -1, 2), InvalidArgumentsError],
            [(1, 1, -1), InvalidArgumentsError],
            [(1, 3, 4), InvalidArgumentsError],
        ]
        for case in cases:
            sides, error = case
            self.assertRaises(error, Triangle, *sides)

    def test_can_calculate_square_with_correct_sides(self):
        cases = [
            [(2.0, 5.0, 4.0), 3.7996710],
            [(7.0, 6.0, 8.0), 20.333163],
            [(60000.0, 30000.0, 50000.0), 748331477.3547883],
        ]

        for case in cases:
            sides, square = case
            t = Triangle(*sides)
            repr_str = f"Triangle(a={sides[0]}, b={sides[1]}, c={sides[2]})"
            self.assertEqual(repr(t), repr_str)
            self.assertEqual(t.a, sides[0])
            self.assertEqual(t.b, sides[1])
            self.assertEqual(t.c, sides[2])
            self.assertAlmostEqual(t.square(), square, 6)

    def test_can_check_if_triangle_is_right(self):
        cases = [
            ([1, 2, 2], 7, False),
            ([3, 4, 5], 7, True),
            ([4, 3, 5], 7, True),
            ([5, 3, 4], 7, True),
        ]

        for case in cases:
            sides, places, ok = case
            t = Triangle(*sides)
            self.assertEqual(t.is_right(places), ok)

    def test_with_sides_updates_triangle(self):
        cases = [
            [(2, 5, 4), (3, None, None), (3, 5, 4), None],
            [(2, 5, 4), (1, None, None), (), InvalidArgumentsError],
        ]
        for case in cases:
            sides, patches, result, error = case
            base = Triangle(*sides)
            if error is not None:
                self.assertRaises(InvalidArgumentsError, base.with_sides, *patches)
                return

            patched = base.with_sides(*patches)
            self.assertEqual(patched.a, float(result[0]))
            self.assertEqual(patched.b, float(result[1]))
            self.assertEqual(patched.c, float(result[2]))


class TestCircle(unittest.TestCase):
    def test_can_create_circle(self):
        cases = [1.0, 3.0, 4.0, 10000.0]

        for radius in cases:
            circle = Circle(radius)
            self.assertEqual(repr(circle), f"Circle(radius={radius})")
            self.assertEqual(circle.radius, radius)

    def test_raises_if_radius_is_invalid(self):
        cases = [0, -1, -1000]

        for radius in cases:
            self.assertRaises(InvalidArgumentsError, Circle, radius)

    def test_can_calculate_square(self):
        cases = [
            [1, math.pi],
            [3, 9 * math.pi],
            [4, 16 * math.pi],
            [10000, 100_000_000 * math.pi],
        ]

        for case in cases:
            radius, square = case
            circle = Circle(radius)
            self.assertAlmostEqual(circle.square(), square, 7)
