import os
import io
import numpy as np
from .mesh import Mesh


def save(mesh: Mesh, path: str, save_normals=False):
    with open(path, "w") as f:
        save_to_stream(mesh, f, save_normals=save_normals)


def save_to_stream(mesh: Mesh, stream: io.TextIOWrapper, save_normals=False):
    assert not save_normals
    _write_vertices(mesh.vertices, stream)
    stream.write("\n")
    if mesh.has_uv():
        _write_texture_vertices(mesh.texture_vertices, stream)
        stream.write("\n")
    _write_faces(mesh.polygon_vertex_indices, mesh.texture_polygon_vertex_indices, stream)


def _write_vertices(vertices, stream: io.TextIOWrapper):
    for v in vertices:
        stream.write("v {0} {1} {2}\n".format(v[0], v[1], v[2]))


def _write_texture_vertices(texture_vertices, stream: io.TextIOWrapper):
    for v in texture_vertices:
        stream.write("vt {0} {1}\n".format(v[0], v[1]))


def _write_faces(polygon_vertex_indices, texture_polygon_vertex_indices, stream: io.TextIOWrapper):
    has_uv = texture_polygon_vertex_indices is not None
    n_faces = len(polygon_vertex_indices)

    if has_uv:
        assert n_faces == len(texture_polygon_vertex_indices)
        for v_face, t_face in zip(polygon_vertex_indices, texture_polygon_vertex_indices):
            line = " ".join("{0}/{1}".format(v_ind + 1, t_ind + 1) for v_ind, t_ind in zip(v_face, t_face))
            stream.write("f {0}\n".format(line))
    else:
        for v_face in polygon_vertex_indices:
            line = " ".join(str(v_ind + 1) for v_ind in v_face)
            stream.write("f {0}\n".format(line))


def export_vertices_by_existing_obj(vertices: np.ndarray, src_path: str, dst_path: str):
    assert os.path.exists(src_path)
    with open(src_path) as inp:
        with open(dst_path, "w") as out:
            export_vertices_by_existing_obj_stream(vertices, inp, out)


def export_vertices_by_existing_obj_stream(
        vertices: np.ndarray,
        src_stream: io.TextIOWrapper,
        dst_stream: io.TextIOWrapper):
    v_ind = 0
    for line in src_stream:
        if line[0:2] == "v ":
            assert v_ind < len(vertices)
            dst_stream.write("v {0} {1} {2}\n".format(vertices[v_ind, 0], vertices[v_ind, 1], vertices[v_ind, 2]))
            v_ind += 1
        else:
            dst_stream.write(line)
