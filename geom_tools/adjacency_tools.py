from typing import List, Optional
import numpy as np


# TODO: separate (crs?) structure for table storage
# TODO: terrible performance, can be improved
def vertices_adjacency_from_polygon_vertex_indices(
        polygon_vertex_indices: List[List[int]],
        n_vertices: Optional[int] = None
) -> List[List[int]]:
    if n_vertices is None:
        n_vertices = 1 + max_vertex_ind_in_list(polygon_vertex_indices)
    res_sets = [set() for _ in range(n_vertices)]

    for polygon in polygon_vertex_indices:
        for i, index1 in enumerate(polygon):
            index2 = polygon[(i - 1) % len(polygon)]
            index3 = polygon[(i + 1) % len(polygon)]
            res_sets[index1].add(index2)
            res_sets[index1].add(index3)
    res = [
        sorted(list(x))
        for x in res_sets
    ]
    return res


def max_vertex_ind_in_list(indices: List[List[int]]) -> int:
    flat_indices_generator = (item for sublist in indices for item in sublist)
    return max(flat_indices_generator)
