import numpy as np

file_name = input('') + '.txt'
with open(file_name) as f:
    reader = f.readlines()

    n = reader[0].split(' ')[0]
    n = int(n)
    m = reader[0].split(' ')[1]
    m = int(m)

    M = np.zeros((m,m))

    matrix_list = []
    for i in range(1,n*m + 1,m):
        for j in range(m):
            M[j] = reader[i+j].split(' ')
        matrix_list.append(M)
        M = np.zeros((m,m))


    dict = {}
    for k in matrix_list:
        det = np.linalg.det(k)
        dict[det] = k

    l = list(dict.keys())
    l.sort()
    positive = []
    negative = []
    for x in l:
        if x <= 0:
            negative.append(x)
        else:
            positive.append(x)
    
    positive.sort(reverse= True)
    negative.sort()
    
    if len(positive) > 1 and len(negative) > 1:
        if positive[0]*positive[1] > negative[0]*negative[1]:
            X = np.matmul(dict[positive[0]],dict[positive[1]])
        else:
            X = np.matmul(dict[negative[1]],dict[negative[0]])

    elif len(positive) <= 1:
        X = np.matmul(dict[l[1]],dict[l[0]])
    elif len(negative) <= 1 :
        X = np.matmul(dict[l.pop()],dict[l.pop()])

    X = np.linalg.inv(X)


    for i in range(m):
        for j in range(m -1):
            print(format(X[i][j],'.3f'), end = ' ')
        print(format(X[i][m-1],'.3f'))



            






