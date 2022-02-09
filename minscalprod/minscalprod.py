# minimum scalar product
pound = "#"
n_tests = int(input())
tests = []
for i in range(n_tests):
    l = int(input())
    x = [int(xi) for xi in input().split()]
    y = [int(yi) for yi in input().split()]
    tests.append((l, x, y))

for i, test in enumerate(tests, start=1):
    l, x, y = test
    x,y = sorted(x), sorted(y)
    out = 0
    for c in range(l):
        out += x[c] * y[-(c+1)]
    print("Case #" + str(i) + ": " + str(out))