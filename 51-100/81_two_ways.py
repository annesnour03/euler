import time
from queue import PriorityQueue
from pprint import pprint
import numpy as np


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(30)]
                      for j in range(30)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight


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
            if row < height - 1:
                bottom_weight = weights_matrix[row + 1, col]
                adjacency_matrix[get_index(row, col)][get_index(
                    row + 1, col)] = bottom_weight
            if col < width - 1:
                right_weight = weights_matrix[row, col + 1]
                adjacency_matrix[get_index(row, col)][get_index(
                    row, col + 1)] = right_weight
    adjacency_matrix[adjacency_matrix == 0] = -1
    return adjacency_matrix


def solve(grid):
    height, width = grid.shape[:2]
    g = Graph(height * width)
    g.edges = generate_adjacency_matrix(grid)
    return dijkstra(g, 0)[g.v - 1]


def main():
    t0 = time.time()
    lines = np.array([])
    with open("81_input.txt") as f:
        for line in f:
            lines = np.append(lines, np.array(
                [list(map(int, line.split(",")))]))
    dim = int(np.sqrt(lines.shape[0]))
    print(lines.shape)
    lines = lines.reshape(dim, -1)
    lines = np.vstack([np.zeros((dim)), lines])
    print(solve(lines))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
