import re
from typing import List

from days.inputreader import day_input, day

illegal_character_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

matching_re = re.compile(r'\(\)|\[\]|\{\}|\<\>')
illegal_re = re.compile(r'\)|\]|\}|\>')


def syntax_error_score(lines: List[str]) -> int:
    score = 0

    for line in lines:
        nr_of_subs = 1
        while nr_of_subs > 0:
            line, nr_of_subs = matching_re.subn('', line)
        m = illegal_re.search(line)
        if m:
            score += illegal_character_scores[m.group(0)]

    return score


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')

    part1 = syntax_error_score(content)
    # part2 = syntax_error_score(content)

    print(part1)
    # print(part2)
