
import heapq
from collections import defaultdict
import itertools

with open('input17.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

dirs = {
    'N': (-1,0),
    'E': (0,1),
    'S': (1,0),
    'W': (0,-1)
    }

reverse = {
    'N': 'S',
    'E': 'W',
    'S': 'N',
    'W': 'E'
    }

checked = []
visited = []

height = len(data)
width = len(data[0])

startHeat = 0
startLoc = (0,0)
startDir = None
startConsec = 0
remain = (height - 0) + (width - 0)

moves = []

ans = 0
consecHigh = 10
consecLow = 4

tmp = 0
heapq.heappush(moves, (height + width, startHeat, startLoc, startDir, (-1, -1)))
while moves:
    value, heat, loc, direction, prev = heapq.heappop(moves)
    if (loc, direction) in visited:
        continue

    visited.append((loc, direction))

    if loc == (height - 1,width - 1):
        ans = heat
        break

    for (newDir, (rowoff, coloff)) in dirs.items():
        if direction is not None and (newDir == direction or newDir == reverse[direction]):
            continue

        newRow, newCol = loc[0], loc[1]
        newHeat = heat

        for i in range(consecHigh):
            newRow += rowoff
            newCol += coloff

            if newRow not in range(height) or newCol not in range(width):
                break
            
            newHeat += int(data[newRow][newCol])

            if i < consecLow - 1:
                continue
            tmp = newHeat + height - newRow + width - newCol
            heapq.heappush(moves, (tmp, newHeat, (newRow, newCol), newDir, loc))

print(ans)
        
        
def old2():
    pass
    '''
    prevHeat = 0
    heapq.heappush(moves, (startHeat, startConsec, startLoc, startDir, (-1, -1)))
    while moves:
        heat, consec, loc, direction, prev = heapq.heappop(moves)

        if (loc, direction, consec) in visited:
            continue

        visited.append((loc, direction, consec))

        if loc == (height - 1, width - 1):
            ans = heat
            break
        
        for (val, (rowoff, coloff)) in dirs.items():

            newDir = val

            if val == reverse[direction]:
                continue
            
            if val == direction:
                newConsec = consec + 1
            else:
                newConsec = 1

            if newConsec > 3:
                continue

            newRow, newCol = loc[0] + rowoff, loc[1] + coloff

            if newRow not in range(height) or newCol not in range(width):
                continue

            cost = int(data[newRow][newCol])

            newHeat = heat + cost

            heapq.heappush(moves, (newHeat, newConsec, (newRow, newCol), newDir, loc))

    print(ans)
    '''

def old():
    pass
    '''
if newConsec > 3:
            continue
            heat1, _, _, loc2 = visited[loc][0]
            for tmpheat, _, _, _ in visited[loc][1:]:
                break
                heatdif = tmpheat - heat1
                heapq.heappush(moves, (newHeat + heatdif, 1, (newRow, newCol), newDir, loc))
                
            heat2, _, _, loc3 = visited[loc2][0]
            for tmpheat, _, _, _ in visited[loc2][1:]:
                break
                heatdif = tmpheat - heat2
                heapq.heappush(moves, (newHeat + heatdif, 1, (newRow, newCol), newDir, loc))
                
            heat3, _, _, _ = visited[loc3][0]
            for tmpheat, _, _, _ in visited[loc3][1:]:
                heatdif = tmpheat - heat3
                heapq.heappush(moves, (newHeat + heatdif, 1, (newRow, newCol), newDir, loc))
            continue
            '''

        
