n = int(input())
m = int(input())

N = bin(n)
M = bin(m)

if len(str(N)) > len(str(M)) :
    m3 =(len(str(N))-len(str(M)))*'0'+ str(M)
    m3=m3.replace('0b','')
    n3 = str(N).replace('0b','')

elif len(str(N)) < len(str(M)) :
    n3 =(len(str(M))-len(str(N)))*'0'+ str(N)
    n3=n3.replace('0b','')
    m3 = str(M).replace('0b','')

else:
    n3=str(N).replace('0b','')
    m3=str(M).replace('0b','')

l=[]
for i in range(len(n3)):
    a = int(n3[i])+int(m3[i]) 
    if a == 1:
        l.append(a)
    


print(len(l))

