import unittest

from geom_tools.utils import is_arrays_equal
import numpy as np
from geom_tools.bounding_box import BoundingBox, from_vertices


class TestMesh(unittest.TestCase):
    def test_from_eq01(self):
        b1 = BoundingBox([0, 0, 0], [1, 1, 1])
        b2 = BoundingBox([0, 0, 0], [1, 1, 1])
        self.assertEqual(b1, b2)

    def test_from_eq02(self):
        b1 = BoundingBox([1, 5, -5], [6, 13, -4])
        b2 = BoundingBox([1, 5, -5], [6, 13, -4])
        self.assertEqual(b1, b2)

    def test_from_eq03(self):
        b1 = BoundingBox([1, 5, -5], [6, 13, -4])
        b2 = BoundingBox([0, 5, -5], [6, 13, -4])
        self.assertNotEqual(b1, b2)

    def test_from_eq04(self):
        b1 = BoundingBox([1, 5, -5], [6, 13, -4])
        b2 = BoundingBox([1, 5, -5], [6, 103, -4])
        self.assertNotEqual(b1, b2)

    def test_from_vertices01(self):
        vertices = [
            [0, 0, 0],
            [1, 1, 1],
        ]
        res = from_vertices(vertices)
        self.assertEqual(BoundingBox([0, 0, 0], [1, 1, 1]), res)

    def test_from_vertices02(self):
        vertices = [
            [6, 0, 0],
            [1, 1, 1],
        ]
        res = from_vertices(vertices)
        self.assertEqual(BoundingBox([1, 0, 0], [6, 1, 1]), res)

    def test_from_vertices03(self):
        vertices = [
            [1, 0, 1],
            [6, -2, 13],
        ]
        res = from_vertices(vertices)
        self.assertEqual(BoundingBox([1, -2, 1], [6, 0, 13]), res)

    def test_from_vertices04(self):
        vertices = [
            [1, 2, 3],
            [-2, 6, 8],
            [0, 0, 11],
        ]
        res = from_vertices(vertices)
        self.assertEqual(BoundingBox([-2, 0, 3], [1, 6, 11]), res)

    def test_from_vertices05(self):
        vertices = [
            [1, 1, 1],
            [5, 5, 5],
            [3, 3, 3]
        ]
        res = from_vertices(vertices)
        self.assertEqual(BoundingBox([1, 1, 1], [5, 5, 5]), res)

    def test_repr01(self):
        ans = "BoundingBox([0.0, 0.0, 0.0], [1.0, 1.0, 1.0])"
        res = str(BoundingBox([0, 0, 0], [1, 1, 1]))
        self.assertEqual(ans, res)

    def test_repr02(self):
        ans = "BoundingBox([-1.0, 0.0, 0.0], [1.0, 1.0, 6.0])"
        res = str(BoundingBox([-1, 0, 0], [1, 1, 6]))
        self.assertEqual(ans, res)
