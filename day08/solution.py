import sys


def part1(input_list: list[str]) -> int:
    visible_list = set()
    grid = [[int(height) for height in line] for line in input_list]

    for row_n in range(1,len(grid)-1):
        prev_height = -1
        for col_n in range(len(grid[0])):
            if grid[row_n][col_n] > prev_height:
                prev_height = grid[row_n][col_n]
                visible_list.add((row_n, col_n))
    for row_n in range(1,len(grid)-1):
        prev_height = -1
        for col_n in range(len(grid[0])-1, -1, -1):
            if grid[row_n][col_n] > prev_height:
                prev_height = grid[row_n][col_n]
                visible_list.add((row_n, col_n))
    
    for col_n in range(1,len(grid[0])-1):
        prev_height = -1
        for row_n in range(len(grid)):
            if grid[row_n][col_n] > prev_height:
                prev_height = grid[row_n][col_n]
                visible_list.add((row_n, col_n))

    for col_n in range(1,len(grid[0])-1):
        prev_height = -1
        for row_n in range(len(grid)-1, -1, -1):
            if grid[row_n][col_n] > prev_height:
                prev_height = grid[row_n][col_n]
                visible_list.add((row_n, col_n))
    return len(visible_list) + 4



def part2(input_list: list[str]) -> int:
    grid = [[int(height) for height in line] for line in input_list]
    scores = []
    for row_n in range(1, len(grid)-1):
        for col_n in range(1, len(grid[0])-1):
            score = 1
            count = 0
            for i in range(row_n-1, -1, -1):
                if grid[row_n][col_n] > grid[i][col_n]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0
            for i in range(row_n+1, len(grid)):
                if grid[row_n][col_n] > grid[i][col_n]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0
            for k in range(col_n-1, -1, -1):
                if grid[row_n][col_n] > grid[row_n][k]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            count = 0
            for k in range(col_n+1, len(grid[0])):
                if grid[row_n][col_n] > grid[row_n][k]:
                    count += 1
                else:
                    count += 1
                    break
            score *= count
            scores.append(score)
    
    return max(scores)

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
