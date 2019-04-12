import numpy as np


def is_arrays_equal(a: np.ndarray, b: np.ndarray):
    if a.shape != b.shape:
        return False
    return np.allclose(a, b)


def triangulate_polygons(polygon_vertex_indices):
    res = []
    for polygon in polygon_vertex_indices:
        n_vertices = len(polygon)
        assert n_vertices >= 3
        for i in range(n_vertices - 2):
            res.append([polygon[0], polygon[i + 1], polygon[i + 2]])

    return res
