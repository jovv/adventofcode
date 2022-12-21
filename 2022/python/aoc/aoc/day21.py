import operator
from dataclasses import dataclass
from typing import Dict, Union

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

FILENAME = "./resources/day21.txt"
with open(FILENAME) as f:
    content = [line.strip() for line in f.readlines()]


@dataclass
class MonkeyOp:
    a: str
    op: str
    b: str


def parse_yell(s: str) -> Union[int, MonkeyOp]:
    if s.isdigit():
        return int(s)

    a, op, b = s.split()
    return MonkeyOp(a, op, b)


monkeys = {}

for line in content:
    monkey, yell = line.split(": ")
    monkeys[monkey] = parse_yell(yell)


def get_value_pt1(name: str, troop: Dict[str, Union[int, MonkeyOp]]) -> int:
    yell = troop[name]
    if type(yell) == int:
        return yell
    return OPS[yell.op](get_value_pt1(yell.a, troop), get_value_pt1(yell.b, troop))


def get_value_pt2(name: str, troop: Dict[str, Union[int, MonkeyOp]]) -> Union[int, float, complex]:
    yell = troop[name]
    if name == "root":
        left = get_value_pt2(yell.a, troop)
        right = get_value_pt2(yell.b, troop)
        return (right - left.real) / left.imag
    if type(yell) == MonkeyOp:
        return OPS[yell.op](get_value_pt2(yell.a, troop), get_value_pt2(yell.b, troop))
    return yell


part1 = int(get_value_pt1("root", monkeys))

monkeys["humn"] = 1j
part2 = int(get_value_pt2("root", monkeys))

print(part1)
print(part2)
