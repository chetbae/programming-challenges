import math
e,f,c = [int(x) for x in input().split()]
n = e + f
out = 0
while n >= c:
    mod, div = n%c, n//c
    out += div
    n = mod + div
print(out)
