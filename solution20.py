
from collections import deque, defaultdict
import math

with open('input20.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

class Node():
    def __init__(self, mode, connections):
        self.mode = mode
        if mode == '%':
            self.state = 0
        elif mode == '&':
            self.state = {}
        self.receivers = connections

    def setInputs(self, nodes):
        if self.mode != '&':
            return
        if type(nodes) == str:
            nodes = [nodes]
        for name in nodes:
            self.state[name] = 0
        
    def process(self, value):
        signal, name = value
        newSignal = None
        if self.mode == '%':
            if signal == 1:
                return None, self.receivers
            if signal == 0:
                self.state = 1 - self.state
                newSignal = self.state

        if self.mode == '&':
            self.state[name] = signal
            if sum(self.state.values()) == len(self.state.values()):
                newSignal = 0
            else:
                newSignal = 1

        if self.mode == 'start':
            newSignal = 0

        #print(f'sending {newSignal} to {self.receivers}')
        return newSignal, self.receivers

    def getState(self):
        if self.mode == '&':
            return sum(self.state.values())
        if self.mode == '%':
            return self.state
        return 0

nodes = {}
values = defaultdict(list)
cons = ['rx']
nodes['rx'] = Node('&', [])
for line in data:
    if 'broadcaster' in line:
        mode = 'start'
    else:
        mode = line[0]
        line = line[1:]
        
    name, _, connections = line.split(' ', 2)
    connections = connections.split(', ')
    nodes[name] = Node(mode, connections)
    for val in connections:
        values[val].append(name)
    if mode == '&':
        cons.append(name)

for name in cons:
    nodes[name].setInputs(values[name])

signals = deque()
low = 0
high = 0
num = 1000
cycle = 0
important = {}
vals = ['qs', 'sv', 'pg', 'sp']
while True:
    #num -= 1
    low += 1
    cycle += 1
    signals.append(('broadcaster', (0, 'button')))
    while signals:
        current, signal = signals.popleft()
        #print('Node', current)
        newSignal, receivers = nodes[current].process(signal)

        val = len(receivers)

        if newSignal is None:
            continue
        
        if newSignal == 0:
            low += val
        else:
            high += val

        for nodeName in receivers:
            for val in vals:
                if val not in important and val in receivers and newSignal == 0:
                    important[val] = cycle
            if nodeName in nodes:
                signals.append((nodeName, (newSignal, current)))

    if len(important) >= 4:
        break

print(important)
print(math.lcm(*list(important.values())))

