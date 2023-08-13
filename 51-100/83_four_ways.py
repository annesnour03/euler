import time
from queue import PriorityQueue
from pprint import pprint
import numpy as np


class Graph:
    def __init__(self, num_of_vertices, grid):
        self.v = num_of_vertices
        self.edges = []
        self.visited = []
        self.original_grid = grid
        self.width, self.height = len(
            self.original_grid[0]), len(self.original_grid)

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

    def get_right_column_indexes(self):
        return [self.width * i + self.width - 1 for i in range(self.height)]

    def get_left_column_indexes(self):
        return [self.width * i for i in range(self.height)]


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def generate_adjacency_matrix(weights_matrix):
    height, width = weights_matrix.shape
    num_vertices = height * width
    adjacency_matrix = np.zeros((num_vertices, num_vertices))

    def get_index(row, col):
        return col + row * width

    for row in range(height):
        for col in range(width):
            # Move left, but not in the first row!
            if col > 1:
                left_weight = weights_matrix[row, col - 1]
                adjacency_matrix[get_index(row, col)][get_index(
                    row, col - 1)] = left_weight

            if row > 0:
                top_weight = weights_matrix[row - 1, col]
                adjacency_matrix[get_index(row, col)][get_index(
                    row - 1, col)] = top_weight

            # Move down
            if row < height - 1:
                bottom_weight = weights_matrix[row + 1, col]
                adjacency_matrix[get_index(row, col)][get_index(
                    row + 1, col)] = bottom_weight

            # Move right
            if col < width - 1:
                right_weight = weights_matrix[row, col + 1]
                adjacency_matrix[get_index(row, col)][get_index(
                    row, col + 1)] = right_weight
    adjacency_matrix[adjacency_matrix == 0] = -1
    return adjacency_matrix


def solve(grid):
    height, width = grid.shape[:2]
    g = Graph(height * width, grid)
    g.original_grid = grid
    g.edges = generate_adjacency_matrix(grid)
    result = dijkstra(g, 0)
    return result[g.v - 1]


def main():
    t0 = time.time()
    lines = np.genfromtxt('81_input.txt', delimiter=',', dtype=int)
    dim = lines.shape[:2][0]
    lines = np.column_stack([np.zeros((dim, 1)), lines])
    pprint(solve(lines))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
