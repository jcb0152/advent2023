import re
import math
with open('input6.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

data = [re.sub(' +', '', line) for line in data]
data = [line.split(':')[1:] for line in data]
cases = list(zip(*data))
print(cases)
ans = 1
for time, dist in cases:
    time = int(time)
    dist = int(dist)
    low = math.floor(0.5 * (time - (time ** 2 - 4 * dist) ** 0.5) + 1)
    high = math.ceil(0.5 * (time + (time ** 2 - 4 * dist) ** 0.5) - 1)
    ans = (high - low + 1)
print(ans)
