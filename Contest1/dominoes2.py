N = int(input())

for case in range(N):
    n,m,l = [int(x) for x in input().split()]
    # print(n, m, l)
    db = {}
    hs = set(range(1,n+1))
    out = 0
    for i in range(m):
        x,y = [int(z) for z in input().split()]
        if x in db:
            arr = db.get(x)
            db[x] = (arr + [y])
        else:
            db[x] = [y]
    # print(db)
    for j in range(l):
        A = [int(input())]
        # print(A)
        while A and hs:
            a = A.pop(0)

            # print(hs)
            # print('a:', a, '    out:', out)
            B = db.get(a)
            if a not in hs:
                continue
            hs.remove(a)
            out += 1
            if B:
                A = A + B

    print(out)

