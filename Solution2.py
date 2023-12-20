with open('input2.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

ans = 0
games = []
for line in data:
    name, rest = line.split(': ')
    game_num = name.split(' ')[1]
    colors = {'red':0, 'blue':0, 'green':0}

    large = False
    sets = rest.split("; ")
    for val in sets:
        draws = val.split(", ")
        for draw in draws:
            (num, color) = draw.split(' ')
            colors[color] = max(colors[color], int(num))
    ans += colors['red'] * colors['blue'] * colors['green']
  
print(ans)
