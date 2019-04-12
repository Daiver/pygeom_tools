# pygeom_tools
[WIP] Simple tools for wavefront obj loading.

It's pretty dirty and slow. No obj file validation. Also it supports only vertices, uv and basic topology. Normals, polygroups, materials, etc, will be ignored 

# Example

```python
    path_to_obj = "models/teapot.obj"
    model = geom_tools.from_obj_file(path_to_obj)
    print(f"Model loaded, "
          f"n vertices: {model.n_vertices()}, "
          f"n vts: {model.n_texture_vertices()}, "
          f"n polygons: {model.n_polygons()}, "
          f"n triangles: {model.n_triangles()}")
    print(model.vertices[:5])  # NumPy array, same for texture vertices, etc
    print(model.polygon_vertex_indices[:5])  # List of lists, same for texture topology, triangulated topology, etc
    print(model.triangle_vertex_indices[:5])  # Fan like triangulation of topology. Keep original triangles

    model.vertices[0] = (1, 2, 3)
    geom_tools.save(model, "res.obj")    
```

Also see `export_vertices_by_existing_obj`, `export_vertices_by_existing_obj_stream`

# Installation

```
pip3 install git+https://github.com/Daiver/pygeom_tools
```
