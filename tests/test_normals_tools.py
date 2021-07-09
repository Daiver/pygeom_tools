import unittest

import numpy as np
from geom_tools import normals_tools


class TestNormalsTools(unittest.TestCase):
    def test_compute_normals_for_triangles01(self):
        vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [0, 1, 2]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, 1]
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_normals_for_triangles02(self):
        vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1]
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_normals_for_triangles03(self):
        vertices = np.array([
            [0, 0, 40],
            [0.1, 0, 40],
            [0, 50, 40],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1]
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_normals_for_triangles04(self):
        vertices = np.array([
            [0, 0, 40],
            [0.1, 0, 40],
            [0, 50, 40],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1]
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_normals_for_triangles05(self):
        vertices = np.array([
            [0, 0, -40],
            [0.1, 0, -40],
            [0, 50, -40],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1],
            [0, 0, -1],
            [0, 0, -1],
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_normals_for_triangles06(self):
        vertices = np.array([
            [0, 0, -40],
            [0.1, 0, -40],
            [0, 50, -40],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 1],
            [0, 0, 1],
            [0, 1, 0]
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0],
            [0, 2, 1],
            [1, 0, 2],
            [3, 4, 5],
            [3, 6, 7]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1],
            [0, 0, -1],
            [0, 0, -1],
            [0, -1, 0],
            [-1, 0, 0]
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_normals_for_triangles07(self):
        vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [0, 1, 2]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, 0]
        ], dtype=np.float32)

        res = normals_tools.compute_normals_for_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_vertices_normals_from_triangles01(self):
        vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [0, 1, 2]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
        ], dtype=np.float32)
        res = normals_tools.compute_vertices_normals_from_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_vertices_normals_from_triangles02(self):
        vertices = np.array([
            [0, 0, -40],
            [0.1, 0, -40],
            [0, 50, -40],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 1],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0],
            [3, 4, 5],
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1],
            [0, 0, -1],
            [0, 0, -1],
            [0, -1, 0],
            [0, -1, 0],
            [0, -1, 0],
        ], dtype=np.float32)
        res = normals_tools.compute_vertices_normals_from_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_vertices_normals_from_triangles03(self):
        vertices = np.array([
            [0, 0, 0],
            [0.1, 0, 0],
            [0, 50, 0],
            [1, 0, 0],
            [0, 0, 1],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [2, 1, 0],
            [0, 3, 4],
        ], dtype=np.int32)
        ans = np.array([
            [0, -0.70710678, -0.70710678],
            [0, 0, -1],
            [0, 0, -1],
            [0, -1, 0],
            [0, -1, 0],
        ], dtype=np.float32)
        res = normals_tools.compute_vertices_normals_from_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_vertices_normals_from_triangles04(self):
        vertices = np.array([
            [0.1, 0, 0],
            [0, 50, 0],
            [1, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [1, 0, 4],
            [4, 2, 3],
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, -1],
            [0, 0, -1],
            [0, -1, 0],
            [0, -1, 0],
            [0, -0.70710678, -0.70710678],
        ], dtype=np.float32)
        res = normals_tools.compute_vertices_normals_from_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_compute_vertices_normals_from_triangles05(self):
        vertices = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
        ], dtype=np.float32)
        triangle_vertex_indices = np.array([
            [0, 1, 2]
        ], dtype=np.int32)
        ans = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ], dtype=np.float32)
        res = normals_tools.compute_vertices_normals_from_triangles(vertices, triangle_vertex_indices)
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))


if __name__ == '__main__':
    unittest.main()
