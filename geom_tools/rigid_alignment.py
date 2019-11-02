from typing import Union, List
import numpy as np

from .transformations import translated


def rigid_alignment_transformation(
        src: Union[List[List[float]], np.ndarray],
        dst: Union[List[List[float]], np.ndarray]
) -> np.ndarray:
    src = np.array(src)
    dst = np.array(dst)
    raise NotImplementedError()


def rot_mat_from_cov_mat(cov_mat: np.ndarray) -> np.ndarray:
    u, s, v = np.linalg.svd(cov_mat)
    d = np.linalg.det(v @ u.T)
    sigma = np.eye(cov_mat.shape[0])
    sigma[-1, -1] = d
    return v @ sigma @ u.T


