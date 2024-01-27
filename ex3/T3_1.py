letter = input()

import re
a = re.findall(r'\S{1}\S+',letter)

l2 = []
l = []
for i in range(len(a)):
    l.append((a[i][1:], a[i][0]))

l.sort(key = lambda x: int(x[0]))
for i in range(len(l)):
    l2.append(l[i][1])


print(''.join(l2))

