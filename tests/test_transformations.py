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


if __name__ == '__main__':
    unittest.main()
