
import functools
import itertools
import re

def bruteforce(groupstr, pattern):
    unknowns = groupstr.count('?')
    replacements = itertools.product('.#', repeat=unknowns)
    ans = 0
    for seq in replacements:
        groupseq = groupstr.split('?')
        values = list(itertools.zip_longest(groupseq, seq, fillvalue=''))
        tempstr = ''.join([''.join(tup) for tup in values])
        if pattern.match(tempstr):
            ans += 1
    return ans
    
@functools.cache
def isValid(group, value):
    for (a, b) in zip(group, value):
        if a == '?':
            continue
        if a != b:
            return False
    return True

@functools.cache
def countArrangements(groups, damaged):
    
    if sum(map(len, groups)) < sum(map(len, damaged)):
        return 0

    if sum(map(len, groups)) == sum(map(len, damaged)):
        groupstr = ''.join(groups)
        damagedstr = ''.join(damaged)
        if isValid(groupstr, damagedstr):
            return 1
        else:
            return 0

    if len(damaged) == 0:
        groupstr = ''.join(groups)
        damagedstr = '.' * len(groupstr)
        if isValid(groupstr, damagedstr):
            return 1
        else:
            return 0
    current, *remaining = damaged

    ans = 0
    for groupnum, group in enumerate(groups):
        for startPos in range(len(group) - len(current) + 1):
            if '#' in group[:startPos]:
                break
            if isValid(group[startPos:], current):
                val = group[startPos + len(current):]
                newGroups = [val, *groups[groupnum + 1:]]
                ans += countArrangements(tuple(newGroups), tuple(remaining))
        if '#' in group:
            break
    return ans
            
with open('input12.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]
    
ans = 0
dup = 5
for line in data:
    springs, other = line.split(' ')
    springs = '?'.join([springs] * dup)
    other = ','.join([other]*dup)
    damaged = list(map(int, other.split(',')))
    groups = list(filter(None, springs.split('.')))

    '''
    regex = '^\.*' + '\.+'.join(['#'*i for i in damaged]) + '\.*$'
    pattern = re.compile(regex)
    tmp1 = bruteforce('.'.join(groups), pattern)
    '''
    
    groups = [group + '.' for group in groups]
    damaged = ['#' * size + '.' for size in damaged]
    
    ans += countArrangements(tuple(groups), tuple(damaged))
    
print(ans)
