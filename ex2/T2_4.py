n = int(input())
l = []
ypoint= [0]
xpoint = [0]
for i in range(2):
    l.append('.' * n)

l[0] = [*l[0]]
l[0][0] = '*'
l[0] = ''.join(l[0])

i = 0
j = 0

r = []
d = ''
while d != 'END':
    d = input()
    if d == 'R':
        if j != n-1:
            j += 1
            l[i] = [*l[i]]
            l[i][j] = '*'
            l[i] = ''.join(l[i])
            ypoint.append(i)
            xpoint.append(j)
    if d == 'L':
        if j != 0:
            j -= 1
            l[i] = [*l[i]]
            l[i][j] = '*'
            l[i] = ''.join(l[i])
            ypoint.append(i)
            xpoint.append(j)
    if d == 'B':
        i += 1
        l[i] = [*l[i]]
        l[i][j] = '*'
        l[i] = ''.join(l[i])
        l.append('.' * n)
        r.append(d)
        ypoint.append(i)
        xpoint.append(j)

h = len(r)

T = 0
if h != ypoint.pop() or xpoint.pop() != n-1:
    T = 1


for i in range(h + 1):
    l[i] = [*l[i]]
    l[i] = ' '.join(l[i])


for i in range(h + 1):
    print(l[i])

if T == 1:
    print('There\'s no way out!')


 
