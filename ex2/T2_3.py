def base(s, b):
    result = ''
    r = 1
    while s != 0:
        r = s % b
        s = int((s - r) / b)
        result += str(r)
    result = result[::-1]
    return result

def numerator(n):
    a = 0
    for i in range(1,n+1):
        if n % i == 0:
            a += i
    return a




l = []
s = 0
w = ''
while l != [-1, -1]:
    l = list(map(int, input().split()))
    if l == [-1,-1]:
        break
    if l[1] > 9 or l[1] < 2:
        w = 'invalid base!'
    else:
        a = base(numerator(l[0]),l[1])
        s += int(a)
    
    
if w == 'invalid base!':
    print(w)
else:
    print(s)

