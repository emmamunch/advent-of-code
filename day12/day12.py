import math

with open('day12input.txt', 'r') as f:
    content = f.readlines()

def add_coord(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def mult_coord(coord, num):
    return (coord[0] * num, coord[1] * num)

def move_forward(curr_pos, dist, direction):
    # facing east
    if direction == 0:
        return add_coord(curr_pos, (0, dist))
    # facing north
    elif direction == 90:
        return add_coord(curr_pos, (-dist, 0))
    # facing west
    elif direction == 180:
        return add_coord(curr_pos, (0, -dist))
    # facing south
    elif direction == 270:
        return add_coord(curr_pos, (dist, 0))


def rotate(dir, amt, dir_idx):
    if dir == 'R':
        return (dir_idx - (amt // 90)) % len(directions)
        # return dir_idx - (amt // 90)
    elif dir == 'L':
        return (dir_idx + (amt // 90)) % len(directions)

def rotate_way(dir, amt, way_pos):
    if dir == 'R':
        if amt == 0:
            return way_pos
        elif amt == 90:
            return (way_pos[1], -way_pos[0])
        elif amt == 180:
            return (-way_pos[0], -way_pos[1])
        elif amt == 270:
            return (-way_pos[1], way_pos[0])
    elif dir == 'L':
        if amt == 0:
            return way_pos
        elif amt == 90:
            return (-way_pos[1], way_pos[0])
        elif amt == 180:
            return (-way_pos[0], -way_pos[1])
        elif amt == 270:
            return (way_pos[1], -way_pos[0])

directions = [0, 90, 180, 270]


def part1():
    start_pos = (0,0)
    curr_pos = start_pos
    dir_idx = 0
    for action in content:
        if action[0] == 'F':
            curr_pos = move_forward(curr_pos, int(action[1:]), directions[dir_idx])
        elif action[0] == 'E':
            curr_pos = add_coord(curr_pos, (0, int(action[1:])))
        elif action[0] == 'N':
            curr_pos = add_coord(curr_pos, (-int(action[1:]), 0))
        elif action[0] == 'W':
            curr_pos = add_coord(curr_pos, (0, -int(action[1:])))
        elif action[0] == 'S':
            curr_pos = add_coord(curr_pos, (int(action[1:]), 0))
        else:
            dir_idx = rotate(action[0], int(action[1:]), dir_idx)
    print('part 1', curr_pos)

part1()

def part2():
    start_pos = (0,0)
    curr_pos = start_pos
    way_pos = (10, 1)
    for action in content:
        if action[0] == 'F':
            curr_pos = add_coord(mult_coord(way_pos, int(action[1:])), curr_pos)
        elif action[0] == 'E':
            way_pos = add_coord(way_pos, (int(action[1:]), 0))
        elif action[0] == 'N':
            way_pos = add_coord(way_pos, (0, int(action[1:])))
        elif action[0] == 'W':
            way_pos = add_coord(way_pos, (-int(action[1:]), 0))
        elif action[0] == 'S':
            way_pos = add_coord(way_pos, (0, -int(action[1:])))
        else:
            way_pos = rotate_way(action[0], int(action[1:]), way_pos)
    print('part 2', curr_pos)

part2()