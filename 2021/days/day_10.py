from functools import reduce
import re
from typing import List

from days.inputreader import day_input, day

illegal_character_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completed_character_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

matching_re = re.compile(r'\(\)|\[\]|\{\}|\<\>')
illegal_re = re.compile(r'\)|\]|\}|\>')


def scores(lines: List[str]) -> int:
    illegal_score = 0
    autocomplete_scores = []

    for line in lines:
        nr_of_subs = 1
        while nr_of_subs > 0:
            line, nr_of_subs = matching_re.subn('', line)
        m = illegal_re.search(line)
        if m:  # corrupt line
            illegal_score += illegal_character_scores[m.group(0)]
        else:  # incomplete line
            autocomplete_scores.append(
                reduce(
                    lambda a, b: 5 * a + b,
                    [completed_character_scores[c] for c in line[::-1]],
                    0,
                ))

    autocomplete_middle_score = sorted(autocomplete_scores)[
        len(autocomplete_scores) // 2]

    return illegal_score, autocomplete_middle_score


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    lines = [line.strip() for line in content]
    part1, part2 = scores(lines)

    print(part1)
    print(part2)
