import unittest

import numpy as np
from geom_tools import Mesh


class TestMesh(unittest.TestCase):
    def test_mesh_has_uv01(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2])
        self.assertFalse(mesh1.has_uv())

    def test_mesh_has_uv02(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2],
            texture_vertices=np.arange(3), texture_polygon_vertex_indices=[2, 1, 0])
        self.assertTrue(mesh1.has_uv())

    def test_mesh_has_normals01(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2])
        self.assertFalse(mesh1.has_normals())

    def test_mesh_has_normals02(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2], normals=np.array([1, 2, 3]))
        self.assertTrue(mesh1.has_normals())

    # TODO: cover all comparison branches
    def test_mesh_comparison01(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2])
        mesh2 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2])
        self.assertTrue(mesh1 == mesh2)

    def test_mesh_comparison02(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2])
        mesh2 = Mesh(vertices=np.arange(2), polygon_vertex_indices=[0, 1, 2])
        self.assertTrue(mesh1 != mesh2)

    def test_mesh_comparison03(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2, 4], triangle_vertex_indices=[[0, 1, 2], [0, 2, 4]])
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2, 4], triangle_vertex_indices=[[0, 1, 2], [0, 2, 4]])
        self.assertTrue(mesh1 == mesh2)

    def test_mesh_comparison04(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2, 4], triangle_vertex_indices=[[0, 1, 2], [0, 2, 4]])
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2, 4], triangle_vertex_indices=[[0, 1, 2], [0, 6, 4]])
        self.assertTrue(mesh1 != mesh2)

    def test_mesh_n_vertices01(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[0, 1, 2])
        self.assertEqual(mesh1.n_vertices(), 5)

    def test_mesh_n_texture_vertices01(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[0, 1, 2],
            texture_vertices=np.arange(6), texture_polygon_vertex_indices=[2, 1, 0])
        self.assertTrue(mesh1.n_texture_vertices(), 6)
