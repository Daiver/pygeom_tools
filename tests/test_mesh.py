import unittest

import numpy as np
from geom_tools import Mesh
from geom_tools.bounding_box import BoundingBox


class TestMesh(unittest.TestCase):
    def test_mesh_has_uv01(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]])
        self.assertFalse(mesh1.has_uv())

    def test_mesh_has_uv02(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]],
            texture_vertices=np.arange(3), texture_polygon_vertex_indices=[[2, 1, 0]])
        self.assertTrue(mesh1.has_uv())

    def test_mesh_has_normals01(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]])
        self.assertFalse(mesh1.has_normals())

    def test_mesh_has_normals02(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]], normals=np.array([1, 2, 3]))
        self.assertTrue(mesh1.has_normals())

    # TODO: cover all comparison branches
    def test_mesh_comparison01(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]])
        mesh2 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]])
        self.assertTrue(mesh1 == mesh2)

    def test_mesh_comparison02(self):
        mesh1 = Mesh(vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]])
        mesh2 = Mesh(vertices=np.arange(2), polygon_vertex_indices=[[0, 1, 2]])
        self.assertTrue(mesh1 != mesh2)

    def test_mesh_comparison03(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]))
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]))
        self.assertTrue(mesh1 == mesh2)

    def test_mesh_comparison04(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]))
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 6, 4]]))
        self.assertTrue(mesh1 != mesh2)

    def test_mesh_comparison05(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]),
            polygon_groups=[-1],
        )
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]),
        )
        self.assertTrue(mesh1 == mesh2)
        self.assertTrue(mesh2 == mesh1)

    def test_mesh_comparison06(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]),
            polygon_groups=[-1],
        )
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]),
            polygon_groups=[-1],
        )
        self.assertTrue(mesh1 == mesh2)
        self.assertTrue(mesh2 == mesh1)

    def test_mesh_comparison07(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]),
            polygon_groups=[0],
        )
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 4]]),
            polygon_groups=[-1],
        )
        self.assertTrue(mesh1 != mesh2)
        self.assertTrue(mesh2 != mesh1)

    def test_mesh_comparison08(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4], [0, 1, 2, 4]],
            polygon_groups=[1, 0],
        )
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4], [0, 1, 2, 4]],
            polygon_groups=[1, 0],
        )
        self.assertTrue(mesh1 == mesh2)
        self.assertTrue(mesh2 == mesh1)

    def test_mesh_comparison09(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4], [0, 1, 2, 4]],
            polygon_groups=[1, 0], group_names=["R", "Left"]
        )
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4], [0, 1, 2, 4]],
            polygon_groups=[1, 0], group_names=["R", "Left"]
        )
        self.assertTrue(mesh1 == mesh2)
        self.assertTrue(mesh2 == mesh1)

    def test_mesh_comparison10(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4], [0, 1, 2, 4]],
            polygon_groups=[1, 0], group_names=["R", "Left"]
        )
        mesh2 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2, 4], [0, 1, 2, 4]],
            polygon_groups=[1, 0], group_names=["Left"]
        )
        self.assertTrue(mesh1 != mesh2)
        self.assertTrue(mesh2 != mesh1)

    def test_mesh_n_vertices01(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[[0, 1, 2]])
        self.assertEqual(mesh1.n_vertices(), 5)

    def test_mesh_n_texture_vertices01(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[[0, 1, 2]])
        self.assertEqual(mesh1.n_texture_vertices(), 0)

    def test_mesh_n_texture_vertices02(self):
        mesh1 = Mesh(
            vertices=np.arange(3), polygon_vertex_indices=[[0, 1, 2]],
            texture_vertices=np.arange(6), texture_polygon_vertex_indices=[[2, 1, 0]])
        self.assertTrue(mesh1.n_texture_vertices(), 6)

    def test_mesh_n_polygons01(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[[0, 1, 2]])
        self.assertEqual(mesh1.n_polygons(), 1)

    def test_mesh_n_polygons02(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[
            [0, 1, 2],
            [4, 5, 6],
        ])
        self.assertEqual(mesh1.n_polygons(), 2)

    def test_mesh_n_triangles01(self):
        mesh1 = Mesh(
            vertices=np.arange(5), polygon_vertex_indices=[
                [0, 1, 2],
                [4, 5, 6, 8],
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2],
                [4, 5, 6],
                [4, 6, 8],
            ]))
        self.assertEqual(mesh1.n_triangles(), 3)
        self.assertTrue(mesh1.is_triangulated())

    def test_mesh_n_triangles02(self):
        mesh1 = Mesh(
            vertices=np.arange(5), polygon_vertex_indices=[
                [0, 1, 2],
                [4, 5, 6, 8],
            ])
        self.assertIsNone(mesh1.n_triangles())
        self.assertFalse(mesh1.is_triangulated())

    def test_mesh_n_groups01(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[[0, 1, 2]])
        self.assertEqual(mesh1.n_groups(), 0)

    def test_mesh_n_groups02(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[[0, 1, 2]], group_names=["F"])
        self.assertEqual(mesh1.n_groups(), 1)

    def test_mesh_n_groups03(self):
        mesh1 = Mesh(vertices=np.arange(5), polygon_vertex_indices=[[0, 1, 2]], group_names=["F", "U", "U"])
        self.assertEqual(mesh1.n_groups(), 3)

    def test_mesh_bbox01(self):
        mesh1 = Mesh(
            vertices=np.array([[0, 1, 2], [-5, 2, 3]]), polygon_vertex_indices=[
                [0, 1, 2],
                [4, 5, 6, 8],
            ])
        bbox = mesh1.bbox()
        self.assertEqual(BoundingBox([-5, 1, 2], [0, 2, 3]), bbox)

    def test_set_vertices_and_compute_normals01(self):
        mesh = Mesh(
            vertices=np.array([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2]
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2]
            ]),
        )
        new_vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
        ])
        ans = np.array([
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
        ], dtype=np.float32)
        self.assertFalse(mesh.has_normals())
        mesh.set_vertices_and_compute_normals(new_vertices)

        res = mesh.normals
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_set_vertices_and_compute_normals02(self):
        new_vertices = np.array([
            [0.1, 0, 0],
            [0, 50, 0],
            [1, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
        ], dtype=np.float32)

        mesh = Mesh(
            vertices=np.zeros_like(new_vertices),
            polygon_vertex_indices=[
                [1, 0, 4],
                [4, 2, 3],
            ],
            triangle_vertex_indices=np.array([
                [1, 0, 4],
                [4, 2, 3],
            ], dtype=np.int32),
        )
        ans = np.array([
            [0, 0, -1],
            [0, 0, -1],
            [0, -1, 0],
            [0, -1, 0],
            [0, -0.70710678, -0.70710678],
        ], dtype=np.float32)
        self.assertFalse(mesh.has_normals())
        mesh.set_vertices_and_compute_normals(new_vertices)

        res = mesh.normals
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))

    def test_set_vertices_and_compute_normals03(self):
        mesh = Mesh(
            vertices=np.array([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2]
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2]
            ]),
        )
        new_vertices = np.array([
            [0, 0, 0],
            [1, 0, 0],
            [0, 1, 0],
        ])
        ans = np.array([
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
        ], dtype=np.float32)
        self.assertFalse(mesh.has_normals())
        mesh2 = mesh.set_vertices_and_compute_normals(new_vertices)

        res = mesh2.normals
        self.assertEqual(ans.shape, res.shape)
        self.assertTrue(np.allclose(ans, res))
