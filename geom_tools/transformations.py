from typing import List, Union
import numpy as np


def transform_vertices(
        matrix: Union[List[List[float]], np.ndarray],
        vector: Union[List[float], np.ndarray],
        vertices: Union[List[List[float]], np.ndarray]
) -> np.ndarray:
    matrix = np.array(matrix, dtype=np.float32)
    vector = np.array(vector, dtype=np.float32)
    vertices = np.array(vertices, dtype=np.float32)
    assert matrix.ndim == 2 and matrix.shape == (3, 3)
    assert vector.ndim == 1 and vector.shape[0] == 3
    assert vertices.ndim == 2 and vertices.shape[1] == 3
    return vertices @ matrix.T + vector
