l = list(map(int,input().split()))

if l[0] <= l[1]:
    c1 = 0
    for i in range(l[0],l[1]+1):
        c2= 0
        for j in range(1,i):
            if i % j == 0:
                c2 += 1
        if c2== 1:
            c1 += 1
    print('main order - amount: '+ str(c1))
elif l[0] > l[1]:
    c1 = 0
    for i in range(l[1],l[0]+1):
        c2= 0
        for j in range(1,i):
            if i % j == 0:
                c2 += 1
        if c2== 1:
            c1 += 1
    print('reverse order - amount: '+ str(c1))





