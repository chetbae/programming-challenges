# busnumbers
import sys

data = sys.stdin.readlines()
n = int(data[0])
numbers = list(map(lambda s: int(s), data[1].split()))

res = ''
numbers.sort()

res += str(numbers[0])
if n < 3: 
    for i in range(1,n):
        res += ' ' + str(numbers[i])
    print(res)
prev = numbers[0]
count = 0
appd = ''
for i in range(1,n):
    num = numbers[i]
    if prev+1 == num:
        if count > 0:
            appd = '-' + str(num)
        else:
            res += appd
            appd = ' ' + str(num)
        count += 1
    else:
        # if count == 0:
        #     res += appd
        res += appd
        count = 0
        appd = ' ' + str(num)
    prev = num
res += appd
print(res)

