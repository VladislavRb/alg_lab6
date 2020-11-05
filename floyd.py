import numpy as np


class FloydPathFinder:
    def __init__(self, matrix: list):
        self.n = len(matrix)
        [self.floyd_matrix, self.path_matrix] = self.__form_floyd_and_path_matrix(np.array(matrix))

    def __form_floyd_and_path_matrix(self, floyd_matrix: np.ndarray):
        path_matrix = np.array([[i for i in range(self.n)] for j in range(self.n)])

        index_array = [i for i in range(self.n)]

        for i in range(self.n):
            indexes_without_i = list(filter(lambda ind: not ind == i, index_array))

            for row_ind in indexes_without_i:
                for col_ind in indexes_without_i:
                    new_path = floyd_matrix[row_ind, i] + floyd_matrix[i, col_ind]

                    if new_path < floyd_matrix[row_ind, col_ind]:
                        floyd_matrix[row_ind, col_ind] = new_path
                        path_matrix[row_ind, col_ind] = path_matrix[row_ind, i]

        return floyd_matrix, path_matrix

    def __extend_step(self, step: list):
        intermediate_vertex_index = self.path_matrix[step[0], step[1]]

        return [[step[0], intermediate_vertex_index], [intermediate_vertex_index, step[1]]]

    def __form_path(self, path: list):
        to_update = False

        for i in range(len(path)):
            step = path[i]

            if not self.path_matrix[step[0], step[1]] == step[1]:
                path[i:(i+1)] = self.__extend_step(step)

                to_update = True

        if to_update:
            return self.__form_path(path)

        return path

    def path_from_to(self, start_vertex_index: int, end_vertex_index: int):
        path = self.__form_path([[start_vertex_index, end_vertex_index]])

        return [step[0] for step in path] + [end_vertex_index]

    def path_length_from_to(self, start_vertex_index: int, end_vertex_index: int):
        return self.floyd_matrix[start_vertex_index, end_vertex_index]

    def distance_to_farthest_vertex_for(self, vertex_index: int):
        other_vertex_indexes = list(filter(lambda ind: not ind == vertex_index, [i for i in range(self.n)]))

        return max([self.path_length_from_to(vertex_index, other_index) for other_index in other_vertex_indexes])

    def optimal_vertex_index(self):
        farthest_distances = [self.distance_to_farthest_vertex_for(i) for i in range(self.n)]

        return farthest_distances.index(min(farthest_distances))
