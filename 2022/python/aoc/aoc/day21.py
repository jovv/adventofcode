import operator
from dataclasses import dataclass
from typing import Dict, Union

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
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


# I'd rather pass on using eval
def do_op(op: str, a: int, b: int) -> int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    return a // b


monkeys = {}

for line in content:
    monkey, yell = line.split(": ")
    monkeys[monkey] = parse_yell(yell)


def get_value(name: str, troop: Dict[str, Union[int, MonkeyOp]]) -> int:
    yell = troop[name]
    if type(yell) == int:
        return yell
    return OPS[yell.op](get_value(yell.a, troop), get_value(yell.b, troop))


part1 = get_value("root", monkeys)

print(part1)
