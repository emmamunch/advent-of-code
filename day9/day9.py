pre_len = 25

content = []
with open('day9input.txt', 'r') as f:
    for line in f:
        content.append(int(line))

for i in range(len(content)-pre_len-1):
    num = content[i+pre_len]
    preamble = content[i:i+pre_len]
    valid = False
    for n in preamble:
        if num-n in preamble:
            valid = True
            break
    if not valid:
        part1 = num
        break

lens = range(2, len(content))
for l in lens:
    for i in range(0, len(content)-l):
        if sum(content[i:i+l]) == part1:
            part2 = min(content[i:i+l]) + max(content[i:i+l])
            break

print(part2)



