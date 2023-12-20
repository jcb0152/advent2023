
def getNext(seq):
    if all(map(lambda x: x == 0, seq)):
        return 0
    diffs = [(seq[i + 1] - seq[i]) for i in range(0, len(seq) - 1)]
    return seq[-1] + getNext(diffs)
    
with open('input9.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]
'''
data = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45'
    ]
'''
ans = 0
for line in data:
    seq = list(map(int, line.split(' ')))
    seq = list(reversed(seq))
    ans += getNext(seq)

print(ans)

