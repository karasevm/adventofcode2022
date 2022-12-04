import sys


def part1(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        first_pair = line.split(',')[0].split('-')
        start_a = int(first_pair[0])
        end_a = int(first_pair[1])

        second_pair = line.split(',')[1].split('-')
        start_b = int(second_pair[0])
        end_b = int(second_pair[1])

        if ((start_a <= start_b and end_a >= end_b) or 
            (start_a >= start_b and end_a <= end_b)):
            result += 1
    

    return result



def part2(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        first_pair = line.split(',')[0].split('-')
        start_a = int(first_pair[0])
        end_a = int(first_pair[1])

        second_pair = line.split(',')[1].split('-')
        start_b = int(second_pair[0])
        end_b = int(second_pair[1])

        if ((start_a <= start_b and end_a >= start_b) or 
            (start_a >= start_b and start_a <= end_b)):
            result += 1
    

    return result

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
