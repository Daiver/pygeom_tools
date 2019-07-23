from .mesh import Mesh


def summary(model: Mesh):
    print(f"Model loaded, "
          f"n vertices: {model.n_vertices()}, "
          f"n vts: {model.n_texture_vertices()}, "
          f"n polygons: {model.n_polygons()}, "
          f"n triangles: {model.n_triangles()}")
