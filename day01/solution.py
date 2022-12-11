import sys


def part1(input_list: list[str]) -> int:
    sums = [0]
    for line in input_list:
        if (len(line) == 0):
            sums.append(0)
            continue
        sums[-1] += int(line)
    return max(sums)



def part2(input_list: list[str]) -> int:
    sums = [0]
    for line in input_list:
        if (len(line) == 0):
            sums.append(0)
            continue
        sums[-1] += int(line)
    return sum(sorted(sums)[-3:])

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
