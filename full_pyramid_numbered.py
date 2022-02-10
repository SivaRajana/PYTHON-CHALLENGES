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
