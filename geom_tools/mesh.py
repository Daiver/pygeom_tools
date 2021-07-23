from typing import Optional, List
import copy
import numpy as np

from .utils import is_arrays_equal, is_arrays_equal_or_both_none, triangulate_polygons
from .bounding_box import from_vertices, BoundingBox
from .normals_tools import compute_vertices_normals_from_triangles


# TODO: asserts for consistent texture information
class Mesh:
    def __init__(
            self,
            vertices: np.ndarray,
            polygon_vertex_indices: List[List[int]],
            texture_vertices: Optional[np.ndarray] = None,
            texture_polygon_vertex_indices: Optional[List[List[int]]] = None,
            normals: Optional[np.ndarray] = None,
            triangle_vertex_indices: Optional[np.ndarray] = None,
            triangle_texture_vertex_indices: Optional[np.ndarray] = None,
            polygon_groups: Optional[List[int]] = None,
            group_names: Optional[List[str]] = None
    ):
        self.vertices = vertices
        self.polygon_vertex_indices = polygon_vertex_indices
        self.texture_vertices = texture_vertices
        self.texture_polygon_vertex_indices = texture_polygon_vertex_indices
        self.normals = normals

        if triangle_vertex_indices is not None:
            triangle_vertex_indices = np.array(triangle_vertex_indices, dtype=np.int32)
            assert triangle_vertex_indices.ndim == 2 and triangle_vertex_indices.shape[1] == 3
        if triangle_texture_vertex_indices is not None:
            triangle_texture_vertex_indices = np.array(triangle_texture_vertex_indices, dtype=np.int32)
            assert triangle_texture_vertex_indices.ndim == 2 and triangle_texture_vertex_indices.shape[1] == 3
        self.triangle_vertex_indices = triangle_vertex_indices
        self.triangle_texture_vertex_indices = triangle_texture_vertex_indices

        if polygon_groups is None:
            polygon_groups = [-1] * len(polygon_vertex_indices)
        assert len(polygon_vertex_indices) == len(polygon_groups)
        self.polygon_groups = polygon_groups
        self.group_names = group_names

    def n_vertices(self) -> int:
        return len(self.vertices)

    def n_texture_vertices(self) -> int:
        return len(self.texture_vertices) if self.has_uv() else 0

    def n_polygons(self) -> int:
        return len(self.polygon_vertex_indices)

    def n_triangles(self) -> Optional[int]:
        return len(self.triangle_vertex_indices) if self.is_triangulated() else None

    def has_uv(self) -> bool:
        return self.texture_vertices is not None

    def has_normals(self) -> bool:
        return self.normals is not None

    def is_triangulated(self) -> bool:
        return self.triangle_vertex_indices is not None

    def n_groups(self) -> int:
        return len(self.group_names) if self.group_names is not None else 0

    def __eq__(self, other) -> bool:
        assert isinstance(other, Mesh)

        if not is_arrays_equal(self.vertices, other.vertices):
            return False
        if not self.polygon_vertex_indices == other.polygon_vertex_indices:
            return False

        if self.has_uv() != other.has_uv():
            return False
        if self.has_uv():
            if not is_arrays_equal(self.texture_vertices, other.texture_vertices):
                return False
            if not self.texture_polygon_vertex_indices == other.texture_polygon_vertex_indices:
                return False

        if self.has_normals() != other.has_normals():
            return False
        if self.has_normals():
            if not is_arrays_equal(self.normals, other.normals):
                return False

        if not is_arrays_equal_or_both_none(self.triangle_vertex_indices, other.triangle_vertex_indices):
            return False
        if not is_arrays_equal_or_both_none(
                self.triangle_texture_vertex_indices, other.triangle_texture_vertex_indices
        ):
            return False

        is_groups_equals = self.polygon_groups == other.polygon_groups and self.group_names == other.group_names
        if not is_groups_equals:
            return False

        return True

    def summary(self) -> str:
        return \
            "Geom info: " \
            "n vertices: {0}, " \
            "n vts: {1}, " \
            "n polygons: {2}, " \
            "n triangles: {3}, " \
            "n groups {4}".format(
                self.n_vertices(),
                self.n_texture_vertices(),
                self.n_polygons(),
                self.n_triangles(),
                self.n_groups()
            )

    def bbox(self) -> BoundingBox:
        return from_vertices(self.vertices)

    def clone(self) -> "Mesh":
        return copy.deepcopy(self)

    def set_vertices_and_compute_normals(self, vertices: np.ndarray):
        assert self.is_triangulated()
        assert vertices.ndim == 2
        assert vertices.shape == self.vertices.shape
        self.vertices = vertices
        self.normals = compute_vertices_normals_from_triangles(self.vertices, self.triangle_vertex_indices)
        return self
