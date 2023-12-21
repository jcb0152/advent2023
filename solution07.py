from collections import defaultdict
def score(hand):
    held = defaultdict(int)
    jokes = 0
    for card in hand:
        if card == 'J':
            jokes += 1
        else:
            held[card] += 1
    totals = list(held.values())
    totals.sort()
    totals = totals or [0]
    totals[-1] += jokes
    rank = {
        (5,): 6,
        (1, 4): 5,
        (2, 3): 4,
        (1, 1, 3): 3,
        (1, 2, 2): 2,
        (1, 1, 1, 2): 1,
        (1, 1, 1, 1, 1): 0
        }[tuple(totals)]
    nums = []
    convert = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    for val in hand:
        if val in convert:
            nums.append(convert[val])
        else:
            nums.append(int(val))
    return (rank, *nums)
        
    
with open('input7.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

'''data = [
    "32T3K 765",
    "T55J5 684",
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483'
    ]'''

nums = []
for line in data:
    hand, rank = line.split(' ')
    nums.append((score(hand), rank))

nums.sort(key = lambda x: x[0])
ans = 0
for (i, (row, score)) in enumerate(nums, start = 1):
    ans += i * int(score)
print(ans)
