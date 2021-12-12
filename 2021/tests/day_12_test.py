from days.day_12 import content_to_graph, nr_of_paths, add_node_edge

sample_content = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

sample_graph = {
    'start': ['A', 'b'],
    'A': ['c', 'b', 'end'],
    'b': ['A', 'd', 'end'],
    'c': ['A'],
    'd': ['b'],
}


def test_content_to_graph():

    assert content_to_graph(sample_content) == sample_graph


def test_nr_of_paths():

    assert nr_of_paths(sample_graph) == 10


def test_node_edge():
    testcases = [('start', 'A', {
        'start': ['A']
    }), ('start', 'b', {
        'start': ['b']
    }), ('A', 'end', {
        'A': ['end']
    }), ('b', 'end', {
        'b': ['end']
    }), ('A', 'c', {
        'A': ['c']
    })]

    for test in testcases:

        _from, _to, expected = test
        assert add_node_edge({}, _from, _to) == expected
