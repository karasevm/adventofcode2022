from collections import deque
import sys


def parse_grid(input_list: list[str]) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    grid: list[list[int]] = []
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)
    for i, line in enumerate(input_list):
        grid_line = []
        for j, char in enumerate(line):
            if char == 'S':
                start = (i, j)
                char = 'a'
            elif char == 'E':
                end = (i, j)
                char = 'z'
            grid_line.append(ord(char))
        grid.append(grid_line)
    return grid, start, end


def part1(input_list: list[str]) -> int:
    grid, start, end = parse_grid(input_list)
    coords_to_check = deque([(start[0], start[1], None)])
    visited = set()
    end_parent = None

    while coords_to_check:
        row, col, parent = coords_to_check.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == end:
            end_parent = parent
            break
        for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (row+offset_row >= 0 and
                col+offset_col >= 0 and
                row+offset_row < len(grid) and
                col+offset_col < len(grid[0]) and
                    grid[row+offset_row][col+offset_col] <= grid[row][col] + 1):
                coords_to_check.append(
                    (row+offset_row, col+offset_col, (row, col, parent)))  # type: ignore

    path_length = 0
    while end_parent:
        end_parent = end_parent[2]
        path_length += 1

    return path_length


def part2(input_list: list[str]) -> int:
    grid, _, end = parse_grid(input_list)
    starts = []

    for i, line in enumerate(grid):
        for j, elev in enumerate(line):
            if elev == 97:
                starts.append((i, j))

    shortest_path_length = 9999999999

    for start in starts:
        coords_to_check = deque([(start[0], start[1], None)])
        visited = set()
        end_parent = None
        while coords_to_check:
            row, col, parent = coords_to_check.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if (row, col) == end:
                end_parent = parent
                break
            for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (row+offset_row >= 0 and
                    col+offset_col >= 0 and
                    row+offset_row < len(grid) and
                    col+offset_col < len(grid[0]) and
                        grid[row+offset_row][col+offset_col] <= grid[row][col] + 1):
                    coords_to_check.append(
                        (row+offset_row, col+offset_col, (row, col, parent)))  # type: ignore
        path_length = 0
        while end_parent:
            end_parent = end_parent[2]
            path_length += 1

        if path_length < shortest_path_length and path_length != 0:
            shortest_path_length = path_length

    return shortest_path_length


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
