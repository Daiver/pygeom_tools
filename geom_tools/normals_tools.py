import numpy as np


def compute_normals_for_triangles(
        vertices: np.ndarray,
        triangle_vertex_indices: np.ndarray,
        eps_zero_length: float = 1e-8
) -> np.ndarray:
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
    length = np.where(length > eps_zero_length, length, 1)
    return cross / length


def compute_vertices_normals_from_triangles(
        vertices: np.ndarray,
        triangle_vertex_indices: np.ndarray,
        eps_zero_length=1e-8
) -> np.ndarray:
    """
    Assumes anti-clockwise vertices order
    Super slow can be written in C++
    """
    assert vertices.ndim == 2 and vertices.shape[1] == 3
    assert triangle_vertex_indices.ndim == 2 and triangle_vertex_indices.shape[1] == 3
    n_vertices = vertices.shape[0]
    n_triangles = triangle_vertex_indices.shape[0]
    normals_per_triangle = compute_normals_for_triangles(vertices, triangle_vertex_indices, eps_zero_length)
    res = np.zeros((n_vertices, 3), dtype=np.float32)
    for tri_ind in range(n_triangles):
        for v_ind in triangle_vertex_indices[tri_ind]:
            res[v_ind] += normals_per_triangle[tri_ind]

    length = np.linalg.norm(res, axis=1).reshape(-1, 1)
    length = np.where(length > eps_zero_length, length, 1)
    return res / length
