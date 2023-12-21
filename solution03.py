import string
import itertools
from collections import defaultdict

def getNum(line, ind):
    start, end = ind, ind
    while start > 0 and line[start - 1] in string.digits:
        start -= 1
    while end < len(line) - 1 and line[end + 1] in string.digits:
        end += 1
    return int(line[start:end + 1]), start, end

def check(data, line, i, j):
    num, start, end = getNum(line, j)
    cols = [x for x in range(max(i - 1, 0), min(i + 1, len(data) - 1) + 1)]
    rows = [x for x in range(max(start - 1, 0), min(end + 1, len(line) - 1) + 1)]
    nums = itertools.product(cols, rows)
    val = 0
    locs = []
    for x, y in nums:
        if data[x][y] == '*':
            val = num
            locs.append((x, y))
        
    return val, end, locs
    
with open('input3.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

gears = defaultdict(list)
ans = 0
for i in range(len(data)):
    line = data[i]
    checked = -1
    for j in range(len(line)):
        if j <= checked:
            continue
        if line[j] in string.digits:
            val, checked, locs = check(data, line, i, j)
            for loc in locs:
                gears[loc].append(val)

for locs in gears.values():
    if len(locs) == 2:
        ans += locs[0] * locs[1]

print(ans)
