import numpy as np
from .utils import is_arrays_equal


class BoundingBox:
    def __init__(self, smallest_corner, biggest_corner):
        smallest_corner = np.array(smallest_corner, dtype=np.float32)
        biggest_corner = np.array(biggest_corner, dtype=np.float32)
        assert smallest_corner.shape == (3,)
        assert biggest_corner.shape == (3,)
        self._smallest_corner = smallest_corner
        self._biggest_corner = biggest_corner

    def __eq__(self, other) -> bool:
        assert isinstance(other, BoundingBox)
        return (is_arrays_equal(self._smallest_corner, other._smallest_corner) and
                is_arrays_equal(self._biggest_corner, other._biggest_corner))

    def __repr__(self) -> str:
        return "BoundingBox([{}, {}, {}], [{}, {}, {}])".format(
            self._smallest_corner[0], self._smallest_corner[1], self._smallest_corner[2],
            self._biggest_corner[0], self._biggest_corner[1], self._biggest_corner[2]
        )

    def smallest_corner(self):
        return self._smallest_corner

    def biggest_corner(self):
        return self._biggest_corner


def from_vertices(vertices):
    vertices = np.array(vertices, dtype=np.float32)
    assert vertices.ndim == 2
    assert vertices.shape[1] == 3

    smallest_corner = vertices.min(axis=0)
    biggest_corner = vertices.max(axis=0)

    return BoundingBox(smallest_corner=smallest_corner, biggest_corner=biggest_corner)
