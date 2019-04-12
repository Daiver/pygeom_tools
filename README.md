# pygeom_tools
[WIP] Simple tools for wavefront obj loading.

It's pretty dirty and slow. Also it supports only vertices, uv and basic topology. Normals, polygroups, materials, etc, will be ignored 

# Example

```python

    path_to_obj = "models/teapot.obj"
    model = geom_tools.from_obj_file(path_to_obj)
    print(f"Model loaded, n vertices: {model.n_vertices()}")
```

# Installation

```
pip3 install git+https://github.com/Daiver/pygeom_tools
```