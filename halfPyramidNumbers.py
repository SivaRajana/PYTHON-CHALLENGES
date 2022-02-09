N = int(input())
for i in range(1, N+1):
    line_pattern = ""
    for j in range(1,i+1):
        line_pattern = line_pattern + str(j) + " "
    print (line_pattern)
