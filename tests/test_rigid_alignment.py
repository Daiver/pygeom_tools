import unittest

import numpy as np

import geom_tools
from geom_tools.rigid_alignment import find_rotation_and_translation


class TestRigidAlignment(unittest.TestCase):
    def test_find_rotation_and_translation01(self):
        src = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        dst = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        src = np.array(src)
        dst = np.array(dst)
        transformation = find_rotation_and_translation(src, dst)
        res = geom_tools.transform_vertices(transformation, src)
        self.assertTrue(geom_tools.utils.is_arrays_equal(res, dst))

    def test_find_rotation_and_translation02(self):
        src = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 2],
            [0, 0, -2],
        ]
        dst = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, -1],
        ]
        ans = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 2],
            [0, 0, -2],
        ]
        src = np.array(src)
        dst = np.array(dst)
        transformation = find_rotation_and_translation(src, dst)
        res = geom_tools.transform_vertices(transformation, src)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))

    def test_find_rotation_and_translation03(self):
        src = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 2],
            [0, 0, -2],
        ]
        dst = [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1],
            [0, 0, -1],
        ]
        ans = [
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 2],
            [0, 0, -2],
        ]
        src = np.array(src)
        dst = np.array(dst)
        transformation = find_rotation_and_translation(src, dst)
        res = geom_tools.transform_vertices(transformation, src)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))


if __name__ == '__main__':
    unittest.main()
