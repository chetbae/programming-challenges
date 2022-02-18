data = input()
data = data.split()
h = int(data[0])
idx = 0
level = 0

if len(data) == 2:
    path = list(data[1])
else:
    path = []
for dir in path:
    if dir == 'L':
        idx = idx*2
    elif dir =='R':
        idx = idx*2 + 1
    level += 1
out = (2 ** (h+1)) - (2 ** (level)) - idx
print(out)

