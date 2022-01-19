# countingstars
import sys

dims = []
matrices = []

data = sys.stdin.readlines()
i = 0
while i < len(data):
    foo = data[i]
    m, n = list(map(lambda s: int(s), foo.split()))
    print(m,n)
    dims.append((m,n))
    matrix = data[i+1:i+1+m]
    matrices.append(matrix)
    i += 1 + m

for dim, mat in zip(dims, matrices):
    print(dim, mat)
