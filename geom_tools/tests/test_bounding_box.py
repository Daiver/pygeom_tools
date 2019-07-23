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
