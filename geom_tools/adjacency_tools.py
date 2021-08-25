from typing import List, Optional


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


def expand_adjacency_table(adjacency_table: List[List[int]]) -> List[List[int]]:
    res = []
    for vertex_ind, vertex_adj_list in enumerate(adjacency_table):
        res_set = set(vertex_adj_list)
        for other_vertex_ind in vertex_adj_list:
            res_set.update(adjacency_table[other_vertex_ind])
        res_set.remove(vertex_ind)
        res_list = sorted(res_set)
        res.append(res_list)
    return res
