from collections import defaultdict
import sys


def part1(input_list: list[str]) -> int:
    cycle = 0
    X = 1
    result = 0 
    check_list = [20, 60, 100, 140 ,180, 220]
    for line in input_list:
        code = line.split(' ')

        if code[0] == 'noop':
            cycle += 1
            if cycle in check_list:
                result += X * cycle
        elif code[0] == 'addx':
            cycle += 1
            if cycle in check_list:
                result += X * cycle
            cycle += 1
            if cycle in check_list:
                result += X * cycle
            X += int(code[1])
    return result


def part2(input_list: list[str]) -> int:
    cycle = 0
    X = 1
    result = 0 

    check_list = [40, 80, 120, 160, 200, 240]
    screen = defaultdict(lambda:'.')

    for line in input_list:
        code = line.split(' ')
        
        if code[0] == 'noop':
            if cycle % 40 in (X-1, X, X+1):
                screen[cycle] = '#'
            cycle += 1
            if cycle in check_list:
                result += X * cycle
            
        elif code[0] == 'addx':
            if cycle % 40 in (X-1, X, X+1):
                screen[cycle] = '#'
            cycle += 1

            if cycle in check_list:
                result += X * cycle
            if cycle % 40 in (X-1, X, X+1):
                screen[cycle] = '#'
            cycle += 1
            if cycle in check_list:
                result += X * cycle
            X += int(code[1])

    for i in range (6):
        for j in range(40):
            print(screen[i*40+j], end='')
        print()
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
