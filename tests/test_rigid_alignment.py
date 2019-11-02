import unittest

import geom_tools


class TestRigidAlignment(unittest.TestCase):
    def test_rigid_alignment01(self):
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
        transformation = geom_tools.rigid_alignment_transformation(src, dst)
        res = geom_tools.transform_vertices(transformation, src)
        self.assertTrue(geom_tools.utils.is_arrays_equal(res, dst))

    def test_rigid_alignment02(self):
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
        transformation = geom_tools.rigid_alignment_transformation(src, dst)
        res = geom_tools.transform_vertices(transformation, src)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))

    def test_rigid_alignment03(self):
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
        transformation = geom_tools.rigid_alignment_transformation(src, dst)
        res = geom_tools.transform_vertices(transformation, src)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))


if __name__ == '__main__':
    unittest.main()
