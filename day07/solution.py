from collections import defaultdict
import sys


def part1(input_list: list[str]) -> int:
    curr_dir: list[str] = []
    file_dict = {}
    for line in input_list:
        if line[0] == '$':
            if line[2:4] == 'cd':
                if line[5:7] == '..':
                    curr_dir = curr_dir[:-1]
                elif line[5:] == '/':
                    curr_dir = []
                else:
                    curr_dir += [line.split(' ')[2]]
        elif line[0:3] != 'dir':
            file_dict['/' + '/'.join(curr_dir + [line.split(' ')[1]])] = int(line.split(' ')[0])

    size_sums = defaultdict(int)
    for file_path, file_size in file_dict.items():
        for i in range(file_path.count('/')):
            size_sums['/'.join(file_path.split('/')[:-i-1])] += file_size
    
    tmp_sump = 0
    for directory in size_sums.values():
        if directory <= 100_000:
            tmp_sump += directory



    return tmp_sump



def part2(input_list: list[str]) -> int:
    curr_dir: list[str] = []
    file_dict = {}
    for line in input_list:
        if line[0] == '$':
            if line[2:4] == 'cd':
                if line[5:7] == '..':
                    curr_dir = curr_dir[:-1]
                elif line[5:] == '/':
                    curr_dir = []
                else:
                    curr_dir += [line.split(' ')[2]]
        elif line[0:3] != 'dir':
            file_dict['/' + '/'.join(curr_dir + [line.split(' ')[1]])] = int(line.split(' ')[0])

    size_sums = defaultdict(int)
    for file_path, file_size in file_dict.items():
        for i in range(file_path.count('/')):
            size_sums['/'.join(file_path.split('/')[:-i-1])] += file_size
    
    sizes = [item for item in sorted(size_sums.values()) if item >= 30_000_000 - (70_000_000 - size_sums[''])]

    return sizes[0]


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
