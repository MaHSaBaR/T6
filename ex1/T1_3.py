a = int(input())
b = int(input())

a2= bin(a)
a2 = str(a2).replace('0b','')
a2 = (32-len(a2))*'0' + a2

b2= bin(b)
b2 = str(b2).replace('0b','')
b2 = (32-len(b2))*'0' + b2

c = b2 + a2
c = c[::-1]

n = int(input())
for i in range(n):
    p = int(input())
    if c[p] == '1':
        print('yes')
    elif c[p] == '0':
        print('no')
