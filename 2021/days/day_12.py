from typing import Dict, List

from days.inputreader import day, day_input


def add_node_edge(graph, _from: str, _to: str) -> Dict[str, str]:
    if _from in graph:
        graph[_from].append(_to)
    else:
        graph[_from] = [_to]
    return graph


def content_to_graph(content: List[str]) -> Dict[str, str]:
    graph = {}
    for line in content:
        _from, _to = line.strip().split('-')
        graph = add_node_edge(graph, _from, _to)
        if _from != 'start' and _to != 'end':
            graph = add_node_edge(graph, _to, _from)

    return graph


def depth_first_search(data, path, paths=[]):
    node = path[-1]
    if node in data:
        for val in data[node]:
            # no visiting a small cave twice
            if val.islower() and val in path:
                continue
            new_path = path + [val]
            paths = depth_first_search(data, new_path, paths)
    else:
        if node != 'end':
            # no backtracking to start or a small cave
            if path[-2] != 'start' and not path[-2].islower():
                new_path = path + [path[-2]]  # backtrack
                paths = depth_first_search(data, new_path, paths)
        else:
            paths += [path]  # stop

    return paths


def nr_of_paths(graph: Dict[str, str]) -> int:
    return len(depth_first_search(graph, ['start'], []))


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')

    graph = content_to_graph(content)
    part1 = nr_of_paths(graph)

    print(part1)
    # print(part2)
