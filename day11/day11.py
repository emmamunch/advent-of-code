import numpy as np

content = []
with open('day11input.txt', 'r') as f:
    for line in f:
        content.append(list(line.strip()))

content = np.array(content)
prev_state = -1

ADJ = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
MAX_H = content.shape[0]
MAX_W = content.shape[1]

def valid_width(w):
    return w >= 0 and w < MAX_W

def valid_height(h):
    return h >= 0 and h < MAX_H

def add_coord(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

def valid_coord(coord):
    return valid_height(coord[0]) and valid_width(coord[1])

def get_neighbors(idx, content):
    n = [[], []]
    for a in ADJ:
        curr_coord = add_coord(idx, a)
        if valid_coord(curr_coord):
            n[0].append(curr_coord[0])
            n[1].append(curr_coord[1])
    return (tuple(n[0]), tuple(n[1]))

def get_neighbors2(idx, content):
    n = [[], []]
    for a in ADJ:
        curr_coord = add_coord(idx, a)
        while valid_coord(curr_coord) and content[curr_coord] == '.':
            curr_coord = add_coord(curr_coord, a)
        if valid_coord(curr_coord):
            n[0].append(curr_coord[0])
            n[1].append(curr_coord[1])
    return (tuple(n[0]), tuple(n[1]))

def empty_rule(indices, content, neighbors_fn):
    to_occupy = [[], []]
    for i in range(len(indices[0])):
        neighbors = neighbors_fn((indices[0][i], indices[1][i]), content)
        if '#' not in np.unique(content[neighbors]):
            to_occupy[0].append(indices[0][i])
            to_occupy[1].append(indices[1][i])
    return (tuple(to_occupy[0]), tuple(to_occupy[1]))


def occ_rule(indices, content, neighbors_fn):
    to_empty = [[], []]
    for i in range(len(indices[0])):
        neighbors = neighbors_fn((indices[0][i], indices[1][i]), content)
        #TODO: change for part 1 back to 3
        if len(np.where(content[neighbors] == '#')[0]) > 4:
            to_empty[0].append(indices[0][i])
            to_empty[1].append(indices[1][i])
    return (tuple(to_empty[0]), tuple(to_empty[1]))

def round(content):
    empty = np.where(content == 'L')
    occ = np.where(content == '#')
    to_occ = empty_rule(empty, content, get_neighbors)
    to_emp = occ_rule(occ, content, get_neighbors)
    content[to_emp] = 'L'
    content[to_occ] = '#'
    return content

def round_2(content):
    empty = np.where(content == 'L')
    occ = np.where(content == '#')
    to_occ = empty_rule(empty, content, get_neighbors2)
    to_emp = occ_rule(occ, content, get_neighbors2)
    content[to_emp] = 'L'
    content[to_occ] = '#'
    return content
    
def start(content):
    prev_content = None
    round_num = 1
    while not np.array_equal(prev_content, content):
        print(round_num)
        prev_content = np.copy(content)
        content = round(content)
        round_num += 1
    return len(np.where(content == '#')[0])

def start2(content):
    prev_content = None
    round_num = 1
    while not np.array_equal(prev_content, content):
        print(round_num)
        prev_content = np.copy(content)
        content = round_2(content)
        round_num += 1
    return len(np.where(content == '#')[0])
    

# print('part 1:', start(content))
print('part 2:', start2(content))

