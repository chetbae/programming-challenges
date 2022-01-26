'''
Mr. Lucky has a store that sells numbers. These numbers have an interesting property: each number formed by its first 𝑘 digits is evenly divisible by 𝑘, for 𝑘 from 1 to 𝑛, where 𝑛 is the number of digits in the number. The numbers do not have leading zeroes.

Mr. Unlucky wants to open a competing store. Price for lucky numbers is driven by demand and supply, and given by the formula

price=demandsupply
while demand for numbers with 𝑛 digits is given by the formula

demand=citySize⋅dayOfMonth−𝑛𝑒
where 𝑒 is the base of the natural logarithm. Supply for lucky numbers with 𝑛 digits is simply the number of lucky numbers with 𝑛 digits. Help Mr. Unlucky calculate the supply for 𝑛 digit lucky numbers.
'''
n = int(input())
cur = [1,2,3,4,5,6,7,8,9]
nxt = []
for k in range(2, n+1):
    for predigits in cur:
        first_divisible = predigits * 10
        while first_divisible%k != 0:
            first_divisible += 1
        upper_limit = (predigits+1) * 10
        for lucky_num_k in range(first_divisible, upper_limit, k): # count no. of lucky nums in ones col by using k steps
            nxt.append(lucky_num_k)
    cur = nxt
    nxt = []
ans = len(cur)
print(ans)