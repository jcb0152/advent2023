
import itertools
with open('input11.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

galaxies = []
rows = set()
cols = set()

numRows = len(data)
numCols = len(data[0])
for (row, line) in enumerate(data):
    for (col, char) in enumerate(line):
        if char == '#':
            galaxies.append((row, col))
            rows.add(row)
            cols.add(col)

dRows = set(range(0, numRows)).difference(rows)
dCols = set(range(0, numCols)).difference(cols)

pairs = itertools.combinations(galaxies, 2)

ans = 0
dups = 1000000
for (startr, startc), (endr, endc) in pairs:
    lowr = min(startr, endr)
    highr = max(startr, endr)
    lowc = min(startc, endc)
    highc = max(startc, endc)

    dist = highr - lowr + (dups - 1) * len(set.intersection(dRows, set(range(lowr, highr))))
    dist += highc - lowc + (dups - 1) * len(set.intersection(dCols, set(range(lowc, highc))))

    ans += dist

print(ans)
