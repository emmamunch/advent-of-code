import collections

with open('day6input.txt', 'r') as f:
    content = f.read()

groups = content.split('\n\n')

def part1(groups):
    num_yes = 0
    for group in groups:
        qs = set()
        for person in group.split('\n'):
            for ans in person.strip():
                qs.add(ans)
        num_yes += len(qs)
    return num_yes

def part2(groups):
    num_yes = 0
    for group in groups:
        qs = collections.defaultdict(list)
        for i, person in enumerate(group.split('\n')):
            for ans in person.strip():
                qs[ans].append(i)
        for k,v in qs.items():
            if len(v) == i+1:
                num_yes += 1
    return num_yes

print('part 1', part1(groups))
print('part 2', part2(groups))