from days.day_8 import (easy_digits, entries, output_values, decode, sum_output)

content = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

lines = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
]
parsed_lines = [
    (
        [
            'be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd',
            'fecdb', 'fabcd', 'edb'
        ],
        ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'],
    ),
    (
        [
            'edbfga', 'begcd', 'cbg', 'gc', 'gcadebf', 'fbgde', 'acbgfd',
            'abcde', 'gfcbed', 'gfec'
        ],
        ['fcgedb', 'cgb', 'dgebacf', 'gc'],
    ),
]

expected_output_values = [
    'fdgacbe',
    'cefdb',
    'cefbgd',
    'gcbe',
    'fcgedb',
    'cgb',
    'dgebacf',
    'gc',
]


def test_entries():
    assert entries(lines) == parsed_lines


def test_output_values():
    assert output_values(parsed_lines) == expected_output_values


def test_easy_digits():
    assert easy_digits(output_values(entries(content))) == 26


def test_decode():
    entry = [
        'acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb',
        'cagedb', 'ab'
    ]
    expected = {
        'abcdeg': 0,
        'ab': 1,
        'acdfg': 2,
        'abcdf': 3,
        'abef': 4,
        'bcdef': 5,
        'bcdefg': 6,
        'abd': 7,
        'abcdefg': 8,
        'abcdef': 9,
    }
    actual = decode(entry)
    assert actual == expected


def test_sum_output():
    decoded_digits = {
        'abcdeg': 0,
        'ab': 1,
        'acdfg': 2,
        'abcdf': 3,
        'abef': 4,
        'bcdef': 5,
        'bcdefg': 6,
        'abd': 7,
        'abcdefg': 8,
        'abcdef': 9,
    }
    entry = ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']

    assert sum_output(decoded_digits, entry) == 5353
