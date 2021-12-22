from collections import defaultdict
from typing import Dict, List, Set, Tuple

import numpy as np

from days.inputreader import day

INFINITY = float('inf')

Node = Tuple[int, int]
Graph = defaultdict[defaultdict[Node, int]]
GraphTravelCost = Dict[Node, int]


def initialize(matrix: np.ndarray) -> Tuple[Graph, Set[Node], GraphTravelCost]:

    graph = defaultdict(defaultdict)
    unvisited = set()
    costs = {}

    # create the graph, fill the unvisited set, assign tentative infinite risk levels
    for row, _ in enumerate(matrix):
        for col, _ in enumerate(matrix[row, :]):
            node = (row, col)
            unvisited.add(node)
            if row == 0 and col == 0:
                costs[node] = 0
            else:
                costs[node] = INFINITY
            # top left
            if row == 0 and col == 0:
                graph[node][(row + 1, col)] = matrix[row + 1, col]
                graph[node][(row, col + 1)] = matrix[row, col + 1]
            # bottom right
            elif row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                graph[node] = {}
            # bottom left
            elif row == len(matrix) - 1 and col == 0:
                graph[node][row - 1, col] = matrix[row - 1, col]
                graph[node][row, col + 1] = matrix[row, col + 1]
            # top right
            elif row == 0 and col == len(matrix[0]) - 1:
                graph[node][row, col - 1] = matrix[row, col - 1]
                graph[node][row + 1, col] = matrix[row + 1, col]
            # left edge
            elif col == 0:
                graph[node][row - 1, col] = matrix[row - 1, col]
                graph[node][row, col + 1] = matrix[row, col + 1]
                graph[node][row + 1, col] = matrix[row + 1, col]
            # right edge
            elif col == len(matrix[0]) - 1:
                graph[node][row - 1, col] = matrix[row - 1, col]
                graph[node][row, col - 1] = matrix[row, col - 1]
                graph[node][row + 1, col] = matrix[row + 1, col]
            # top edge
            elif row == 0:
                graph[node][row, col + 1] = matrix[row, col + 1]
                graph[node][row + 1, col] = matrix[row + 1, col]
                graph[node][row, col - 1] = matrix[row, col - 1]
            # botom edge
            elif row == len(matrix) - 1:
                graph[node][row, col + 1] = matrix[row, col + 1]
                graph[node][row - 1, col] = matrix[row - 1, col]
                graph[node][row, col - 1] = matrix[row, col - 1]
            # anywhere off the edges
            else:
                graph[node][row, col - 1] = matrix[row, col - 1]
                graph[node][row, col + 1] = matrix[row, col + 1]
                graph[node][row - 1, col] = matrix[row - 1, col]
                graph[node][row + 1, col] = matrix[row + 1, col]

    return graph, unvisited, costs


def lowest_cost_node(costs: GraphTravelCost, unvisited: Set[Node]):
    lowest_cost = INFINITY
    _lowest_cost_node = None
    for node in unvisited:
        if costs[node] < lowest_cost:
            lowest_cost = costs[node]
            _lowest_cost_node = node
    return _lowest_cost_node


# dijkstra
def shortest_path(
    graph: Graph,
    unvisited: Set[Node],
    costs: GraphTravelCost,
    initial_node: Node,
    destination_node: Node,
) -> int:
    current_node = initial_node
    while destination_node in unvisited:
        cost = costs[current_node]
        for neighbour_node, neighbour_cost in graph[current_node].items():
            new_cost = cost + neighbour_cost
            if costs[neighbour_node] > new_cost:
                costs[neighbour_node] = new_cost
        unvisited.remove(current_node)
        current_node = lowest_cost_node(costs, unvisited)

    return costs[destination_node]


if __name__ == '__main__':

    cavern = np.genfromtxt(
        f'{day(__file__)}_input.txt', delimiter=1, dtype=np.uint8)

    graph, unvisited, costs = initialize(cavern)
    initial_node = (0, 0)
    destination_node = (len(cavern) - 1, len(cavern[0]) - 1)
    part1 = shortest_path(
        graph=graph,
        unvisited=unvisited,
        costs=costs,
        initial_node=initial_node,
        destination_node=destination_node,
    )

    print(part1)
    # print(part2)
