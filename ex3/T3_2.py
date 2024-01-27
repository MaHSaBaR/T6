import re

n = int(input())

myset = set()
for i in range(n):
    a = input()
    a = re.findall(r'@(.*)',a)
    if a != []:
        if not a[0] in myset:
           myset.add(a[0])
myset2 = sorted(myset)
for x in myset2:
    print(x)