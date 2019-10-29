import geom_tools


def main():
    path_to_obj = "models/teapot.obj"
    model = geom_tools.from_obj_file(path_to_obj)
    # Print various statistics
    print(f"Model loaded, "
          f"n vertices: {model.n_vertices()}, "
          f"n vts: {model.n_texture_vertices()}, "
          f"n polygons: {model.n_polygons()}, "
          f"n triangles: {model.n_triangles()}")
    # or simply
    print(geom_tools.summary(model))
    print(model.vertices[:5])  # NumPy array, same for texture vertices, etc
    print(model.polygon_vertex_indices[:5])  # List of lists, same for texture topology, triangulated topology, etc
    print(model.triangle_vertex_indices[:5])  # Fan like triangulation of topology. Keep original triangles


if __name__ == '__main__':
    main()
