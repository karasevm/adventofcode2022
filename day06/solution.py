import sys


def part1(input_list: list[str]) -> int:
    for i in range(len(input_list[0]) - 4):
        if len(set(input_list[0][i:i+4])) == 4:
            return i + 4
    return -1



def part2(input_list: list[str]) -> int:
    for i in range(len(input_list[0]) - 14):
        if len(set(input_list[0][i:i+14])) == 14:
            return i + 14
    return -1

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
