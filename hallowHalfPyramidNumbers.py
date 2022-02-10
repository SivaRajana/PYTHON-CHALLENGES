# 1
# 1 2
# 1   3
# 1     4
# 1 2 3 4 5 
N = int(input())
for i in range(1, N+1):
    if(i == 1):
        print ("1")
    elif (i == N):
        pattern = ""
        for j in range(1, N+1):
            pattern = pattern + str(j) + " "
        print (pattern)
    else:
        pattern = "1 "
        for k in range(i-2):
            pattern = pattern + "  "  
        pattern = pattern + str (i)
        print (pattern)
