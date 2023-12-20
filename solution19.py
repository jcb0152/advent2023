
from collections import defaultdict
from operator import mul
from functools import reduce

accepted = []
def combineValues(values1, values2):
    print(values1)
    print(values2)
    if values2 is None:
        return values1

    if values1 is None:
        return values2
    
    newValues = {}
    for key in 'xmas':
        low1, high1 = values1[key]
        low2, high2 = values2[key]
        low = min(low1, low2)
        high = max(high1, high2)
        newValues[key] = (low, high)
    return newValues

def updateValues(condition, values):
    newValues = dict(values.items())
    remaining = dict(values.items())

    if condition == True:
        return newValues, None
    
    if '<' in condition:
        var, num = condition.split('<')
        op = '<'
        
    if '>' in condition:
        var, num = condition.split('>')
        op = '>'
        
    num = int(num)

    small, big = newValues[var]
    low, high = remaining[var]

    if op == '<':
        big = min(big, num - 1)
        low = big + 1

    if op == '>':
        small = max(small, num + 1)
        high = small - 1

    newValues[var] = (small, big)
    remaining[var] = (low, high)
    
    if small > big:
        newValues = None

    if low > high:
        remaining = None
    return newValues, remaining
            
    
def getCombos(steps, step, values):
    if step == 'R' or values is None:
        return None

    if step == 'A':
        accepted.append(values)
        return
    
    current = steps[step]
    remaining = dict(values.items())
    for condition, result in current:
        tmpValues, remaining = updateValues(condition, remaining)
        getCombos(steps, result, tmpValues)
    return
    
with open('input19.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

workflows = []
parts = []

part2 = False
for line in data:
    if line == '':
        part2 = True
        continue
    if not part2:
        workflows.append(line)
        continue
    parts.append(line)
    continue

steps = defaultdict(list)

for line in workflows:
    name, values = line[:-1].split('{')
    values = values.split(',')

    for value in values:
        if ':' in value:
            condition, result = value.split(':')
        else:
            condition, result = True, value

        steps[name].append((condition, result))

possible = {
    'x': (1, 4000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
    }

tmp1 = {
    'x': (1, 2000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
    }

tmp2 = {
    'x': (1, 1000),
    'm': (1, 4000),
    'a': (1, 4000),
    's': (1, 4000)
    }

getCombos(steps, 'in', possible)
#print(reduce(mul, [high - low + 1 for low, high in values.values()]))
ans = 0
for row in accepted:
    ans += reduce(mul, [high - low + 1 for low, high in row.values()])
print(ans)
def checkParts(parts, steps):
    ans = 0
    for part in parts:
        step = 'in'
        ratings = dict([rating.split('=') for rating in part[1:-1].split(',')])

        while True:
            if step == 'A':
                ans += sum(map(int, ratings.values()))
                break

            if step == 'R':
                break
            
            current = steps[step]
            for condition, result in current:
                if condition == True:
                    step = result
                    break

                if '<' in condition:
                    var, num = condition.split('<')
                    if int(ratings[var]) < int(num):
                        step = result
                        break
                    
                if '>' in condition:
                    var, num = condition.split('>')
                    if int(ratings[var]) > int(num):
                        step = result
                        break
    return ans
        
