import math
import numpy as np
def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

content = []
with open('day10input.txt', 'r') as f:
    for line in f:
        content.append(int(line))

content.sort()

jolts = [0,0,0]
content.insert(0,0)
content.append(max(content)+3)
necessary = [0]

btw = []
combos = []
for i in range(1, len(content)):
    jolts[content[i]-content[i-1]-1] += 1
    
    if content[i]-content[i-1] == 3:
        if content[i-1] not in necessary:
            necessary.append(content[i-1])
        if content[i] not in necessary:
            necessary.append(content[i])
        if btw:
            diff = necessary[-2] - necessary[-3]
            min_adpt = (diff - 1) // 3
            max_adpt = len(btw) - 1
            count = 0
            for j in range(min_adpt,max_adpt+1):
                count += choose(max_adpt, j)
            if count:
                print(btw)
                print(count)
                combos.append(count)
        btw = []
    else:
        btw.append(content[i])

print('part 1', jolts[0]*jolts[2])
print(necessary)
print('part 2', np.prod(combos))