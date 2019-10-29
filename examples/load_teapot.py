import cv2
import numpy as np

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

    canvas_size = (300, 250)
    fit_to_view_transformation = geom_tools.fit_to_view_transform(
        bbox=model.bbox(),
        canvas_size=canvas_size
    )
    vertices = geom_tools.transform_vertices(fit_to_view_transformation, model.vertices)
    canvas = np.zeros((canvas_size[1], canvas_size[0], 3), dtype=np.uint8)
    for v in vertices.round().astype(np.int32):
        cv2.circle(canvas, (v[0], v[1]), 1, (0, 200, 0), -1)
    cv2.imshow("", canvas)
    cv2.waitKey()


if __name__ == '__main__':
    main()
