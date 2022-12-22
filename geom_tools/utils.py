from typing import List, Union, Any
import numpy as np


def is_arrays_equal(
        a: Union[List[float], List[List[float]], np.ndarray],
        b: Union[List[float], List[List[float]], np.ndarray]
) -> bool:
    a = np.array(a)
    b = np.array(b)
    if a.shape != b.shape:
        return False
    return np.allclose(a, b)


def is_arrays_equal_or_both_none(
        a: Union[None, List[float], List[List[float]], np.ndarray],
        b: Union[None, List[float], List[List[float]], np.ndarray]
) -> bool:
    if a is not None and b is not None:
        return is_arrays_equal(a, b)
    return (a is None) and (b is None)


def is_none_or_ndarray(variable: Any, required_dtype: np.dtype = None) -> bool:
    if variable is None:
        return True
    if not isinstance(variable, np.ndarray):
        return False
    return (required_dtype is None) or (variable.dtype == required_dtype)


def triangulate_polygons(polygon_vertex_indices: List[List[int]]) -> np.ndarray:
    n_all_vertices_in_polygons = 0
    for polygon in polygon_vertex_indices:
        n_vertices = len(polygon)
        assert n_vertices >= 3
        n_all_vertices_in_polygons += n_vertices - 2

    res = np.zeros((n_all_vertices_in_polygons, 3), dtype=np.int32)
    counter = 0
    for polygon in polygon_vertex_indices:
        n_vertices = len(polygon)
        assert n_vertices >= 3
        for i in range(n_vertices - 2):
            res[counter] = [polygon[0], polygon[i + 1], polygon[i + 2]]
            counter += 1

    return res


def center_of_vertices(vertices: np.ndarray) -> np.ndarray:
    assert vertices.ndim == 2
    assert vertices.shape[0] > 0
    return vertices.mean(axis=0)


def center_of_vertices_weighted(vertices: np.ndarray, weights: np.ndarray) -> np.ndarray:
    assert vertices.ndim == 2
    assert vertices.shape[0] > 0
    assert weights.ndim == 1
    assert vertices.shape[0] == weights.shape[0]
    sum_of_weights = weights.sum()
    if sum_of_weights == 0.0:
        sum_of_weights = 1.0
    return (vertices * weights[:, None]).sum(axis=0) / sum_of_weights
