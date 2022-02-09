# planting trees

n = int(input())
days = [int(x) for x in input().split()]

ord_days = sorted(days, reverse=True)
out = 0
for i, c in enumerate(ord_days, start=2):
    out = max(out, i + c)
print(out)