from collections import Counter
from itertools import pairwise
from typing import Dict, List, Tuple

from days.inputreader import day, day_input


def parse_content(content: List[str]) -> Tuple[str, Dict[str, str]]:

    stripped = [s.strip() for s in content]
    slice_i = stripped.index('')
    template = stripped[:slice_i][0]
    pairs_raw = stripped[slice_i + 1:]
    pairs = dict([tuple(pair.split(' -> ')) for pair in pairs_raw])

    return template, pairs


def polymer_count(template: str, pairs: Dict[str, str], steps: int) -> int:

    tpl = template
    letter_count = Counter(tpl)
    template_pairs = Counter([''.join(p) for p in pairwise(tpl)])
    for _ in range(steps):
        new_pairs = Counter()
        for pair, cnt in template_pairs.items():
            letter = pairs[pair]
            letter_count[letter] += cnt
            new_pairs[f'{pair[0]}{letter}'] += cnt
            new_pairs[f'{letter}{pair[1]}'] += cnt
        template_pairs = new_pairs

    return max(letter_count.values()) - min(letter_count.values())


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    template, pairs = parse_content(content)

    part1 = polymer_count(template, pairs, 10)
    part2 = polymer_count(template, pairs, 40)

    print(part1)
    print(part2)
