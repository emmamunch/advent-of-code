import collections
import re

def part1():
    bag_graph = collections.defaultdict(list)
    with open('day7input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            line = re.sub(' bag+(s)?', '', line)
            line = line.split(' contain ')
            outer = line[0].strip()
            inner = line[1].strip('. \n').split(', ')
            for bag in inner:
                bag_graph[bag[2:]].append(outer)


    check = set()
    curr_bag = ['shiny gold']
    while len(curr_bag) != 0:
        for bag in bag_graph[curr_bag[0]]:
            if bag not in check:
                check.add(bag)
                curr_bag.append(bag)
        curr_bag.pop(0)

    print('part 1', len(check))

part1()

def bag_dfs(startName, bag_graph):
    total = 0
    coeff = 1
    stack = [(1, startName)]
    while stack:
        coeff, name = stack.pop(0)
        for edge in bag_graph[name]:
            total += coeff * int(edge[0])
            stack.insert(0, (coeff * int(edge[0]), edge[1]))
    
    return total

def part2():
    bag_graph = collections.defaultdict(list)
    with open('day7input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            line = re.sub(' bag+(s)?', '', line)
            line = line.split(' contain ')
            outer = line[0].strip()
            if 'no other' in line[1]:
                bag_graph[outer] = []
            else:
                inner = line[1].strip('. \n').split(', ')
                for bag in inner:
                    bag_graph[outer].append((bag[0], bag[2:]))
    
    print('part 2', bag_dfs('shiny gold', bag_graph))

part2()




