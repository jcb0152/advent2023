from collections import defaultdict
import itertools
import math

with open('input8.txt', 'r') as f:
    order, _, *data = [line.rstrip("\n") for line in f]

''' 
order = 'LR'
data = [
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)'
    ]
    '''
routes = defaultdict(dict)
begin = []
target = []
for line in data:
    start, _, tup1, tup2 = line.split(' ')
    L, R = tup1[1:-1], tup2[:-1]
    routes[start]['L'], routes[start]['R'] = L, R
    if start[2] == 'A':
        begin.append(start)
    elif start[2] == 'Z':
        target.append(start)

distances = dict()
for loc in begin:
    current = loc
    dist = 0
    targets = 0
    offset = 0
    for dir in itertools.cycle(order):
        dist += 1
        current = routes[current][dir]
        if current in target:
            if offset == 0:
                offset = dist
            else:
                distances[loc] = (offset, dist)
                break
print(distances.values())

print(math.lcm(*list(map(lambda x: x[1], distances.values()))) / 2)

