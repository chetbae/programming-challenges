n = int(input())
key = 'Simon says' # 10 chars

for i in range(n):
    line = input()
    if line[:10] == key:
        print(line[11:])

