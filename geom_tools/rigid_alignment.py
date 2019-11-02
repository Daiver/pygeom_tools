from typing import Union, List, Tuple
import numpy as np

from .utils import center_of_vertices
from .transformations import translated


def rigid_alignment_transformation(
        src: Union[List[List[float]], np.ndarray],
        dst: Union[List[List[float]], np.ndarray]
) -> Tuple[np.ndarray, np.ndarray]:
    src = np.array(src)
    dst = np.array(dst)
    assert src.ndim == 2
    assert src.shape == dst.shape
    src_center = center_of_vertices(src)
    dst_center = center_of_vertices(dst)

    src_centered = translated(src_center, src)
    dst_centered = translated(dst_center, dst)
    cov_mat = src_centered.T @ dst_centered

    rotation = rot_mat_from_cov_mat(cov_mat)
    translation = dst_center - rotation @ src_center
    return rotation, translation


def rot_mat_from_cov_mat(cov_mat: np.ndarray) -> np.ndarray:
    u, s, v = np.linalg.svd(cov_mat)
    d = np.linalg.det(v.T @ u.T)
    sigma = np.eye(cov_mat.shape[0])
    sigma[-1, -1] = d
    return v.T @ sigma @ u.T


