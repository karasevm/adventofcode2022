import sys
import re

def find_stacks_dimensions(input_list: list[str]) -> tuple[int, int]:
    rows = 0
    for i, line in enumerate(input_list):
        if line == '':
            rows = i - 1
            break
    cols = int(input_list[rows][-1])

    return rows,cols

def part1(input_list: list[str]) -> str:
    
    rows, cols = find_stacks_dimensions(input_list)

    stacks = [[]]
    for i in range(cols):
        col = []
        for k in range(rows):
            if len(input_list[k]) >= i*4+1 and input_list[k][i*4+1] != ' ':
                col.append(input_list[k][i*4+1])
        stacks.append(col)

    for line in input_list[rows + 2:]:
        re_result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        assert re_result != None
        for i in range(int(re_result.group(1))):
            stacks[int(re_result.group(3))].insert(0,stacks[int(re_result.group(2))].pop(0))

    result = ''
    for stack in stacks[1:]:
        result += stack[0]

    return result



def part2(input_list: list[str]) -> str:
    
    
    rows, cols = find_stacks_dimensions(input_list)

    stacks = [[]]
    for i in range(cols):
        col = []
        for k in range(rows):
            if len(input_list[k]) >= i*4+1 and input_list[k][i*4+1] != ' ':
                col.append(input_list[k][i*4+1])
        stacks.append(col)

    for line in input_list[rows + 2:]:
        re_result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        assert re_result != None
        tmp_stack = []
        for i in range(int(re_result.group(1))):
            tmp_stack.append(stacks[int(re_result.group(2))].pop(0))
        stacks[int(re_result.group(3))] = tmp_stack + stacks[int(re_result.group(3))]

    result = ''
    for stack in stacks[1:]:
        result += stack[0]

    return str(result)

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
