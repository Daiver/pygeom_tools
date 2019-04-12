import io
import numpy as np
from .mesh import Mesh


def save(path: str, mesh: Mesh, save_normals=False):
    with open(path, "w") as f:
        save_to_stream(f, mesh, save_normals=save_normals)


def save_to_stream(stream: io.TextIOWrapper, mesh: Mesh, save_normals=False):
    assert not save_normals
    _write_vertices(mesh.vertices, stream)
    stream.write("\n")
    if mesh.has_uv():
        _write_texture_vertices(mesh.texture_vertices, stream)
        stream.write("\n")
    _write_faces(mesh.polygon_vertex_indices, mesh.texture_polygon_vertex_indices, stream)


def _write_vertices(vertices, stream: io.TextIOWrapper):
    for v in vertices:
        stream.write(f"v {v[0]} {v[1]} {v[2]}\n")


def _write_texture_vertices(texture_vertices, stream: io.TextIOWrapper):
    for v in texture_vertices:
        stream.write(f"vt {v[0]} {v[1]}\n")


def _write_faces(polygon_vertex_indices, texture_polygon_vertex_indices, stream: io.TextIOWrapper):
    has_uv = texture_polygon_vertex_indices is not None
    n_faces = len(polygon_vertex_indices)

    if has_uv:
        assert n_faces == len(texture_polygon_vertex_indices)
        for v_face, t_face in zip(polygon_vertex_indices, texture_polygon_vertex_indices):
            line = " ".join(f"{v_ind + 1}/{t_ind + 1}" for v_ind, t_ind in zip(v_face, t_face))
            stream.write(f"f {line}\n")
    else:
        for v_face in polygon_vertex_indices:
            line = " ".join(f"{v_ind + 1}" for v_ind in v_face)
            stream.write(f"f {line}\n")

