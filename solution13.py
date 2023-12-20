
def hamming(seq1, seq2):
    return sum(i != j for (i, j) in zip(seq1, seq2))

from collections import defaultdict
with open('input13.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

data.append('')
case = []
ans = 0
for line in data:
    if line != "":
        case.append(line)
        continue

    rows = case
    cols = list(zip(*rows))

    for i in range(1, len(rows)):
        start = list(reversed(rows[:i]))
        end = rows[i:]
        size = min(len(end), len(start))

        if len(end) > len(start):
            end = end[:size]
        elif len(start) > len(end):
            start = start[:size]
        if sum(hamming(seq1, seq2) for seq1, seq2 in zip(start, end))  == 1:
            ans += 100 * i
            
    for i in range(1, len(cols)):
        start = list(reversed(cols[:i]))
        end = cols[i:]
        size = min(len(end), len(start))

        if len(end) > len(start):
            end = end[:size]
        elif len(start) > len(end):
            start = start[:size]
        if sum(hamming(seq1, seq2) for seq1, seq2 in zip(start, end))  == 1:
            ans += i
    case = []
print(ans)
