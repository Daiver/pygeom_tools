from typing import List, Tuple, Union
import numpy as np

from .bounding_box import BoundingBox


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


def rotated(
        rotation_matrix: Union[List[List[float]], np.ndarray],
        vertices: Union[List[List[float]], np.ndarray]
) -> np.ndarray:
    return rotated_and_translated(rotation_matrix=rotation_matrix, translation=[0, 0, 0], vertices=vertices)


def rotation_around_vertex(
        rotation_matrix: Union[List[List[float]], np.ndarray],
        rotation_center: Union[List[float], np.ndarray],
        translation: Union[List[float], np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    rotation_matrix = np.array(rotation_matrix, dtype=np.float32)
    rotation_center = np.array(rotation_center, dtype=np.float32)
    if translation is None:
        translation = np.zeros((3,), dtype=np.float32)
    translation = np.array(translation, dtype=np.float32)

    assert rotation_matrix.ndim == 2 and rotation_matrix.shape == (3, 3)
    assert rotation_center.ndim == 1 and rotation_center.shape[0] == 3
    assert translation.ndim == 1 and translation.shape[0] == 3

    return rotation_matrix, -rotation_matrix @ rotation_center + rotation_center + translation


def fit_to_view_transform(bbox: BoundingBox, canvas_size: (int, int)) -> (np.ndarray, np.ndarray):
    """
    Untested, fit vertices to z aligned ortho camera box
    :param bbox:
    :param canvas_size:
    :return:
    """
    center = bbox.center()
    size = bbox.size()
    scale = np.min(canvas_size) / size[:2].max()

    mat = np.array([
        [scale, 0, 0],
        [0, -scale, 0],
        [0, 0, scale],
    ], dtype=np.float32)
    trans = -mat @ center + [canvas_size[0] / 2.0, canvas_size[1] / 2.0, 0]

    return mat, trans


def translated(
        translation: Union[List[List[float]], np.ndarray],
        vertices: Union[List[List[float]], np.ndarray]
) -> np.ndarray:
    translation = np.array(translation)
    vertices = np.array(vertices)
    return vertices[:] + translation
