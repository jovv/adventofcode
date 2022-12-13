import functools
import json


def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def is_ordered(left, right) -> int:
    if type(left) == int:
        if type(right) == int:
            return sign(right - left)
        else:
            left = [left]

    if type(right) == int:
        if type(left) == int:
            return sign(right - left)
        else:
            right = [right]
            
    for i in range(min(len(left), len(right))):
        res = is_ordered(left[i], right[i])
        if res != 0:
            return res

    return sign(len(right) - len(left))

def part1(puzzle_input: str) -> int:
    pairs = [[json.loads(part) for part in pair.split("\n") ]for pair in puzzle_input.split("\n\n")]

    sum_ordered = 0
    
    for i, pair in enumerate(pairs):
        if is_ordered(*pair) == 1:
            sum_ordered += i + 1

    return sum_ordered

def part2(puzzle_input: str) -> int:
    packets = [json.loads(line) for line in puzzle_input.split("\n") if line.strip()] + [[[2]]] + [[[6]]]
    sorted_packets = sorted(packets, key=functools.cmp_to_key(is_ordered), reverse=True)
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

if __name__ == "__main__":

    filename = "day13.txt"
    with open(filename) as f:
        content = f.read()

    print(f"Part 1: {part1(content)}")
    print(f"Part 2: {part2(content)}")

