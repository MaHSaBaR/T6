a = str(input()).strip()
n = int(input())
a = a.split(' ')
s = set(a)
ind = set(enumerate(a))
l = []
s2 = set()
for i,x in ind:
    y = n - int(x)
    y = str(y)
    s.remove(x)
    if y in s:
        if not y in s2:
            l.append(i+a.index(y))
            s2.add(x)
    s.add(x)

l = sorted(l)

if len(l) == 0:
    print('Not Found!')
else:
    for x in l:
        print(x)
