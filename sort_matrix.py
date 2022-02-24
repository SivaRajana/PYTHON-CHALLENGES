M, N = input().split()
M, N = int(M), int(N)

matrix = []
for i in range(M):
    integers = input().split()
    matrix.append(integers)
# print (matrix)

all_numbers_list = []
for i in range(M):
    for j in range(N):
        all_numbers_list.append(int(matrix[i][j]))
# print (all_numbers_list)
all_numbers_list.sort()

index = 0
for row in range(M):
    for col in range(N):
        # print (index)
        print (all_numbers_list[index], end = " ")
        index = index + 1
    print ()

        
        
        
