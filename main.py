from floyd import FloydPathFinder
from math import inf


matrix = [
    [inf, inf, 6, inf, 3],
    [4, inf, inf, 2, 1],
    [inf, 5, inf, inf, 8],
    [inf, -1, 7, inf, -3],
    [inf, inf, 8, 4, inf]]

pfdr = FloydPathFinder(matrix)
optimal_vertex_index = pfdr.optimal_vertex_index()

print("optimal vertex index:", optimal_vertex_index)
print("distance to farthest vertex:", pfdr.distance_to_farthest_vertex_for(optimal_vertex_index))
