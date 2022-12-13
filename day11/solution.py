from __future__ import annotations
from collections import defaultdict
import sys
from enum import Enum


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2
    SQUARE = 3


op_string_mapping = {'+': Operation.ADD, '*': Operation.MULTIPLY}


class Monkey:
    def __init__(self, items: list[int], op: Operation, arg: int, mod: int, destination_true: int, destination_false: int):
        self.items = items
        self.op = op
        self.arg = arg
        self.mod = mod
        self.destination_true = destination_true
        self.destination_false = destination_false
        self.modulo: int | None = None

    def __repr__(self):
        return f"{self.items}"

    def add_item(self, item: int):
        self.items.append(item)

    def do_turn(self, monkeys: list[Monkey], divide: bool) -> int:
        inspect_count = 0
        while len(self.items) != 0:
            inspect_count += 1
            item = self.items.pop(0)
            if self.op == Operation.ADD:
                item += self.arg
            elif self.op == Operation.MULTIPLY:
                item *= self.arg
            elif self.op == Operation.SQUARE:
                item *= item
            if divide:
                item //= 3
            if self.modulo:
                item %= self.modulo
            if not item % self.mod:
                monkeys[self.destination_true].add_item(item)
            else:
                monkeys[self.destination_false].add_item(item)
        return inspect_count


def part1(input_list: list[str]) -> int:
    monkeys: list[Monkey] = []
    for line_n in range(0, len(input_list), 7):
        starting_items = [
            int(k) for k in input_list[line_n+1].split(": ")[1].split(', ')]
        op = op_string_mapping[input_list[line_n+2][23]]
        arg = (-1 if input_list[line_n + 2][-1] == 'd' else
               int(input_list[line_n+2].split(' ')[-1]))
        mod = int(input_list[line_n+3].split('by ')[1])
        destination_true = int(input_list[line_n+4][-1])
        destination_false = int(input_list[line_n+5][-1])

        if op == Operation.MULTIPLY and arg == -1:
            op = Operation.SQUARE

        monkeys.append(Monkey(starting_items, op, arg, mod,
                       destination_true, destination_false))

    monkeys_counts = defaultdict(int)

    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            monkeys_counts[i] += monkey.do_turn(monkeys, True)

    return sorted(monkeys_counts.values(), reverse=True)[0] * sorted(monkeys_counts.values(), reverse=True)[1]


def part2(input_list: list[str]) -> int:
    monkeys: list[Monkey] = []
    common_modulo = 1
    for line_n in range(0, len(input_list), 7):
        starting_items = [
            int(k) for k in input_list[line_n+1].split(": ")[1].split(', ')]
        op = op_string_mapping[input_list[line_n+2][23]]
        arg = (-1 if input_list[line_n + 2][-1] == 'd' else
               int(input_list[line_n+2].split(' ')[-1]))
        mod = int(input_list[line_n+3].split('by ')[1])
        destination_true = int(input_list[line_n+4][-1])
        destination_false = int(input_list[line_n+5][-1])

        common_modulo *= mod

        if op == Operation.MULTIPLY and arg == -1:
            op = Operation.SQUARE

        monkeys.append(Monkey(starting_items, op, arg, mod,
                       destination_true, destination_false))

    for monkey in monkeys:
        monkey.modulo = common_modulo

    monkeys_counts = defaultdict(int)

    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            monkeys_counts[i] += monkey.do_turn(monkeys, False)

    return sorted(monkeys_counts.values(), reverse=True)[0] * sorted(monkeys_counts.values(), reverse=True)[1]


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Error opening the file, try again")
        sys.exit(1)
    with f:
        lines = f.readlines()
        f.close()
        lines = [line.rstrip() for line in lines]
        print(
            f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
