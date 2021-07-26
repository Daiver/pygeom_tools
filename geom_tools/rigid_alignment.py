from typing import Tuple
import numpy as np

from .utils import center_of_vertices, center_of_vertices_weighted
from .transformations import translated


def find_rotation_and_translation(src: np.ndarray, dst: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    assert src.ndim == 2
    assert src.shape == dst.shape
    src_center = center_of_vertices(src)
    dst_center = center_of_vertices(dst)

    src_centered = translated(-src_center, src)
    dst_centered = translated(-dst_center, dst)
    cov_mat = cov_mat_from_vertices(src_centered, dst_centered)

    rotation = rot_mat_from_cov_mat(cov_mat)
    translation = dst_center - rotation @ src_center
    return rotation, translation


def find_rotation_and_translation_weighted(
        src: np.ndarray,
        dst: np.ndarray,
        weights: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    assert src.ndim == 2
    assert src.shape == dst.shape
    assert weights.ndim == 1 and weights.shape[0] == src.shape[0]
    src_center = center_of_vertices_weighted(src, weights)
    dst_center = center_of_vertices_weighted(dst, weights)

    src_centered = translated(-src_center, src)
    dst_centered = translated(-dst_center, dst)
    cov_mat = cov_mat_from_vertices_weighted(src_centered, dst_centered, weights)

    rotation = rot_mat_from_cov_mat(cov_mat)
    translation = dst_center - rotation @ src_center
    return rotation, translation


def cov_mat_from_vertices(src: np.ndarray, dst: np.ndarray) -> np.ndarray:
    return src.T @ dst


def cov_mat_from_vertices_weighted(src: np.ndarray, dst: np.ndarray, weights_vec: np.ndarray) -> np.ndarray:
    assert weights_vec.ndim == 1
    assert weights_vec.shape[0] == src.shape[0]
    tmp = src * weights_vec[:, None]
    return tmp.T @ dst


def rot_mat_from_cov_mat(cov_mat: np.ndarray) -> np.ndarray:
    u, s, v = np.linalg.svd(cov_mat)
    d = np.linalg.det(v.T @ u.T)
    sigma = np.eye(cov_mat.shape[0])
    sigma[-1, -1] = d
    return v.T @ sigma @ u.T
