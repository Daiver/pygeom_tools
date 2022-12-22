from collections import OrderedDict
import numpy as np
from .mesh import Mesh
from .utils import triangulate_polygons
from .normals_tools import compute_vertices_normals_from_triangles

from . import obj_import_cpp


# Just for simplicity
def load(file_name, triangulate=True, compute_normals=True) -> Mesh:
    return from_obj_file(file_name=file_name, triangulate=triangulate, compute_normals=compute_normals)


def load_vertices(file_name: str) -> np.ndarray:
    return from_obj_file_vertices(file_name=file_name)


def from_obj_file_vertices(file_name: str) -> np.ndarray:
    with open(file_name) as f:
        string = f.read()
        return from_obj_string_vertices(string)


def from_obj_string_vertices(string: str) -> np.ndarray:
    flat_vertices = obj_import_cpp.read_flat_vertices_from_string(string)
    if flat_vertices is None:
        raise ValueError("Cannot read file")
    assert len(flat_vertices) % 3 == 0
    return np.array(flat_vertices, dtype=np.float32).reshape(-1, 3)


# Currently normals are not supported
# TODO: not effective, use file streams or something like this
def from_obj_file(file_name, triangulate=True, compute_normals=True):
    with open(file_name) as f:
        string = f.read()
        return from_obj_string(string, triangulate=triangulate, compute_normals=compute_normals)


# TODO: just ugly, split it to several functions, add assertions, etc
def from_obj_string(string, triangulate=True, compute_normals=True):
    lines = string.split("\n")
    vertices = []
    texture_vertices = []
    polygon_vertex_indices = []
    texture_polygon_vertex_indices = []

    group_names = OrderedDict()
    polygon_groups = []
    last_group_ind = -1

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue

        tokens = [x for x in line.split(" ") if len(x) > 0]

        if tokens[0] == "v":
            assert len(tokens) == 4
            vertices.append([float(x) for x in tokens[1:]])
        elif tokens[0] == "vt":
            assert len(tokens) in [3, 4]
            texture_vertices.append([float(x) for x in tokens[1:3]])
        elif tokens[0] == "f":
            assert len(tokens) >= 3
            vertex_face = []
            texture_face = []
            for token in tokens[1:]:
                is_token_contains_double_slash = "//" in token
                face_tokens = token.split("/")
                vertex_face.append(int(face_tokens[0]) - 1)
                if len(face_tokens) > 1 and not is_token_contains_double_slash:
                    texture_face.append(int(face_tokens[1]) - 1)
            polygon_vertex_indices.append(vertex_face)
            if len(texture_face) > 0:
                texture_polygon_vertex_indices.append(texture_face)
            polygon_groups.append(last_group_ind)
        elif tokens[0] == "g":
            if len(tokens) == 1:
                last_group_ind = -1
                continue
            group_name = tokens[1]
            if group_name not in group_names:
                group_names[group_name] = len(group_names)
            last_group_ind = group_names[group_name]

    vertices = np.array(vertices, dtype=np.float32)
    if len(texture_vertices) > 0:
        texture_vertices = np.array(texture_vertices, dtype=np.float32)
    else:
        texture_vertices = None
        texture_polygon_vertex_indices = None

    normals = None
    triangle_vertex_indices = None
    triangle_texture_vertex_indices = None

    if triangulate:
        triangle_vertex_indices = triangulate_polygons(polygon_vertex_indices)
        if texture_vertices is not None:
            triangle_texture_vertex_indices = triangulate_polygons(texture_polygon_vertex_indices)
        if compute_normals:
            normals = compute_vertices_normals_from_triangles(vertices, triangle_vertex_indices)

    group_names = list(group_names.keys()) if len(group_names) != 0 else None

    return Mesh(
        vertices=vertices,
        polygon_vertex_indices=polygon_vertex_indices,
        texture_vertices=texture_vertices,
        texture_polygon_vertex_indices=texture_polygon_vertex_indices,
        normals=normals,
        triangle_vertex_indices=triangle_vertex_indices,
        triangle_texture_vertex_indices=triangle_texture_vertex_indices,
        polygon_groups=polygon_groups,
        group_names=group_names,
    )
