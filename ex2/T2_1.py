n = int(input())

t = ''
l =[]

def fact(n):
    if n == 0:
        fact = 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
    return fact


def choose(n, k):
    return int(fact(n)/(fact(n-k) * fact(k)))


for i in range(n):
    for j in range(i+1):
        t += str(choose(i, j))+ ' '
    l.append(t)
    t = ''

for i in l:
    print(i)


    
