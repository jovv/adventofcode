from days.day_14 import parse_content, polymer_count

sample_content = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C',
]

expected_template = 'NNCB'
expected_pairs = {
    'CH': 'B',
    'HH': 'N',
    'CB': 'H',
    'NH': 'C',
    'HB': 'C',
    'HC': 'B',
    'HN': 'C',
    'NN': 'C',
    'BH': 'H',
    'NC': 'B',
    'NB': 'B',
    'BN': 'B',
    'BB': 'N',
    'BC': 'B',
    'CC': 'N',
    'CN': 'C',
}


def test_parse_content():

    template, pairs = parse_content(sample_content)
    assert template == expected_template
    assert pairs == expected_pairs


def test_small():

    assert polymer_count(expected_template, expected_pairs, 10) == 1588


def test_large():

    assert polymer_count(expected_template, expected_pairs, 40) == 2188189693529
