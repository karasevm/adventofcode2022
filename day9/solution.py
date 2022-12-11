import math
import sys


def part1(input_list: list[str]) -> int:
    offset_dict = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0) }
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    tail_visited = set()
    for line in input_list:
        for _ in range(int(line.split(' ')[1])):
            old_head_x = head_x
            old_head_y = head_y
            head_x += offset_dict[line.split(' ')[0]][0]
            head_y += offset_dict[line.split(' ')[0]][1]
            if (abs(tail_y - head_y) == 2 or abs(tail_x - head_x) == 2):
                tail_x = old_head_x
                tail_y = old_head_y
            tail_visited.add((tail_x, tail_y))

    return len(tail_visited)

def pretty_print(knots: list[list[int]]):
    for i in range(-10, 10):
        for j in range(-10, 10):
            print('.' if [i,j] not in knots else knots.index([i,j]), end='')
        print()


def find_offset(first_coords: tuple[int, int], second_coords: tuple[int,int ]) -> tuple[int, int]:
    if first_coords[0] == second_coords[0]:
        return (first_coords[0],second_coords[1] - first_coords[1])
    if first_coords[1] == second_coords[1]:
        return (second_coords[0] - first_coords[0],first_coords[1])
    return (second_coords[0] - first_coords[0], second_coords[1] - first_coords[1])

def find_distance(first_coords: tuple[int, int], second_coords: tuple[int,int ]) -> float:
    return math.sqrt((second_coords[0]-first_coords[0])**2+(second_coords[1]-first_coords[1])**2)

def part2(input_list: list[str]) -> int:
    offset_dict = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0) }
    knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    tail_visited = set()
    for line in input_list:
        for _ in range(int(line.split(' ')[1])):
            knots[0][0] += offset_dict[line.split(' ')[0]][0]
            knots[0][1] += offset_dict[line.split(' ')[0]][1]
            for knot_n in range(1, len(knots)):
                distances = {}
                if (abs(knots[knot_n-1][0] - knots[knot_n][0]) == 2 or 
                    abs(knots[knot_n-1][1] - knots[knot_n][1]) == 2):
                    if (abs(knots[knot_n-1][0] == knots[knot_n][0]) or 
                        abs(knots[knot_n-1][1] == knots[knot_n][1])):
                        for i in [-1,1]:
                            if abs(knots[knot_n-1][0] - (knots[knot_n][0]+i)) < 2 and abs(knots[knot_n-1][1] - (knots[knot_n][1])) < 2:
                                distances[find_distance((knots[knot_n][0] ,knots[knot_n][1]),(knots[knot_n][0]+i, knots[knot_n][1]))]=(knots[knot_n][0]+i, knots[knot_n][1])
                        for i in [-1,1]:
                            if abs(knots[knot_n-1][0] - (knots[knot_n][0])) < 2 and abs(knots[knot_n-1][1] - (knots[knot_n][1]+i)) < 2:
                                distances[find_distance((knots[knot_n][0] ,knots[knot_n][1]),(knots[knot_n][0], knots[knot_n][1]+i))]=(knots[knot_n][0], knots[knot_n][1]+i)
                        knots[knot_n][0] = distances[min(distances.keys())][0]
                        knots[knot_n][1] = distances[min(distances.keys())][1]
                    else:
                        for i,j in [(1,1), (1,-1), (-1,-1), (-1,1)]:
                                if (abs(knots[knot_n-1][0] - (knots[knot_n][0]+i)) < 2 and 
                                    abs(knots[knot_n-1][1] - (knots[knot_n][1]+j)) < 2):
                                    distances[find_distance((knots[knot_n][0] ,knots[knot_n][1]),(knots[knot_n][0]+i, knots[knot_n][1]+j))]=(knots[knot_n][0]+i, knots[knot_n][1]+j)
                        knots[knot_n][0] = distances[min(distances.keys())][0]
                        knots[knot_n][1] = distances[min(distances.keys())][1]

            tail_visited.add(tuple(knots[-1]))

    return len(tail_visited)

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
