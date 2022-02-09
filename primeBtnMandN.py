M = int(input())
N = int(input())
for i in range(M,N+1):
    flag = True
    for j in range(2,i):
        if (i % j == 0):
            flag = False
    if(flag):
        print (i)
