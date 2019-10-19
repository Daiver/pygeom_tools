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
print(geom_tools.summary(model))
print(model.vertices[:5])  # NumPy array, same for texture vertices, etc
print(model.polygon_vertex_indices[:5])  # List of lists, same for texture topology, triangulated topology, etc
print(model.triangle_vertex_indices[:5])  # Fan like triangulation of topology. Keep original triangles

model.vertices[0] = (1, 2, 3)
geom_tools.save(model, "res.obj")    
```

See `geom_tools.mesh.Mesh` for more details. For saving stuff see `export_vertices_by_existing_obj`, `export_vertices_by_existing_obj_stream`

# Installation

## Pip

```
pip3 install git+https://github.com/Daiver/pygeom_tools
```

## Manual
```
git clone https://github.com/Daiver/pygeom_tools
cd pygeom_tools
python3 setup.py install
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

## Vertices transformations

```python
import geom_tools
matrix = [
    [0, 1, 0],
    [1, 0, 0],
    [2, 0, 0]
]
vector = [2, 0, 3]

res = geom_tools.rotated_and_translated(
    rotation_matrix=matrix, translation=vector,
    vertices=[
        [0, 0, 0],
        [1, 0, 5],
    ]
)
print(res)    
# res = [
#     [2, 0, 3],
#     [2, 1, 5],
# ]

# Alternative syntax:
res = geom_tools.transform_vertices(
    (matrix, vector),
    vertices=[
        [0, 0, 0],
        [1, 0, 5],
    ]
)
```
