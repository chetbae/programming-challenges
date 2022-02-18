import sys

hs = {}
sh = {}
data = sys.stdin.readlines()
for line in data:
    line = line.strip().split()
    if line[0] == "clear":
        hs.clear()
        sh.clear()
    elif line[0] == "def":
        if line[1] in hs:
            sh.pop(hs[line[1]])
        hs[line[1]] = (line[2])
        sh[(line[2])] = line[1]
    else:
        line = line[1:]
        print(" ".join(line), end=" ")
        line = line[:-1]
        for word in line[::2]:
            if not(word in hs):
                print("unknown")
                break
        else:
            line = ["(" + hs[word] + ")" if index%2 == 0 else word for index,word in enumerate(line)]
            line = " ".join(line)
            line = eval(line)
            if (str(line) in sh):
                print(sh[str(line)])
            else:
                print("unknown")
