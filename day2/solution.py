import sys


opponent = ['A', 'B', 'C']
you = ['X', 'Y', 'Z']

def part1(input_list: list[str]) -> int:
    score = 0
    for line in input_list:
        score += you.index(line[2]) + 1
        if ((line[0]) == 'A'):
            if((line[2]) == 'X'):
                score += 3
            elif((line[2]) == 'Y'):
                score += 6
        elif ((line[0]) == 'B'):
            if((line[2]) == 'Y'):
                score += 3
            elif((line[2]) == 'Z'):
                score += 6
        elif ((line[0]) == 'C'):
            if((line[2]) == 'Z'):
                score += 3
            elif((line[2]) == 'X'):
                score += 6

    return score



def part2(input_list: list[str]) -> int:
    score = 0
    for line in input_list:
        if ((line[0]) == 'A'):
            if((line[2]) == 'Y'):
                score += 4
            elif((line[2]) == 'Z'):
                score += 8
            elif((line[2]) == 'X'):
                score += 3

        elif ((line[0]) == 'B'):
            if((line[2]) == 'Y'):
                score += 5
            elif((line[2]) == 'Z'):
                score += 9
            elif((line[2]) == 'X'):
                score += 1
        elif ((line[0]) == 'C'):
            if((line[2]) == 'Y'):
                score += 6
            elif((line[2]) == 'Z'):
                score += 7
            elif((line[2]) == 'X'):
                score += 2

    return score

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
