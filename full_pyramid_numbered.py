N = int(input())
for i in range(1, N+1):
    line_pattern = " " * (N-i)
    for j in range(1, i+1):
        line_pattern = line_pattern + str(j) + " "
    print(line_pattern)
    
    
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 

n = int(input())
start = 1
for row in range(1, n+1):
    print (" " * (n-row), end="")
    for col in range(1, row+1):
        print (start, end=" ")
        start += 1
    print ()
