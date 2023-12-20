
from collections import namedtuple, deque, defaultdict

def checkDir(row, col, enter):
    loc = data[row][col]
    
    if loc == 'S':
        return 5

    if enter in nodes[loc]:
        vals = nodes[loc]
        if enter == vals[0]:
            return vals[1]
        return vals[0]
    return -1
        
        
with open('input10.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

'''dirs:
north: 0
east: 1
south: 2
west: 3
'''

'''
data = [
    '7-F7-',
    '.FJ|7',
    'SJLL7',
    '|F--J',
    'LJ.LJ',
    ]
    '''

nodes = {
    '|': (0,2),
    '-': (1,3),
    'L': (0,1),
    'J': (0,3),
    '7': (2,3),
    'F': (1,2),
    '.': tuple(),
    'S': (0,1,2,3)
    }

invert = {
    0: 2,
    1: 3,
    2: 0,
    3: 1
    }

convert = {
    0: (-1,0),
    1: (0,1),
    2: (1,0),
    3: (0,-1)
    }

Node = namedtuple("Node", ["row", "col", "enter", "dist"])
consider = deque()
loop = deque()

for (row, line) in enumerate(data):
    if 'S' not in line:
        continue
    col = line.find('S')

    for i in range(4):
        offset = convert[i]
        if (row + offset[0] in range(0, len(data)) and
            col + offset[1] in range(0, len(data[0]))):
            consider.append(Node(row + offset[0],
                                     col + offset[1],
                                     i,
                                     1))
    loop.append((row, col))
            
ans1 = 0
startdirs = []
while len(consider) != 0:
    row, col, enter, dist = consider.popleft()
    nextDir = checkDir(row, col, invert[enter])
    if nextDir < 0:
        continue

    if len(startdirs) < 2:
        startdirs.append(enter)
        startdirs.sort()
        
    if (row, col) in loop:
        ans1 = dist
        break
    
    loop.append((row, col))
    
    if data[row][col] == 'S':
        ans1 = dist
        break
    
    offset = convert[nextDir]
    
    if (row + offset[0] in range(0, len(data)) and
            col + offset[1] in range(0, len(data[0]))):
            consider.append(Node(row + offset[0],
                                     col + offset[1],
                                     nextDir,
                                     dist + 1))
print(ans1)
s_loc = loop[0]
for letter, dirs in nodes.items():
    if tuple(startdirs) == dirs:
        data[s_loc[0]] = data[s_loc[0]][:s_loc[1]] + letter + data[s_loc[0]][s_loc[1] + 1:]
        break
        
rows = defaultdict(list)
for row, col in loop:
    rows[row].append(col)

ans2 = 0
    
for (row, used) in rows.items():
    small = min(used)
    large = max(used)

    enclosed = False
    last = ''
    for col in range(small, large + 1):
        if (row, col) in loop:
            if data[row][col] in "|":
                enclosed = not enclosed
            
            if data[row][col] in 'LF':
                last = data[row][col]
            if (last, data[row][col]) in [('L', '7'), ('F', 'J')]:
                enclosed = not enclosed
            continue

        if enclosed:
            ans2 += 1
        
print(ans2)
