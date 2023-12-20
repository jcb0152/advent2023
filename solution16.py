
from collections import defaultdict, deque

def getEner(startLoc, startDir):
    ener = defaultdict(list)
    moves = deque([(startLoc, startDir)])

    while(len(moves) > 0):
        currentLoc, currentDir = moves.popleft()
        
        if currentLoc in ener and currentDir in ener[currentLoc]:
            continue

        row, col = currentLoc

        if ((row < 0 or row > len(data) - 1) or
            (col < 0 or col > len(data[0]) - 1)):
            continue

        ener[currentLoc].append(currentDir)
        cell = data[row][col]

        if cell == '.':
            rowoff, coloff = dirs[currentDir]
            newLoc = (row + rowoff, col + coloff)
            moves.appendleft((newLoc, currentDir))
            continue
        
        if cell in '/\\':
            if (cell == '/' and currentDir in 'NS' or
                cell == '\\' and currentDir in 'EW'):
                newDir = right[currentDir]
            else:
                newDir = left[currentDir]

            rowoff, coloff = dirs[newDir]
            newLoc = (row + rowoff, col + coloff)
            moves.appendleft((newLoc, newDir))
            continue

        if cell in '|-':
            if (cell == '|' and currentDir in 'EW' or
                cell == '-' and currentDir in 'NS'):
                newDirs = [left[currentDir], right[currentDir]]
            else:
                newDirs = [currentDir]

            for newDir in newDirs:
                rowoff, coloff = dirs[newDir]
                newLoc = (row + rowoff, col + coloff)
                moves.appendleft((newLoc, newDir))
            continue
    return len(ener.keys())
    
with open('input16.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

dirs = {
    'N': (-1,0),
    'E': (0,1),
    'S': (1,0),
    'W': (0,-1)
    }

right = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
    }

left = {
    'N': 'W',
    'E': 'N',
    'S': 'E',
    'W': 'S'
    }

startLoc = (0,0)
startDir = 'E'

height = len(data)
width = len(data[0])

southStart = [((0, col), 'S') for col in range(width)]
eastStart = [((row, 0), 'E') for row in range(height)]
northStart = [((height - 1, col), 'N') for col in range(width)]
westStart = [((row, width - 1), 'W') for row in range(height)]

startValues = [*southStart, *eastStart, *northStart, *westStart]

ans = 0
for startLoc, startDir in startValues:
    ans = max(ans, getEner(startLoc, startDir))
print(ans)
