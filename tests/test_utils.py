import unittest

import numpy as np
import geom_tools


class TestObjParser(unittest.TestCase):
    def test_is_array_equal01(self):
        self.assertTrue(geom_tools.utils.is_arrays_equal(np.array([1, 2]), np.array([1, 2])))

    def test_is_array_equal02(self):
        self.assertFalse(geom_tools.utils.is_arrays_equal(np.array([1, 2]), np.array([6, 2])))

    def test_is_array_equal03(self):
        self.assertFalse(geom_tools.utils.is_arrays_equal(np.array([1, 1, 2]), np.array([1, 2])))

    def test_triangulate01(self):
        faces = [
            [5, 3, 5]
        ]
        res = geom_tools.utils.triangulate_polygons(faces)
        ans = [[5, 3, 5]]
        self.assertTrue(res == ans)

    def test_triangulate02(self):
        faces = [
            [5, 3, 6, 5]
        ]
        res = geom_tools.utils.triangulate_polygons(faces)
        ans = [
            [5, 3, 6],
            [5, 6, 5],
        ]
        self.assertTrue(res == ans)

    def test_triangulate03(self):
        faces = [
            [11, 5, 3, 6, 5],
            [0, 3, 4],
            [1, 2, 3, 4]
        ]
        res = geom_tools.utils.triangulate_polygons(faces)
        ans = [
            [11, 5, 3],
            [11, 3, 6],
            [11, 6, 5],
            [0, 3, 4],
            [1, 2, 3],
            [1, 3, 4]
        ]
        self.assertTrue(res == ans)


if __name__ == '__main__':
    unittest.main()
