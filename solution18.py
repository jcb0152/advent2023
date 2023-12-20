
with open('input18.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

dirs = {
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0),
    'R': (0, 1)
    }

encoded = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
    }

path = []
row = 0
col = 0

path.append((row, col))
border = 0

for line in data:
    direc, amt, color = line.split(' ')

    amt, direc = color[2:7], color[7]
 
    direc = encoded[direc]
    amt = int(amt, 16)

    rowoff = amt * dirs[direc][0]
    coloff = amt * dirs[direc][1]
    row += rowoff
    col += coloff

    path.append((row, col))
    border += amt

area = 0
for i in range(len(path) - 1):
    current = path[i]
    other = path[i + 1]
    area += current[0] * other[1] - current[1] * other[0]

area = abs(area * 0.5)
interior = area - border * 0.5 + 1

print(interior + border)
