# pygeom_tools
[WIP] Simple tools for wavefront obj loading.

It's pretty dirty and slow. No obj file validation. Also it supports only vertices, uv and basic topology. Normals, polygroups, materials, etc, will be ignored 

# Example

```python
import geom_tools
path_to_obj = "models/teapot.obj"
model = geom_tools.from_obj_file(path_to_obj)
# Print various statistics 
print(f"Model loaded, "
      f"n vertices: {model.n_vertices()}, "
      f"n vts: {model.n_texture_vertices()}, "
      f"n polygons: {model.n_polygons()}, "
      f"n triangles: {model.n_triangles()}")
# or simply
geom_tools.summary(model)
print(model.vertices[:5])  # NumPy array, same for texture vertices, etc
print(model.polygon_vertex_indices[:5])  # List of lists, same for texture topology, triangulated topology, etc
print(model.triangle_vertex_indices[:5])  # Fan like triangulation of topology. Keep original triangles

model.vertices[0] = (1, 2, 3)
geom_tools.save(model, "res.obj")    
```

See `geom_tools.mesh.Mesh` for more details. For saving stuff see `export_vertices_by_existing_obj`, `export_vertices_by_existing_obj_stream`

# Installation

```
pip3 install git+https://github.com/Daiver/pygeom_tools
```

# Features
## Bounding box

```python
import numpy as np
from geom_tools import Mesh
mesh = Mesh(
    vertices=np.array([[0, 1, 2], [1, 1, 2], [-5, 2, 3]]), polygon_vertex_indices=[[0, 1, 2]])
print(mesh.bbox())
# prints: BoundingBox([-5, 1, 2], [1, 2, 3])
```
