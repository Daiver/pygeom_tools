import numpy as np


def compute_normals_for_triangles(vertices: np.ndarray, triangle_vertex_indices: np.ndarray) -> np.ndarray:
    """
    Assumes anti-clockwise vertices order
    """
    assert vertices.ndim == 2 and vertices.shape[1] == 3
    assert triangle_vertex_indices.ndim == 2 and triangle_vertex_indices.shape[1] == 3

    vertices_for_triangles = vertices[triangle_vertex_indices]
    edges1 = vertices_for_triangles[:, 1] - vertices_for_triangles[:, 0]
    edges2 = vertices_for_triangles[:, 2] - vertices_for_triangles[:, 0]
    cross = np.cross(edges1, edges2)
    length = np.linalg.norm(cross, axis=1).reshape(-1, 1)
    return cross / length
