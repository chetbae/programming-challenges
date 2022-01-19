# backspace
import sys

data = sys.stdin.readlines()
str = data[0]
stk = []
n = len(str)
for i in range(n):
    c = str[i]
    if c != '<':
        stk.append(c)
    else:
        stk.pop(-1)
out = ''.join(stk)
print(out)