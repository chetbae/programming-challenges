line = input().lower()
tr = "@ 8 ( |) 3 # 6 [-] | _| |< 1 []\/[] []\[] 0 |D (,) |Z $ '][' |_| \/ \/\/ }{ `/ 2".split()
out = ''
chars = list(line)
for c in chars:
    val = ord(c) - 97
    if 0 <= val <= 26:
        out += tr[val]
    else:
        out += c
print(out)
