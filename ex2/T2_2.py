def sum():
    l = []
    a = 0
    s = 0
    while a != 'end':
        l.append(a)
        a = input()
    for i in range(len(l)):
        s += int(l[i])
    return s 


        
def average():
    l = []
    a = 0
    s = 0
    while a != 'end':
        l.append(a)
        a = input()
    for i in range(len(l)):
        s += int(l[i])
    return round(s / (len(l) - 1), 2)

def GCD(a ,b):
    while b != 0: 
        a , b = b , a % b
    return a


def gcd():
    a = input()
    w1 = input()
    w2 = GCD(int(a), int(w1))
    while w1 != 'end':
        w2 = GCD(int(w2), int(w1))
        w1 = input()
        if w1 == 'end':
            break
    return w2


def lcd():
    l = []
    a = input()
    while a != 'end':
        l.append(int(a))
        a = input()
        if a == 'end':
            break
    i = 1
    N = 0
    while N != len(l):
        for n in l:
            if i % n == 0:
                N += 1
        if N == len(l):
            print(i)
            break
        else :
            i += 1
            N = 0

def max():
    l = []
    a = input()
    while a != 'end':
        l.append(int(a))
        a = input()
        if a == 'end':
            break
    while len(l) > 1:
        for n in l:
            for m in l:
                if n > m:
                    l.remove(m)
    return l[0]

def min():
    l = []
    a = input()
    while a != 'end':
        l.append(int(a))
        a = input()
        if a == 'end':
            break
    while len(l) > 1:
        for n in l:
            for m in l:
                if n < m:
                    l.remove(m)
    return l[0]       
        

f = input()
if f == 'sum':
    print(sum())
elif f == 'average':
    print(average())
elif f == 'gcd':
    print(gcd())
elif f =='lcd':
    lcd()
elif f == 'min':
    print(min())
elif f == 'max':
    print(max())
else:
    print('Invalid command')
   