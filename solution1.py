import string
with open('input1.txt', 'r') as f:
    data = [line.rstrip("\n") for line in f]

values = ["one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
tricks = [("nineight", "98"), ("eighthree", "83"),
          ("eightwo", "82"), ("sevenine", "79"),
          ("fiveight", "58"), ("threeight", "38"),
          ("twone", "21"), ("oneight", "18")]
ans = 0
for line in data:
    for (trick, val) in tricks:
        line = line.replace(trick, str(val))
        
    for (i, value) in enumerate(values, start=1):
        line = line.replace(value, str(i))
    left = -1
    right = -1
    for char in line:
        if char in string.digits:
            right = int(char)
            if left == -1:
                left = int(char)
    ans += 10 * left + right

print(ans)
    
