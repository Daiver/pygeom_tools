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

    def test_cov_mat_from_vertices_weighted01(self):
        vertices1 = np.array([
            [1, 2, 0],
        ], dtype=np.float32)
        vertices2 = np.array([
            [3, 5, 0],
        ], dtype=np.float32)
        weights = np.array([
            2
        ])
        ans = np.array([
            [6, 10, 0],
            [12, 20, 0],
            [0, 0, 0],
        ], dtype=np.float32)
        res = geom_tools.rigid_alignment.cov_mat_from_vertices_weighted(vertices1, vertices2, weights)
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans, res))

    def test_find_rotation_and_translation_weighted01(self):
        vertices1 = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [1, 0, 0],
            [0, 1, 0]
        ])
        vertices2 = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [1, 0, 0],
            [0, 1, 0]
        ])
        weights = np.array([1, 1, 1, 1])
        ans_trans = np.array([0, 0, 0], dtype=np.float32)
        ans_rot = np.eye(3)
        res_rot, res_trans = geom_tools.rigid_alignment.find_rotation_and_translation_weighted(
            vertices1, vertices2, weights
        )
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans_rot, res_rot))
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans_trans, res_trans))

    def test_find_rotation_and_translation_weighted02(self):
        vertices1 = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [1, 0, 0],
            [1, 20, -55],
            [0, 1, 0]
        ])
        vertices2 = np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [1, 0, 0],
            [100, 2340, 55],
            [0, 1, 0]
        ])
        weights = np.array([1, 1, 1, 0, 1])
        ans_trans = np.array([0, 0, 0], dtype=np.float32)
        ans_rot = np.eye(3)
        res_rot, res_trans = geom_tools.rigid_alignment.find_rotation_and_translation_weighted(
            vertices1, vertices2, weights
        )
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans_rot, res_rot))
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans_trans, res_trans))

    def test_find_rotation_and_translation_weighted03(self):
        vertices1 = np.array([
            [-1, 0, 0.5],
            [-2, -4, 5],
            [0, -1, 0.5],
            [1, 0, 0.5],
            [0, 1, 0.5],
            [22, -5, 2],
        ])
        vertices2 = np.array([
            [0, 2, 1],
            [13, 3, 3],
            [-2, 0, 1],
            [0, -2, 1],
            [2, 0, 1],
            [16, 55, 33],
        ])
        weights = np.array([1, 0, 1, 1, 1, 0])
        ans_trans = np.array([0, 0, 0.5], dtype=np.float32)
        ans_rot = np.array([
            [0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]
        ], dtype=np.float)
        res_rot, res_trans = geom_tools.rigid_alignment.find_rotation_and_translation_weighted(
            vertices1, vertices2, weights
        )
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans_rot, res_rot))
        self.assertTrue(geom_tools.utils.is_arrays_equal(ans_trans, res_trans))


if __name__ == '__main__':
    unittest.main()
