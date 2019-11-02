import unittest

import numpy as np
import geom_tools
from geom_tools.utils import is_arrays_equal


class TestTransformations(unittest.TestCase):
    def test_rotated_and_translated01(self):
        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        vector = [0, 0, 0]

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [0, 0, 0]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [0, 0, 0]
            ]
        ))

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [5, -3, 6],
                [13, 2, 0]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [5, -3, 6],
                [13, 2, 0]
            ]
        ))

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [5, -3, 6],
                [13, 2, 0],
                [-4.5, 55, 1]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [5, -3, 6],
                [13, 2, 0],
                [-4.5, 55, 1]
            ]
        ))
        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [5, -3, 6],
                [13, 2, 0],
                [-4.5, 55, 1],
                [2, 4, 8],
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [5, -3, 6],
                [13, 2, 0],
                [-4.5, 55, 1],
                [2, 4, 8],
            ]
        ))

    def test_rotated_and_translated02(self):
        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        vector = [0, 5, 0]

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [0, 0, 0]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [0, 5, 0]
            ]
        ))

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [5, -3, 6],
                [13, 2, 0]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [5, 2, 6],
                [13, 7, 0]
            ]
        ))

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [5, -3, 6],
                [13, 2, 0],
                [-4.5, 55, 1]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [5, 2, 6],
                [13, 7, 0],
                [-4.5, 60, 1]
            ]
        ))
        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [5, -3, 6],
                [13, 2, 0],
                [-4.5, 55, 1],
                [2, 4, 8],
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [5, 2, 6],
                [13, 7, 0],
                [-4.5, 60, 1],
                [2, 9, 8],
            ]
        ))

    def test_rotated_and_translated03(self):
        matrix = [
            [0.5, 0, 0],
            [0, 2, 0],
            [0, 0, 0.1]
        ]
        vector = [0, 0, 0]

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [0, 0, 0],
                [13, -10, 5]
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [0, 0, 0],
                [6.5, -20, 0.5]
            ]
        ))

    def test_rotated_and_translated04(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]
        vector = [0, 0, 0]

        res = geom_tools.rotated_and_translated(
            matrix, vector,
            vertices=[
                [0, 0, 0],
                [1, 0, 5],
                [0, 3, -5],
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [0, 0, 0],
                [0, 1, 5],
                [3, 0, -5],
            ]
        ))

    def test_rotated_and_translated05(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [2, 0, 0]
        ]
        vector = [2, 0, 3]

        res = geom_tools.rotated_and_translated(
            rotation_matrix=matrix, translation=vector,
            vertices=[
                [0, 0, 0],
                [1, 0, 5],
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [2, 0, 3],
                [2, 1, 5],
            ]
        ))

    def test_rotated_and_translated06(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [2, 0, 0]
        ]
        vector = [2, 0, 3]

        res = geom_tools.transform_vertices(
            (matrix, vector),
            vertices=[
                [0, 0, 0],
                [1, 0, 5],
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [2, 0, 3],
                [2, 1, 5],
            ]
        ))

    def test_rotated01(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]

        res = geom_tools.rotated(
            matrix,
            vertices=[
                [0, 0, 0],
                [1, 0, 5],
                [0, 3, -5],
            ]
        )
        self.assertTrue(is_arrays_equal(
            res,
            [
                [0, 0, 0],
                [0, 1, 5],
                [3, 0, -5],
            ]
        ))

    def test_rotation_around_vertex01(self):
        rotation = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]
        center = [0, 2, 0]
        transformation = geom_tools.rotation_around_vertex(rotation, center)
        vertices = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        res = geom_tools.transform_vertices(transformation, vertices)
        ans = [
            [2, 3, 0],
            [1, 2, 0],
            [2, 2, 1],
        ]
        self.assertTrue(is_arrays_equal(ans, res))

    def test_rotation_around_vertex02(self):
        rotation = [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ]
        center = [0, 2, 0]
        transformation = geom_tools.rotation_around_vertex(rotation, center, translation=[1, 2, 6])
        vertices = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
        res = geom_tools.transform_vertices(transformation, vertices)
        ans = [
            [3, 5, 6],
            [2, 4, 6],
            [3, 4, 7],
        ]
        self.assertTrue(is_arrays_equal(ans, res))

    def test_translated_points01(self):
        translation = np.array([-1, -2, -3], dtype=np.float32)
        vertices = np.array([
            [1, 2, 3]
        ], dtype=np.float32)
        res = geom_tools.translated(translation, vertices)
        self.assertTrue(is_arrays_equal([[0, 0, 0]], res))

    def test_translated_points02(self):
        translation = np.array([-1, -2, -3], dtype=np.float32)
        vertices = np.array([
            [1, 2, 3],
            [4, 0, 2],
        ], dtype=np.float32)
        res = geom_tools.translated(translation, vertices)
        ans = [
            [0, 0, 0],
            [3, -2, -1]
        ]
        self.assertTrue(is_arrays_equal(ans, res))

    def test_translated_points03(self):
        translation = np.array([-1, 1, -3], dtype=np.float32)
        vertices = np.array([
            [1, 2, 3],
            [4, 0, 2],
            [5, 6, 7]
        ], dtype=np.float32)
        res = geom_tools.translated(translation, vertices)
        ans = [
            [0, 3, 0],
            [3, 1, -1],
            [4, 7, 4]
        ]
        self.assertTrue(is_arrays_equal(ans, res))

    def test_translated_points04(self):
        translation = np.array([-1, 1, -3], dtype=np.float32)
        vertices = np.array([
            [1, 2, 3],
            [4, 0, 2],
            [5, 6, 7],
            [0, 0, 0]
        ], dtype=np.float32)
        res = geom_tools.translated(translation, vertices)
        ans = [
            [0, 3, 0],
            [3, 1, -1],
            [4, 7, 4],
            [-1, 1, -3]
        ]
        self.assertTrue(is_arrays_equal(ans, res))

    def test_translated_points05(self):
        translation = [-1, 1, -3]
        vertices = [
            [1, 2, 3],
            [4, 0, 2],
            [5, 6, 7],
            [0, 0, 0]
        ]
        res = geom_tools.translated(translation, vertices)
        ans = [
            [0, 3, 0],
            [3, 1, -1],
            [4, 7, 4],
            [-1, 1, -3]
        ]
        self.assertTrue(is_arrays_equal(ans, res))


if __name__ == '__main__':
    unittest.main()
