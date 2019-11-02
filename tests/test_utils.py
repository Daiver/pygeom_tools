import unittest

import numpy as np
import geom_tools


class TestUtils(unittest.TestCase):
    def test_is_array_equal01(self):
        self.assertTrue(geom_tools.utils.is_arrays_equal(np.array([1, 2]), np.array([1, 2])))

    def test_is_array_equal02(self):
        self.assertFalse(geom_tools.utils.is_arrays_equal(np.array([1, 2]), np.array([6, 2])))

    def test_is_array_equal03(self):
        self.assertFalse(geom_tools.utils.is_arrays_equal(np.array([1, 1, 2]), np.array([1, 2])))

    def test_is_none_or_ndarray01(self):
        self.assertTrue(geom_tools.utils.is_none_or_ndarray(None))
        self.assertFalse(geom_tools.utils.is_none_or_ndarray(1))
        self.assertFalse(geom_tools.utils.is_none_or_ndarray("31"))
        self.assertTrue(geom_tools.utils.is_none_or_ndarray(np.zeros(2)))
        self.assertTrue(geom_tools.utils.is_none_or_ndarray(np.zeros(2, dtype=np.uint8), required_dtype=np.uint8))
        self.assertFalse(geom_tools.utils.is_none_or_ndarray(np.zeros(2, dtype=np.int32), required_dtype=np.uint8))

    def test_is_array_equal_or_both_none01(self):
        self.assertTrue(geom_tools.utils.is_arrays_equal_or_both_none(np.array([1, 2]), np.array([1, 2])))
        self.assertFalse(geom_tools.utils.is_arrays_equal_or_both_none(np.array([1, 2]), None))
        self.assertFalse(geom_tools.utils.is_arrays_equal_or_both_none(None, np.array([1, 2])))
        self.assertTrue(geom_tools.utils.is_arrays_equal_or_both_none(None, None))

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

    def test_center_of_vertices01(self):
        vertices = [
            [0, 0, 0]
        ]
        ans = [0, 0, 0]
        res = geom_tools.utils.center_of_vertices(vertices)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))

    def test_center_of_vertices02(self):
        vertices = [
            [0, 0],
            [1, 0]
        ]
        ans = [0.5, 0]
        res = geom_tools.utils.center_of_vertices(vertices)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))

    def test_center_of_vertices03(self):
        vertices = [
            [0, 0],
            [1, 0],
            [2, 0.3]
        ]
        ans = [1.0, 0.1]
        res = geom_tools.utils.center_of_vertices(vertices)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))

    def test_center_of_vertices04(self):
        vertices = [
            [0, 0, 3],
            [1, 0, 1],
            [2, -0.3, 2]
        ]
        ans = [1.0, -0.1, 2]
        res = geom_tools.utils.center_of_vertices(vertices)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))


if __name__ == '__main__':
    unittest.main()
