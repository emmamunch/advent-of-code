import pandas as pd
import numpy as np

# tree = pd.read_csv('day3input.txt', header=None)
# arr = np.array(tree)
# print(arr.shape)
# print(arr[:,0])

content = []

with open('day3input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        content.append(list(line.strip()))

arr = np.matrix(content)
trees = []
i = 0
j = 0
i_inc = [1, 1, 1, 1, 2]
j_inc = [1, 3, 5, 7, 1]
print(arr.shape)
for k in range(5):
    num_trees = 0
    while i < arr.shape[0]:
        if arr[i, (j % arr.shape[1])] == '#':
            num_trees += 1
        i += i_inc[k]
        j += j_inc[k]
    print(num_trees)
    trees.append(num_trees)

print(np.product(trees))

import math

with open('day3input.txt', 'r') as f:
    lines = f.read().splitlines() 

routes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

total = []
for route in routes:
    c = 0
    for v in range(0, len(lines), route[1]):
        h = int(divmod((v / route[1]) * route[0], len(lines[v]))[1])
        value = lines[v][h]
        if value == "#":
            c += 1
    total.append(c)

print("Solution 1 =>", total[1])
print("Solution 2 =>", np.product(total))