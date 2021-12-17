from collections import Counter
from typing import Dict, List

from days.inputreader import day, day_input


def add_node_edge(graph: Dict[str, str], _from: str,
                  _to: str) -> Dict[str, str]:
    if _from == 'end' or _to == 'start':
        return graph

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
        graph = add_node_edge(graph, _to, _from)

    return graph


def depth_first_search(data: Dict[str, str], path: List[str], paths: List[str],
                       revisit: bool) -> List[List[str]]:
    node = path[-1]
    if node in data:
        for val in data[node]:

            if val.islower() and val in path:
                if revisit:
                    small_caves_count = Counter([
                        p for p in path
                        if p.islower() and p not in ['start', 'end']
                    ])
                    # visit at most one small cave twice
                    if sum(small_caves_count.values()) > len(small_caves_count):
                        continue
                # no visiting a small cave twice
                else:
                    continue
            new_path = path + [val]
            paths = depth_first_search(data, new_path, paths, revisit)
    else:  # 'end'
        paths += [path]

    return paths


def nr_of_paths(graph: Dict[str, str], revisit: bool) -> int:
    return len(depth_first_search(graph, ['start'], [], revisit))


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')

    graph = content_to_graph(content)
    part1 = nr_of_paths(graph, False)
    part2 = nr_of_paths(graph, True)

    print(part1)
    print(part2)
