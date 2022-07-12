import unittest

import numpy as np
import geom_tools
from geom_tools.utils import is_arrays_equal


class TestObjParser(unittest.TestCase):
    def test_from_obj_string01(self):
        content = """
        v 1 0 0
        v 0 1 0
        v 0 0 1
        
        f 1 2 3
        
        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ]),
            polygon_vertex_indices=[[0, 1, 2]],
            triangle_vertex_indices=np.array([[0, 1, 2]])
        )
        self.assertTrue(res == ans)

    def test_from_obj_string02(self):
        content = """
        v 1 0 0
        v 0 1 0
        v 0 0 1
        v 16 3 2

        f 1 2 3 4

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [16, 3, 2],
            ]),
            polygon_vertex_indices=[[0, 1, 2, 3]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 3]])
        )
        self.assertTrue(res == ans)

    def test_from_obj_string03(self):
        content = """
        v 1 0 0
        v 0 1 0
        v 0 0 1
        v 16 3 2
        
        vn 1 0 0

        f 1//1 2//1 3//1 4//1

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [16, 3, 2],
            ]),
            polygon_vertex_indices=[[0, 1, 2, 3]],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 3]])
        )
        self.assertTrue(res == ans)

    def test_from_obj_string04(self):
        content = """
        v 1 0 0
        v 0 1 0
        v 0 0 1
        v 16 3 2

        vt 0.5 0
        vt 0.5 0.5
        vt 0 0.5

        f 1/1 2/2 3/3 4/1

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [16, 3, 2],
            ]),
            polygon_vertex_indices=[[0, 1, 2, 3]],
            texture_vertices=np.array([
                [0.5, 0],
                [0.5, 0.5],
                [0, 0.5]
            ]),
            texture_polygon_vertex_indices=[
                [0, 1, 2, 0]
            ],
            triangle_vertex_indices=np.array([[0, 1, 2], [0, 2, 3]]),
            triangle_texture_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 0]
            ]),
        )
        self.assertTrue(res == ans)

    def test_from_obj_string05(self):
        content = """
        v 1 0 0
        v 16 3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0
        vt 0.5 0.5
        vt 0 0.5

        f 1/1 2/2 3/3 4/1
        f 2/1 3/2 4/3

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [16, 3, 2],
                [0, 1, 0],
                [0, 0, 1],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2, 3],
                [1, 2, 3]
            ],
            texture_vertices=np.array([
                [0.5, 0],
                [0.5, 0.5],
                [0, 0.5]
            ]),
            texture_polygon_vertex_indices=[
                [0, 1, 2, 0],
                [0, 1, 2],
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 3],
                [1, 2, 3],
            ]),
            triangle_texture_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 0],
                [0, 1, 2],
            ]),
        )
        self.assertTrue(res == ans)

    def test_from_obj_string06(self):
        content = """
        v 1 0 0
        v 16 3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0
        vt 0.5 0.5
        vt 0 0.5

        f 1/1 2/2 3/3 4/1        
        f 2/1 3/2 4/3

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [16, 3, 2],
                [0, 1, 0],
                [0, 0, 1],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2, 3],
                [1, 2, 3]
            ],
            texture_vertices=np.array([
                [0.5, 0],
                [0.5, 0.5],
                [0, 0.5]
            ]),
            texture_polygon_vertex_indices=[
                [0, 1, 2, 0],
                [0, 1, 2],
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 3],
                [1, 2, 3],
            ]),
            triangle_texture_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 0],
                [0, 1, 2],
            ]),
        )
        self.assertTrue(res == ans)

    def test_from_obj_string07(self):
        content = """
        v 1 0 0
        v 16 3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0 0
        vt 0.5 0.5 0 
        vt 0 0.5 0

        f 1/1 2/2 3/3 4/1
        # something useful
        f 2/1 3/2 4/3

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [16, 3, 2],
                [0, 1, 0],
                [0, 0, 1],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2, 3],
                [1, 2, 3]
            ],
            texture_vertices=np.array([
                [0.5, 0],
                [0.5, 0.5],
                [0, 0.5]
            ]),
            texture_polygon_vertex_indices=[
                [0, 1, 2, 0],
                [0, 1, 2],
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 3],
                [1, 2, 3],
            ]),
            triangle_texture_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 0],
                [0, 1, 2],
            ]),
        )
        self.assertTrue(res == ans)

    def test_from_obj_string08(self):
        content = """
        v 1 0 0
        v 16   3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0 0
        vt 0.5 0.5 0 
        vt 0 0.5 0

        f 1/1 2/2 3/3 4/1
        # something useful
        f 2/1 3/2 4/3

        """
        res = geom_tools.from_obj_string(content, compute_normals=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [1, 0, 0],
                [16, 3, 2],
                [0, 1, 0],
                [0, 0, 1],
            ]),
            polygon_vertex_indices=[
                [0, 1, 2, 3],
                [1, 2, 3]
            ],
            texture_vertices=np.array([
                [0.5, 0],
                [0.5, 0.5],
                [0, 0.5]
            ]),
            texture_polygon_vertex_indices=[
                [0, 1, 2, 0],
                [0, 1, 2],
            ],
            triangle_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 3],
                [1, 2, 3],
            ]),
            triangle_texture_vertex_indices=np.array([
                [0, 1, 2],
                [0, 2, 0],
                [0, 1, 2],
            ]),
        )
        self.assertTrue(res == ans)

    def test_from_obj_string09(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0        

        vn 1 0 0

        f 1//1 2//1 3//1 

        """
        res = geom_tools.from_obj_string(content, compute_normals=True)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2]],
            triangle_vertex_indices=np.array([[0, 1, 2]]),
            normals=np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]], dtype=np.float32),
        )
        self.assertTrue(res == ans)

    def test_from_obj_string10(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        g Face
        f 1 2 3 

        """
        res = geom_tools.from_obj_string(content, compute_normals=True)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2]],
            triangle_vertex_indices=np.array([[0, 1, 2]]),
            normals=np.array([[0, 0, 1], [0, 0, 1], [0, 0, 1]], dtype=np.float32),
            polygon_groups=[0],
            group_names=["Face"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string11(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        g Face
        f 1 2 3
        f 1 2 3  

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2]],
            polygon_groups=[0, 0],
            group_names=["Face"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string12(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        g Face
        f 1 2 3
        g Face
        f 1 2 3  

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2]],
            polygon_groups=[0, 0],
            group_names=["Face"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string13(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        g Face
        f 1 2 3
        g Hand
        f 1 2 3  
        g Face
        f 1 2 3

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2], [0, 1, 2]],
            polygon_groups=[0, 1, 0],
            group_names=["Face", "Hand"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string14(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        g Face
        f 1 2 3
                g      Hand
        f 1 2 3  
        g Face
        f 1 2 3
        f 3 2 1

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]],
            polygon_groups=[0, 1, 0, 0],
            group_names=["Face", "Hand"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string15(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                
        
        f 1 2 3
                g      Hand
        f 1 2 3  
        g Face
        f 1 2 3
        f 3 2 1

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]],
            polygon_groups=[-1, 0, 1, 1],
            group_names=["Hand", "Face"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string16(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        f 1 2 3
        g
        f 1 2 3  
        g Face
        f 1 2 3
        f 3 2 1

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]],
            polygon_groups=[-1, -1, 0, 0],
            group_names=["Face"]
        )
        self.assertTrue(res == ans)

    def test_from_obj_string17(self):
        content = """
        v 0 0 0
        v 1 0 0
        v 0 1 0                

        f 1 2 3
        g
        f 1 2 3  
        g Face
        f 1 2 3
            g   
        f 3 2 1

        """
        res = geom_tools.from_obj_string(content, compute_normals=False, triangulate=False)
        ans = geom_tools.Mesh(
            vertices=np.array([
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
            ]),
            polygon_vertex_indices=[[0, 1, 2], [0, 1, 2], [0, 1, 2], [2, 1, 0]],
            polygon_groups=[-1, -1, 0, -1],
            group_names=["Face"]
        )
        self.assertTrue(res == ans)

    def test_file_not_found01(self):
        self.assertRaises(FileNotFoundError, geom_tools.load, "123")

    def test_load_vertices01(self):
        content = """
        v 1 0 0
        v 0 1 0
        v 0 0 1

        f 1 2 3

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype=np.float32)
        self.assertEqual(vertices.dtype, np.float32)
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices02(self):
        content = """
        v 1 0 0
        v 0 1 0
        v 0 0 1
        v 16 3 2

        f 1 2 3 4

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [16, 3, 2],
            ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices03(self):
        content = """
        v 11 0 0
        v 0 1 0
        v 0 0 1
        
        vn 1 0 0

        f 1//1 2//1 3//1 4//1

        v 16 3 2

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
                [11, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [16, 3, 2],
            ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices04(self):
        content = """
        v 1 0.1 0
        v -2 1 0        

        vt 0.5 0
        vt 0.5 0.5
        vt 0 0.5
        
        v 0 0 1
        v 16 3 2

        f 1/1 2/2 3/3 4/1

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0.1, 0],
            [-2, 1, 0],
            [0, 0, 1],
            [16, 3, 2],
        ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices05(self):
        content = """
        v 1 0 0
        v 16 3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0
        vt 0.5 0.5
        vt 0 0.5

        f 1/1 2/2 3/3 4/1
        f 2/1 3/2 4/3

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0, 0],
            [16, 3, 2],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices06(self):
        content = """
        v 1 0 0
        v 16 3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0
        vt 0.5 0.5
        vt 0 0.5

        f 1/1 2/2 3/3 4/1
        g something useful
        f 2/1 3/2 4/3

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0, 0],
            [16, 3, 2],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices07(self):
        content = """
        v 1 0 0
        v 16 3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0 0
        vt 0.5 0.5 0 
        vt 0 0.5 0

        f 1/1 2/2 3/3 4/1
        g something useful
        f 2/1 3/2 4/3

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0, 0],
            [16, 3, 2],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices08(self):
        content = """
        v 1 0 0
        v 16   3 2
        v 0 1 0
        v 0 0 1

        vt 0.5 0 0
        vt 0.5 0.5 0 
        vt 0 0.5 0

        f 1/1 2/2 3/3 4/1
        g something useful
        f 2/1 3/2 4/3

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0, 0],
            [16, 3, 2],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices09(self):
        content = """
        v 1 0 0
        v 16   3 2.2
        v 0 1 0
        v 0 0 1

        vt 0.5 0 0
        vt 0.5 0.5 0 
        vt 0 0.5 0

        f 1/1 2/2 3/3 4/1
        g something useful
        f 2/1 3/2 4/3

        """
        vertices = geom_tools.obj_import.from_obj_string_vertices(content)

        ans_vertices = np.array([
            [1, 0, 0],
            [16, 3, 2.2],
            [0, 1, 0],
            [0, 0, 1],
        ])
        self.assertTrue(is_arrays_equal(ans_vertices, vertices))

    def test_load_vertices10(self):
        content = """
        v Hi! 0 0
        v 16   3 2.2
        v 0 1 0
        v 0 0 1

        vt 0.5 0 0
        vt 0.5 0.5 0 
        vt 0 0.5 0

        f 1/1 2/2 3/3 4/1
        g something useful
        f 2/1 3/2 4/3

        """
        self.assertRaises(ValueError, geom_tools.obj_import.from_obj_string_vertices, content)

    def test_load_vertices11(self):
        content = """
        v 5 3

        """
        self.assertRaises(ValueError, geom_tools.obj_import.from_obj_string_vertices, content)

    def test_load_vertices12(self):
        content = """
        v 5 2"""
        self.assertRaises(ValueError, geom_tools.obj_import.from_obj_string_vertices, content)

    def test_load_vertices13(self):
        content = """
        v 5 2 """
        self.assertRaises(ValueError, geom_tools.obj_import.from_obj_string_vertices, content)


if __name__ == '__main__':
    unittest.main()
