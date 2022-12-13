from functools import cmp_to_key
import sys
import json


def compare(first: int | list, second: int | list) -> int:
    if isinstance(first, int) and isinstance(second, int):
        return first - second

    if isinstance(first, list) and isinstance(second, list):
        for i in range(min(len(first), len(second))):
            tmp_result = compare(first[i], second[i])
            if tmp_result != 0:
                return tmp_result
        return len(first) - len(second)

    if isinstance(first, int) and isinstance(second, list):
        return compare([first], second)

    if isinstance(first, list) and isinstance(second, int):
        return compare(first, [second])

    return 0


def part1(input_list: list[str]) -> int:
    result = 0
    for line_n in range(0, len(input_list), 3):
        first = json.loads(f"[{input_list[line_n]}]")
        second = json.loads(f"[{input_list[line_n+1]}]")
        if compare(first, second) < 0:
            result += (line_n // 3) + 1

    return result


def part2(input_list: list[str]) -> int:
    packets = [[[2]], [[6]]]
    for line in input_list:
        if line != '':
            packets.append(json.loads(line))

    packets.sort(key=cmp_to_key(compare))

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


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
