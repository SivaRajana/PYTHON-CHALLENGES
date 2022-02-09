#method 1
N = int(input())
for i in range(0, N):
    line_pattern = ""
    for j in range(N-i):
        line_pattern = line_pattern + str(j+1) + " "
    print (line_pattern)
    
#method 2
N = int(input())
i = 0
while (i < N):
    j = 1
    while (j <= (N-i)):
        print (j, end=" ")
        j = j + 1
    print ("")
    i = i + 1
