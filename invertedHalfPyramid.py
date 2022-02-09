N = int(input())
for i in range(0, N):
    line_pattern = ""
    for j in range(N-i):
        line_pattern = line_pattern + str(j+1) + " "
    print (line_pattern)
