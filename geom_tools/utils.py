from typing import List, Union
import numpy as np


def is_arrays_equal(
        a: Union[List[float], List[List[float]], np.ndarray],
        b: Union[List[float], List[List[float]], np.ndarray]
):
    a = np.array(a)
    b = np.array(b)
    if a.shape != b.shape:
        return False
    return np.allclose(a, b)


def is_arrays_equal_or_both_none(
        a: Union[None, List[float], List[List[float]], np.ndarray],
        b: Union[None, List[float], List[List[float]], np.ndarray]
):
    if a is not None and b is not None:
        return is_arrays_equal(a, b)
    return (a is None) and (b is None)


def is_none_or_ndarray(variable: Union[None, np.ndarray], required_dtype: np.dtype = None) -> bool:
    if variable is None:
        return True
    if not isinstance(variable, np.ndarray):
        return False
    return (required_dtype is None) or (variable.dtype == required_dtype)


def triangulate_polygons(polygon_vertex_indices):
    res = []
    for polygon in polygon_vertex_indices:
        n_vertices = len(polygon)
        assert n_vertices >= 3
        for i in range(n_vertices - 2):
            res.append([polygon[0], polygon[i + 1], polygon[i + 2]])

    return res
