import math
n = int(input())

split = math.log2(n)
days = math.ceil(split) + 1
print(days)