
from collections import defaultdict, OrderedDict

def hashval(val):
    currentValue = 0
    for character in val:
        ascVal = ord(character)
        currentValue += ascVal
        currentValue *= 17
        currentValue = currentValue % 256
    return currentValue

with open('input15.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

boxes = defaultdict(OrderedDict)
ans = 0
data = data[0].split(',')
for line in data:
    
    sep = ''
    if '=' in line:
        sep = '='
    else:
        sep = '-'

    lens = line.split(sep)
    
    label = lens[0]
    boxnum = hashval(label)

    if sep == '=':
        size = int(lens[1])
        boxes[boxnum][label] = size
    if sep == '-':
        if label in boxes[boxnum]:
            boxes[boxnum].move_to_end(label)
            boxes[boxnum].popitem()

ans = 0
for box, values in boxes.items():
    for index, (_, size) in enumerate(values.items()):
        ans += (box + 1) * (index + 1) * size

print(ans)
