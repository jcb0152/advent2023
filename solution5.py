from collections import deque

def convertBounds(seeds, conversions):
    seeds = deque(seeds)
    conversions = deque(conversions)
    newBounds = []
    low, high = seeds.popleft()
    ((start, end), diff) = conversions.popleft()
    while True:
        if low < start:
            if high < start:
                newBounds.append((low, high))
                if len(seeds) > 0:
                    (low, high) = seeds.popleft()
                    continue
                else:
                    break
            newBounds.append((low, start))
            low = start
            continue
        if low < end:
            if high < end:
                newBounds.append((low + diff, high + diff))
                if len(seeds) > 0:
                    (low, high) = seeds.popleft()
                    continue
                else:
                    break
            newBounds.append((low + diff, end + diff))
            low = end
            continue
        if len(conversions) > 0:
            ((start, end), diff) = conversions.popleft()
            continue
        else:
            newBounds.append((low, high))
            newBounds.extend(seeds)
            break
    return newBounds
        
        
with open('input5.txt', 'r') as f:
    first, _, *data = [line.rstrip("\n") for line in f]

seeds = first.split(":")[1].strip().split(' ')
seeds = list(map(lambda x, y: tuple((int(x), int(x) + int(y))), seeds[0::2], seeds[1::2]))

conversions = []
data.append('')
for line in data:
    if 'map' in line:
        continue

    if line == '':
        conversions.sort(key = lambda x: x[0][0])
        seeds.sort(key = lambda x: x[0])
        seeds = convertBounds(seeds, conversions)
        conversions = []
        continue

    vals = (list(map(int, line.split())))
    conversions.append(((vals[1], vals[1] + vals[2]), vals[0] - vals[1]))

print(min(seeds))
