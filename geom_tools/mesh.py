import numpy as np

from .utils import is_arrays_equal
from .bounding_box import from_vertices, BoundingBox


# TODO: asserts for consistent texture information
class Mesh:
    def __init__(self,
                 vertices: np.ndarray,
                 polygon_vertex_indices: list,
                 texture_vertices: np.ndarray = None,
                 texture_polygon_vertex_indices: list = None,
                 normals: np.ndarray = None,
                 triangle_vertex_indices: list = None,
                 triangle_texture_vertex_indices: list = None):
        self.vertices = vertices
        self.polygon_vertex_indices = polygon_vertex_indices
        self.texture_vertices = texture_vertices
        self.texture_polygon_vertex_indices = texture_polygon_vertex_indices
        self.normals = normals
        self.triangle_vertex_indices = triangle_vertex_indices
        self.triangle_texture_vertex_indices = triangle_texture_vertex_indices

    def n_vertices(self) -> int:
        return len(self.vertices)

    def n_texture_vertices(self) -> int:
        if self.has_uv():
            return len(self.texture_vertices)
        return 0

    def n_polygons(self) -> int:
        return len(self.polygon_vertex_indices)

    def n_triangles(self):
        if self.has_triangulated():
            return len(self.triangle_vertex_indices)
        else:
            return None

    def has_uv(self) -> bool:
        return self.texture_vertices is not None

    def has_normals(self) -> bool:
        return self.normals is not None

    def has_triangulated(self) -> bool:
        return self.triangle_vertex_indices is not None

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

        if self.triangle_vertex_indices != other.triangle_vertex_indices:
            return False
        if self.triangle_texture_vertex_indices != other.triangle_texture_vertex_indices:
            return False

        return True

    def bbox(self) -> BoundingBox:
        return from_vertices(self.vertices)
