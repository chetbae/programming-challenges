n = int(input())
for i in range(n):
    g = int(input())
    ids = [int(x) for x in input().split()]
    db = {}
    for id in ids:
        if id in db:
            db.pop(id)
        else:
            db[id] = 1
    keys = db.keys()
    for key in keys:
        out = key

    print('Case #' + str(i+1) + ': ' + str(out))