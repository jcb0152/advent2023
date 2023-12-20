
from collections import defaultdict, deque

def rotate(data, stuck, moving, top, side):
    nums = []
    ans = 0

    newMoving = defaultdict(list)
    for i in range(side + 1):
        filled = defaultdict(int)
        
        spots = [top, *stuck[i], -1]
        rocks = iter(moving[i])
        
        buckets = [range(spots[i + 1], spots[i]) for i in range(len(spots) - 1)]

        try:
            current = next(rocks)
        except:
            continue
        
        for j in range(len(spots) - 1):
            while current in buckets[j]:
                ans += spots[j]
                newMoving[spots[j] - 1].append(side - i - 1)
                spots[j] -= 1
                try:
                    current = next(rocks)
                except:
                    break
    return ans, newMoving

with open('input14.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

top = len(data)
side = len(data[0])
stuckN = defaultdict(list)
stuckW = defaultdict(list)
stuckS = defaultdict(deque)
stuckE = defaultdict(deque)

moving = defaultdict(list)

for (row, line) in enumerate(data):
    for (col, val) in enumerate(line):
        if val == 'O':
            moving[col].append(top - row - 1)
        if val == '#':
            stuckN[col].append(top - row - 1)
            stuckW[top - row - 1].append(side - col - 1)
            stuckS[side - col - 1].appendleft(row)
            stuckE[row].appendleft(col)

outcomes = []
cycleStart = 0
cycleEnd = 0
numCycles = 1000000000
end = False
for i in range(numCycles):
    N, moving = rotate(data, stuckN, moving, top, side)
    W, moving = rotate(data, stuckW, moving, side, top)
    S, moving = rotate(data, stuckS, moving, top, side)
    E, moving = rotate(data, stuckE, moving, side, top)

    ans = 0
    for vals in moving.values():
        ans += sum(vals) + len(vals)
        
    if (N, W, S, E, ans) in outcomes:
        cycleEnd = i
        cycleStart = outcomes.index((N, W, S, E, ans))
        break
    outcomes.append((N, W, S, E, ans))

outcomes = outcomes[cycleStart:]
index = (numCycles - cycleStart) % len(outcomes) - 1
print(outcomes[index][4])
