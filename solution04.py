import re
from collections import defaultdict
with open('input4.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

ans = 0
copies = defaultdict(lambda: 1)

for (i, line) in enumerate(data, start=1):
    ans += copies[i]
    line = re.sub(' +', ' ', line)
    start, vals = line.split(':')
    cnum = start.strip().split(' ')[1]
    win, card = vals.strip().split('|')
    winners = {x: 0 for x in win.strip().split(' ')}
    val = 0
    for num in card.strip().split(' '):
        if num in winners:
            winners[num] += 1
            val += 1
    for j in range(i + 1, i + val + 1):
        copies[j] += copies[i]
print(ans)
    
