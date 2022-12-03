import sys

alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def part1(input_list: list[str]) -> int:
    sum_prio = 0
    for line in input_list:
        print(line)
        shared_item = set(line[:len(line)//2]) & set(line[len(line)//2:])
        sum_prio += 1 + alphabet.index(shared_item.pop())
    return sum_prio



def part2(input_list: list[str]) -> int:
    sum_prio = 0
    for i in range(0,len(input_list),3):
        shared_item = set(input_list[i]) & set(input_list[i+1]) & set(input_list[i+2])
        sum_prio += 1 + alphabet.index(shared_item.pop())
    return sum_prio

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
