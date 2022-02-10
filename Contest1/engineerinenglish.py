import sys
data = sys.stdin.readlines()
db = {}
for line in data:
    out = ''
    words = line.split()
    for word in words:
        if word.lower() in db:
            out += '. '
        else:
            db[word.lower()] = 1
            out += word + ' '
    print(out[:-1])


