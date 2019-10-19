from typing import List, Tuple, Union
import numpy as np


def rotated_and_translated(
        rotation_matrix: Union[List[List[float]], np.ndarray],
        translation: Union[List[float], np.ndarray],
        vertices: Union[List[List[float]], np.ndarray]
) -> np.ndarray:
    """
    Applyes 3x3 transformation matrix and translation vector
    :param rotation_matrix: 3x3 matrix, can be not a rotation matrix, btw
    :param translation:
    :param vertices:
    :return: vertices @ rotation_matrix.T + translation
    """
    rotation_matrix = np.array(rotation_matrix, dtype=np.float32)
    translation = np.array(translation, dtype=np.float32)
    vertices = np.array(vertices, dtype=np.float32)
    assert rotation_matrix.ndim == 2 and rotation_matrix.shape == (3, 3)
    assert translation.ndim == 1 and translation.shape[0] == 3
    assert vertices.ndim == 2 and vertices.shape[1] == 3
    return vertices @ rotation_matrix.T + translation


def transform_vertices(
        transformation: Tuple[
            Union[List[List[float]], np.ndarray],
            Union[List[float], np.ndarray],
        ],
        vertices: Union[List[List[float]], np.ndarray]
) -> np.ndarray:
    return rotated_and_translated(transformation[0], transformation[1], vertices)


def rotation_around_vertex(
        rotation: Union[List[List[float]], np.ndarray],
        rotation_center: Union[List[float], np.ndarray],
        additional_translation: Union[List[float], np.ndarray],
) -> np.ndarray:
    raise NotImplementedError
    pass
