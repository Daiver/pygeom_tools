import unittest

import io
import numpy as np
import geom_tools


class TestObjParser(unittest.TestCase):
    def test_mesh_obj_export01(self):
        mesh = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ], dtype=np.float32),
            polygon_vertex_indices=[
                [0, 1, 2]
            ],
        )

        stream = io.StringIO()
        geom_tools.save_to_stream(stream, mesh)
        res = stream.getvalue()
        ans = """\
v 1.0 0.0 0.0
v 0.0 1.0 0.0
v 0.0 0.0 1.0

f 1 2 3
"""
        self.assertEqual(res, ans)

    def test_mesh_obj_export02(self):
        mesh = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [5, 6, 7.5],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2, 3],
                [3, 1, 2],
            ],
        )

        stream = io.StringIO()
        geom_tools.save_to_stream(stream, mesh)
        res = stream.getvalue()
        ans = """\
v 1.0 0.0 0.0
v 0.0 1.0 0.0
v 0.0 0.0 1.0
v 5.0 6.0 7.5

f 1 2 3 4
f 4 2 3
"""
        self.assertEqual(res, ans)

    def test_mesh_obj_export03(self):
        mesh = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ], dtype=np.float32),
            polygon_vertex_indices=[
                [0, 1, 2]
            ],
            texture_vertices=np.array([
                [0, 1],
                [1, 0],
                [1, 0.5]
            ], dtype=np.float32),
            texture_polygon_vertex_indices=[
                [2, 0, 1]
            ],
        )

        stream = io.StringIO()
        geom_tools.save_to_stream(stream, mesh)
        res = stream.getvalue()
        ans = """\
v 1.0 0.0 0.0
v 0.0 1.0 0.0
v 0.0 0.0 1.0

vt 0.0 1.0
vt 1.0 0.0
vt 1.0 0.5

f 1/3 2/1 3/2
"""
        self.assertEqual(res, ans)

    def test_mesh_obj_export04(self):
        mesh = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
            ], dtype=np.float32),
            polygon_vertex_indices=[
                [0, 1, 2],
                [2, 1, 0, 2],
                [1, 2, 0]
            ],
            texture_vertices=np.array([
                [0, 1],
                [1, 0],
                [1, 0.5],
                [0.5, 0.5],
            ], dtype=np.float32),
            texture_polygon_vertex_indices=[
                [2, 0, 1],
                [3, 1, 0, 2],
                [0, 2, 3],
            ],
        )

        stream = io.StringIO()
        geom_tools.save_to_stream(stream, mesh)
        res = stream.getvalue()
        ans = """\
v 1.0 0.0 0.0
v 0.0 1.0 0.0
v 0.0 0.0 1.0

vt 0.0 1.0
vt 1.0 0.0
vt 1.0 0.5
vt 0.5 0.5

f 1/3 2/1 3/2
f 3/4 2/2 1/1 3/3
f 2/1 3/3 1/4
"""
        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()
