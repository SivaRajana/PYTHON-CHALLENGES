# 1 2 3 
# 4 5 6 
# 7 8 9 

N = int(input())
number = 0
for i in range(N):
    line = ""
    for j in range(N):
        number = number + 1
        line = line + str(number) + " "
    print (line)
