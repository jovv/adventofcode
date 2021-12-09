from typing import Dict, List, Tuple, Set
from days.inputreader import day_input, day

digit_segments = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}


def entries(lines: List[str]) -> List[Tuple[List[str], List[str]]]:
    return [
        tuple(part.strip().split(' ') for part in line.strip().split('|'))
        for line in lines
    ]


def output_values(all_entries: List[Tuple[List[str], List[str]]]) -> List[str]:
    return [digit for entry in all_entries for digit in entry[1]]


def easy_digits(digits: List[str]) -> int:
    return sum([1 for digit in digits if len(digit) in digit_segments.keys()])


def decode(entry: List[str]) -> Dict[int, Set[str]]:
    lengths = {s: len(s) for s in entry}
    codes = {}
    for length, nr in digit_segments.items():
        codes[nr] = [set(s) for s, le in lengths.items() if le == length][0]
    # 7 - 1 = top segment
    top_segment = codes[7] - codes[1]
    # 9 - 4 - top = bottom segment
    nine, bottom_segment = [
        (set(s), set(s) - codes[4] - top_segment) for s, le in lengths.items()
        if le == 6 and len(set(s) - codes[4] - top_segment) == 1
    ][0]
    codes[9] = nine
    # 3 - 1 - top - bottom = middle segment
    three, middle_segment = [
        (set(s), set(s) - codes[1] - top_segment - bottom_segment)
        for s, le in lengths.items()
        if le == 5 and len(set(s) - codes[1] - top_segment -
                           bottom_segment) == 1
    ][0]
    codes[3] = three
    # 8 - middle = 0
    codes[0] = codes[8] - middle_segment
    # 6 is the only unknown left of length 6
    codes[6] = [
        set(s) for s, le in lengths.items() if le == 6 and
        sorted(s) not in [sorted(codes[0]), sorted(codes[9])]
    ][0]
    # 5 = 6 - 5 with a single segment left
    codes[5] = [
        set(s) for s, le in lengths.items()
        if le == 5 and len(codes[6] - set(s)) == 1
    ][0]
    # 2 is leftover
    codes[2] = [
        set(s) for s, le in lengths.items() if le == 5 and
        sorted(s) not in [sorted(codes[3]), sorted(codes[5])]
    ][0]

    return {''.join(sorted(v)): k for k, v in codes.items()}


def sum_output(decoded_digits: Dict[str, int], output: List[str]) -> int:
    return int(''.join(
        [''.join(str(decoded_digits[''.join(sorted(s))])) for s in output]))


def sum_output_values(entries: List[Tuple[List[str], List[str]]]) -> int:
    total = 0
    for entry in entries:
        decoded_digits = decode(entry[0])
        total += sum_output(decoded_digits, entry[1])
    return total


if __name__ == '__main__':

    content = day_input(f'{day(__file__)}_input.txt')
    all_entries = entries(content)

    part1 = easy_digits(output_values(all_entries))
    part2 = sum_output_values(all_entries)

    print(part1)
    print(part2)
