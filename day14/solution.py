from collections import defaultdict
import sys


def create_grid(input_list: list[str]):
    grid = defaultdict(lambda: defaultdict(lambda: '.'))
    y_limits = (0, 0)
    x_limits = (1000, 0)
    for line in input_list:
        points = line.split(' -> ')
        for point_n in range(len(points) - 1):
            y_start, y_end = sorted(
                [int(points[point_n].split(',')[1]), int(points[point_n+1].split(',')[1])])
            y_limits = 0, max(y_limits[1], y_end)
            for y in range(y_start, y_end+1):
                x_start, x_end = sorted(
                    [int(points[point_n].split(',')[0]), int(points[point_n+1].split(',')[0])])
                x_limits = min(x_limits[0], x_start), max(x_limits[1], x_end)
                for x in range(x_start, x_end+1):
                    grid[y][x] = '#'

    return (y_limits[0], y_limits[1]+1), (x_limits[0], x_limits[1]+1), grid


def part1(input_list: list[str]) -> int:
    y_limits, x_limits, grid = create_grid(input_list)

    sand_count = 0
    while True:
        sand_count += 1
        sand_y, sand_x = 0, 500
        while sand_y <= y_limits[1]:
            if grid[sand_y+1][sand_x] == '.':
                sand_y += 1
                continue
            elif grid[sand_y+1][sand_x-1] == '.':
                sand_y += 1
                sand_x -= 1
                continue
            elif grid[sand_y+1][sand_x+1] == '.':
                sand_y += 1
                sand_x += 1
                continue
            break
        if sand_y > y_limits[1]:
            for y in range(*y_limits):
                for x in range(*x_limits):
                    print(grid[y][x], end='')
                print()
            print()
            return sand_count - 1
        grid[sand_y][sand_x] = 'o'


def part2(input_list: list[str]) -> int:
    y_limits, x_limits, grid = create_grid(input_list)
    y_limits = (y_limits[0], y_limits[1] + 2)

    grid[y_limits[1]-1] = defaultdict(lambda: '#')

    sand_count = 0
    while grid[0][500] != 'o':
        sand_count += 1
        sand_y, sand_x = 0, 500
        while True:
            if grid[sand_y+1][sand_x] == '.':
                sand_y += 1
                continue
            elif grid[sand_y+1][sand_x-1] == '.':
                sand_y += 1
                sand_x -= 1
                continue
            elif grid[sand_y+1][sand_x+1] == '.':
                sand_y += 1
                sand_x += 1
                continue
            break
        grid[sand_y][sand_x] = 'o'
        x_limits = min(x_limits[0], sand_x), max(x_limits[1], sand_x+1)
    for y in range(*y_limits):
        for x in range(*x_limits):
            print(grid[y][x], end='')
        print()
    print()

    return sand_count


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
