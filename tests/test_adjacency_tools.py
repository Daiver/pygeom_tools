import unittest

from geom_tools.adjacency_tools import (
    vertices_adjacency_from_polygon_vertex_indices,
    max_vertex_ind_in_list
)


class TestAdjacencyTools(unittest.TestCase):
    def test_vertices_adjacency_from_polygon_vertex_indices01(self):
        indices = [
            [0, 1, 2]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
            [1, 2],
            [0, 2],
            [0, 1],
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices02(self):
        indices = [
            [1, 2, 3]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
            [],
            [2, 3],
            [1, 3],
            [1, 2]
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices03(self):
        indices = [
            [3, 1, 2]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices, 5)
        ans = [
            [],
            [2, 3],
            [1, 3],
            [1, 2],
            [],
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices04(self):
        indices = [
            [1, 2, 3],
            [0, 2, 1]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
            [1, 2],
            [0, 2, 3],
            [0, 1, 3],
            [1, 2],
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices05(self):
        indices = [
            [5, 4],
            [1, 2, 3],
            [0, 2, 1]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
            [1, 2],
            [0, 2, 3],
            [0, 1, 3],
            [1, 2],
            [5],
            [4]
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices06(self):
        indices = [
            [4, 2, 0, 1, 3]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
            [1, 2],  # 0
            [0, 3],  # 1
            [0, 4],  # 2
            [1, 4],  # 3
            [2, 3],  # 4
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices07(self):
        indices = [
            [4, 2, 0, 1, 3],
            [7, 8, 6]
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
            [1, 2],  # 0
            [0, 3],  # 1
            [0, 4],  # 2
            [1, 4],  # 3
            [2, 3],  # 4
            [],
            [7, 8],
            [6, 8],
            [6, 7]
        ]
        self.assertEqual(ans, res)

    def test_vertices_adjacency_from_polygon_vertex_indices08(self):
        indices = [
            [0, 2, 3, 1],
            [2, 3, 6],
            [6, 3, 5],
            [2, 6, 4],
            [6, 5, 4],
            [7, 9, 8, 1],
            [0, 10, 2],
        ]
        res = vertices_adjacency_from_polygon_vertex_indices(indices)
        ans = [
              [1, 2, 10],
              [0, 3, 7, 8],
              [0, 3, 4, 6, 10],
              [1, 2, 5, 6],
              [2, 5, 6],
              [3, 4, 6],
              [2, 3, 4, 5],
              [1, 9],
              [1, 9],
              [7, 8],
              [0, 2],
        ]
        self.assertEqual(ans, res)

    def test_max_vertex_ind_in_list01(self):
        indices = [[1]]
        self.assertEqual(1, max_vertex_ind_in_list(indices))

    def test_max_vertex_ind_in_list02(self):
        indices = [[1, 0, 3]]
        self.assertEqual(3, max_vertex_ind_in_list(indices))

    def test_max_vertex_ind_in_list03(self):
        indices = [[6, 5], [1, 0, 3]]
        self.assertEqual(6, max_vertex_ind_in_list(indices))

    def test_max_vertex_ind_in_list04(self):
        indices = [[1, 2, 3, 4], [6, 50], [1, 0, 3]]
        self.assertEqual(50, max_vertex_ind_in_list(indices))


if __name__ == '__main__':
    unittest.main()
