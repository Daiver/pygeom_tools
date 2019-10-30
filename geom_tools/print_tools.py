from .mesh import Mesh


def summary(model: Mesh) -> str:
    return \
        "Model info:, " \
        "n vertices: {0}, " \
        "n vts: {1}, " \
        "n polygons: {2}, " \
        "n triangles: {3}".format(
            model.n_vertices(),
            model.n_texture_vertices(),
            model.n_polygons(),
            model.n_triangles()
        )
